"""Public API for Device API."""
from __future__ import absolute_import
import base64
from collections import defaultdict
import logging
import Queue
import threading
import time
import urllib

# Import common functions and exceptions from frontend API
from mbed_cloud import BaseAPI
from mbed_cloud.decorators import catch_exceptions
from mbed_cloud.exceptions import AsyncError
from mbed_cloud.exceptions import UnhandledError
from mbed_cloud import PaginatedResponse

# Import backend API
import mbed_cloud._backends.device_catalog as dc
from mbed_cloud._backends.device_catalog.models import \
    DeviceDetail as DeviceDetailBackend
from mbed_cloud._backends.device_catalog.rest import \
    ApiException as DeviceCatalogApiException
import mbed_cloud._backends.device_query_service as dc_queries
from mbed_cloud._backends.device_query_service.models import \
    DeviceQueryDetail
from mbed_cloud._backends.device_query_service.rest import \
    ApiException as DeviceQueryServiceApiException
import mbed_cloud._backends.mds as mds
from mbed_cloud._backends.mds.rest import ApiException as MdsApiException

LOG = logging.getLogger(__name__)


class DeviceAPI(BaseAPI):
    """Describing the public device API.

    Exposing functionality from the following underlying services:
        - Connector / mDS
        - Device query service
        - Device catlog
    """

    def __init__(self, params={}, b64decode=True):
        """Setup the backend APIs with provided config.

        In addition we need to setup some special handling of background
        threads for the mDS functionality - as it relies on background polling.
        """
        super(DeviceAPI, self).__init__(params)

        # Initialize the wrapped APIs
        self.mds = self._init_api(mds)
        self.dc = self._init_api(dc)
        self.dc_queries = self._init_api(dc_queries)

        self._db = {}
        self._queues = defaultdict(lambda: defaultdict(Queue.Queue))

        self._long_polling_thread = _LongPollingThread(self._db, self._queues, b64decode=b64decode)
        self._long_polling_thread.daemon = True

    def start_long_polling(self):
        """Start the long-polling thread.

        If not an external callback is setup (using `register_webhook`) then
        calling this function is mandatory.
        """
        self._long_polling_thread.start()

    def stop_long_polling(self):
        """Stop the long-polling thread."""
        self._long_polling_thread.stop()

    @catch_exceptions(MdsApiException)
    def list_endpoints(self, start=0, sort_by=None, sort_direction="asc"):
        """List all endpoints.

        :param start: Not yet implemented.
        :param sort_by: Not yet implemented.
        :param sort_direction: Not yet implemented.
        :returns: a list of device objects registered in the catalog.
        """
        if start != 0 or sort_by is not None or sort_direction != "asc":
            raise NotImplementedError("Sorting and pagination is not yet implemented")

        api = self.mds.EndpointsApi()
        return api.v2_endpoints_get()

    @catch_exceptions(MdsApiException)
    def list_resources(self, endpoint_name):
        """List all resources registered to a connected endpoint/device."""
        api = self.mds.EndpointsApi()
        return api.v2_endpoints_endpoint_name_get(endpoint_name)

    @catch_exceptions(MdsApiException)
    def get_resource_value(self, endpoint_name, resource_path, fix_path=True):
        """Get a resource value for a given endpoint and resource path by blocking thread.

        :param fix_path: if True then the leading /, if found, will be stripped before
            doing request to backend. This is a requirement for the API to work properly
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_get(endpoint_name, resource_path)

        # The async consumer, which will read data from long-polling thread
        consumer = AsyncConsumer(resp.async_response_id, self._db)

        # We block the thread and get the value for the user.
        return self._get_value_synchronized(consumer)

    @catch_exceptions(MdsApiException)
    def get_resource_value_async(self, endpoint_name, resource_path, fix_path=True):
        """Get a resource value for a given endpoint and resource path.

        :param bool fix_path: strip leading / of path if present
        :return: Consumer object to control asynchronous request
        :rtype: AsyncConsumer
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_get(endpoint_name, resource_path)

        # The async consumer, which will read data from long-polling thread
        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def set_resource_value(self, endpoint_name, resource_path,
                           resource_value, fix_path=True):
        """Set resource value for given resource path, on endpoint."""
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name,
                                                                resource_path,
                                                                resource_value)

        consumer = AsyncConsumer(resp.async_response_id, self._db)
        return self._get_value_synchronized(consumer)

    @catch_exceptions(MdsApiException)
    def set_resource_value_async(self, endpoint_name, resource_path,
                                 resource_value, fix_path=True):
        """Set resource value for given resource path, on endpoint."""
        # When path starts with / we remove the slash, as the API can't handle //.
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_put(endpoint_name,
                                                                resource_path,
                                                                resource_value)
        return AsyncConsumer(resp.async_response_id, self._db)

    @catch_exceptions(MdsApiException)
    def subscribe(self, endpoint_name, resource_path, fix_path=True, queue_size=5):
        """Subscribe to resource updates.

        When called on valid endpoint and resource path a subscription is setup so that
        any update on the resource path value triggers a new element on the FIFO queue.
        The returned object is a native Python Queue object.

        :param fix_path: Removes leading / on resource_path if found.
        :param queue_size: set the Queue size. If set to 0, no queue object will be created.
        """
        # When path starts with / we remove the slash, as the API can't handle //.
        # Keep the original path around however, as we use that for queue registration.
        fixed_path = resource_path
        if fix_path and resource_path.startswith("/"):
            fixed_path = resource_path[1:]

        # Create the queue and register it with the dict holding all queues
        q = Queue.Queue(queue_size) if queue_size > 0 else None
        self._queues[endpoint_name][resource_path] = q

        # Send subscription request
        api = self.mds.SubscriptionsApi()
        api.v2_subscriptions_endpoint_name_resource_path_put(endpoint_name, fixed_path)

        # Return the Queue object to the user
        return q

    @catch_exceptions(MdsApiException)
    def pre_subscribe(self, endpoint_name, resource_path, endpoint_type=""):
        """Create pre-subscription for endpoint and resource path."""
        api = self.mds.SubscriptionsApi()

        presubscription = self.mds.Presubscription(
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            _resource_path=[resource_path]
        )
        api.v2_subscriptions_put([presubscription])

        # Returns void
        return

    @catch_exceptions(MdsApiException)
    def unsubscribe(self, endpoint_name=None, resource_path=None, fix_path=True):
        """Unsubscribe from endpoint and/or resource_path updates.

        If endpoint_name or resource_path is None, we remove every subscripton
        for them. I.e. calling this method without arguments removes all subscriptions,
        but calling it with only endpoint_name removes subscriptions for all resources
        on the given endpoint.

        :param endpoint_name: endpoint to unsubscribe events from. If not
            provided, all registered endpoints will be unsubscribed.
        :param resource_path: resource_path to unsubscribe events from. If not
            provided, all resource paths will be unsubscribed.
        :param fix_path: remove trailing / in resouce path to ensure API works.
        :return: void
        """
        endpoints = filter(None, [endpoint_name])
        if not endpoint_name:
            endpoints = self._queues.keys()
        resource_paths = [resource_path]
        if not resource_path:
            resource_paths = []
            for e in endpoints:
                resource_paths.extend(self._queues[e].keys())

        # Delete the subscriptions
        self._queues.clear()

        api = self.mds.SubscriptionsApi()
        for e in endpoints:
            for r in resource_paths:
                # Fix the path, if required.
                fixed_path = r
                if fix_path and r.startswith("/"):
                    fixed_path = r[1:]

                # Make request to API, ignoring result
                api.v2_subscriptions_endpoint_name_resource_path_delete(endpoint_name, fixed_path)

                # Remove Queue from dictionary
                del self._queues[e][r]
        return

    @catch_exceptions(MdsApiException)
    def register_webhook(self, url, headers={}):
        """Register new webhook for incoming subscriptions.

        If a webhook is already set, this will do an overwrite.

        :param url: the URL with listening webhook (str)
        :return: void
        """
        api = self.mds.NotificationsApi()

        # Send the request to register the webhook
        webhook_obj = self.mds.Webhook(url=url, headers=headers)
        api.v2_notification_callback_put(webhook_obj)
        return

    @catch_exceptions(MdsApiException)
    def deregister_webhook(self):
        """Delete/remove registered webhook.

        If no webhook is registered, an exception (404) will be raised.

        Note that every registered subscription will be deleted as part of
        deregistering a webhook.

        :return: void
        """
        api = self.mds.DefaultApi()
        api.v2_notification_callback_delete()

        # Every subscription will be deleted, so we can clear the queues too.
        self._queues.clear()

        return

    @catch_exceptions(MdsApiException)
    def execute(self, endpoint_name, resource_path, fix_path=True, sync=True, **kwargs):
        """Execute the callback function associated with a resource.

        :param endpoint_name: the endpoint/device to execute on.
        :param resource_path: resource URL on endpoint.
        :param fix_path: ensure leading / is stripped from path to comply with backend API.
        :param sync: run in (blocking) synchronized mode. If false,
            it returns a ::class:`AsyncConsumer`
        :param resource_function: (Optional) Most of the time resources do not
            accept a function but they have their own functions predefined. You can
            use this to trigger them.

        :return: an ::class:`AsyncConsumer` if not `sync` is set to True, in
            which case it returns the value as a string.
        """
        if fix_path and resource_path.startswith("/"):
            resource_path = resource_path[1:]

        api = self.mds.ResourcesApi()
        resp = api.v2_endpoints_endpoint_name_resource_path_post(
            endpoint_name,
            resource_path,
            **kwargs
        )

        consumer = AsyncConsumer(resp.async_response_id, self._db)
        if sync:
            return self._get_value_synchronized(consumer)
        return consumer

    def is_active(self, endpoint_name):
        """Check if endpoint/device has active status."""
        endpoints = self.list_endpoints()
        # Create map by endpoint name, and check if requested endpoint is in it and status is ACTIVE
        active_endpoints = dict((e.name, True) for e in endpoints if e.status == "ACTIVE")
        return active_endpoints.get(endpoint_name, False)

    @catch_exceptions(DeviceCatalogApiException)
    def list_devices(self, **kwargs):
        """List devices in the device catalog.

        :param limit: (Optional) The number of devices to retrieve. (int)
        :param order: (Optional) The ordering direction, ascending (asc) or
            descending (desc) (str)
        :param after: (Optional) Get devices after/starting at given `device_id` (str)
        :param filters: (Optional) Dictionary of filters to apply.
        :returns: a list of device objects registered in the catalog.
        """
        kwargs = self._verify_sort_options(kwargs)
        kwargs = self._verify_filters(kwargs)

        api = self.dc.DefaultApi()
        return PaginatedResponse(api.device_list, **kwargs)

    @catch_exceptions(DeviceCatalogApiException)
    def get_device(self, device_id):
        """Get device details from catalog.

        :param device_id: the ID of the device to retrieve (str)
        :returns: device object matching the `device_id`.
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        return DeviceDetail(api.device_retrieve(device_id))

    @catch_exceptions(DeviceCatalogApiException)
    def update_device(self, device_obj):
        """Get device details from catalog.

        :param device_object: the device_object to pass in for update (device)
        :returns: the new device object
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        return DeviceDetail(api.device_update(device_obj.id, device_obj))

    @catch_exceptions(DeviceCatalogApiException)
    def create_device(self, mechanism, provision_key, **kwargs):
        """Create new device in catalog.

        :param str mechanism: The ID of the channel used to communicate with the device (str)
        :param str provision_key: The key used to provision the device (str)
        :param str account_id: Owning IAM account ID
        :param bool auto_update: Mark this device for auto firmware update
        :param str created_at: When the device was created (ISO-8601)
        :param str custom_attributes: Up to 5 JSON attributes (json encoded)
        :param str deployed_state: State of the device's deployment
        :param str deployment: Last deployment used on the device
        :param str description: Description of the device
        :param str device_class: Class of the device
        :param str id: ID of the device
        :param str manifest: URL for the current device manifest
        :param str mechanism_url: Address of the connector to use
        :param str name: Name of the device
        :param str serial_number: Serial number of device
        :param str state: Current state of device
        :param int trust_class: Trust class of device
        :param int trust_level: Trust level of device
        :param int updated_at: Time the device was updated
        :param int vendor_id: Device vendor ID
        :return: the newly created device object.
        :rtype: DeviceDetail
        """
        api = self.dc.DefaultApi()
        return DeviceDetail(
            api.device_create(mechanism=mechanism, provision_key=provision_key, **kwargs)
        )

    @catch_exceptions(DeviceCatalogApiException)
    def delete_device(self, device_id):
        """Delete device from catalog.

        :param device_id: ID of device in catalog to delete (str)
        :return: void
        """
        api = self.dc.DefaultApi()
        return api.device_destroy(device_id)

    @catch_exceptions(DeviceQueryServiceApiException)
    def list_filters(self, **kwargs):
        """List filters in device query service.

        :param int limit: (Optional) The number of devices to retrieve.
        :param str order: (Optional) The ordering direction, ascending (asc) or
            descending (desc)
        :param str after: (Optional) Get devices after/starting at given `device_id`
        :returns: a list of :py:class:`Filter` objects.
        :rtype: PaginatedResponse
        """
        kwargs = self._verify_sort_options(kwargs)
        api = self.dc_queries.DefaultApi()

        return PaginatedResponse(api.device_query_list, lwrap_type=Filter, **kwargs)

    @catch_exceptions(DeviceQueryServiceApiException)
    def create_filter(self, name, query, custom_attributes=None, **kwargs):
        """Create new filter in device query service.

        :param str name: Name of filter
        :param dict query: Filter properties to apply
        :param dict custom_attributes: Extra filter attributes
        :param return: the newly created filter object.
        :return: the newly created filter object
        :rtype: Filter
        """
        api = self.dc_queries.DefaultApi()

        # Ensure we have the correct types and get the new query object based on
        # passed in query object and custom attributes.
        query = self._get_filter_attributes(query, custom_attributes)

        return Filter(api.device_query_create(name=name, query=query, **kwargs))

    @catch_exceptions(DeviceQueryServiceApiException)
    def update_filter(self, filter_id, name, query, custom_attributes=None, **kwargs):
        """Update existing filter in device query service.

        :param str filter_id: Existing filter ID to update
        :param str name: (New) name of filter
        :param dict query: (New) filter properties to apply
        :param dict custom_attributes: (New) extra filter attributes
        :param return: the newly updated filter object.
        """
        api = self.dc_queries.DefaultApi()

        # Get urlencoded query attribute
        query = self._get_filter_attributes(query, custom_attributes)

        body = self.dc_queries.Body(
            name=name,
            query=query,
            **kwargs
        )

        return api.device_query_update(filter_id, body)

    @catch_exceptions(DeviceQueryServiceApiException)
    def delete_filter(self, filter_id):
        """Delete filter in device query service.

        :param filter_id: id of the filter to delete (int)
        :param return: void
        """
        api = self.dc_queries.DefaultApi()
        return api.device_query_destroy(filter_id)

    @catch_exceptions(DeviceQueryServiceApiException)
    def get_filter(self, filter_id):
        """Get filter in device query service.

        :param int filter_id: id of the filter to get
        :returns: device filter object
        """
        api = self.dc_queries.DefaultApi()
        return api.device_query_retrieve(filter_id)

    def _get_filter_attributes(self, query, custom_attributes):
        # Ensure the query is of dict type
        if query and not isinstance(query, dict):
            raise ValueError("'query' parameter needs to be of type dict")

        # Add custom attributes, if provided
        if custom_attributes:
            if not isinstance(custom_attributes, dict):
                raise ValueError("Custom attributes when creating filter needs to be dict object")
            for k, v in custom_attributes.iteritems():
                if not k:
                    LOG.warning("Ignoring custom attribute with value %r as key is empty" % (v,))
                    continue
                query['custom_attributes__' + k] = v

        # Ensure query is valid
        if not query.keys():
            raise ValueError("'query' parameter not valid, needs to contain query keys")

        return self._urlify_query(query)

    def _urlify_query(self, query):
        # Quote strings using %20, not '+' which is default when urlencoding dicts
        for k, v in query.iteritems():
            if type(v) is str:
                query[k] = urllib.quote(v)

        # Encode the query string
        return urllib.urlencode(query)

    def _get_value_synchronized(self, consumer):
        # We return synchronously, so we block in a busy loop waiting for the
        # request to be done.
        while not consumer.is_done:
            time.sleep(0.1)

        # If we get an error we throw an exception to the user, which can then be handled
        # accordingly.
        if consumer.error:
            raise AsyncError(consumer.error)

        return consumer.value


class AsyncConsumer(object):
    """Consumer object for reading values from a long-polling thread.

    Example usage:

    .. code-block:: python

        async_resp = api.get_resource_value(endpoint, resource)
        while not async_resp.is_done:
            time.sleep(0.1)
        if async_resp.error:
            raise Exception("Async error: %r" % async_resp.error)
        print("Got value: %r" % (async_resp.value,))

    """

    def __init__(self, async_id, db):
        """Setup the consumer, listening for a specific async ID to appear in external DB.

        The DB is populated from the long polling thread.
        """
        self.async_id = async_id
        self.db = db

    @property
    def is_done(self):
        """Check if the DB has received an event with the specified async ID.

        :return: Whether the async request has finished or not
        :rtype: bool
        """
        return self.async_id in self.db

    @property
    def error(self):
        """Check if the async response is an error.

        Take care to call `is_done` before calling `error`. Note that the error
        messages are always encoded as strings.

        :raises UnhandledError: When not checking `is_done` first
        :return: the error value/payload, if found.
        :rtype: str
        """
        if not self.is_done:
            raise UnhandledError("Need to check if request is done, before checking for error")
        return self.db[self.async_id]["error"]

    @property
    def get_value(self):
        """Get the value of the finished async request.

        Take care to ensure the async request is indeed done, by checking both `is_done`
        and `error` before calling `value`.

        :raises UnhandledError: When not checking value of `error` or `is_done` first
        :return: the payload value
        :rtype: str
        """
        if not self.is_done:
            raise UnhandledError("Need to check if request is done, before getting value")
        if self.error:
            raise UnhandledError("Async request returned an error. Need to check for errors,"
                                 "before getting value.\nError: %s" % self.error)

        # Return the payload
        return self.db[self.async_id]["payload"]


class _LongPollingThread(threading.Thread):
    def __init__(self, db, queues, b64decode=True):
        super(_LongPollingThread, self).__init__()

        self.db = db
        self.queues = queues

        self._b64decode = b64decode
        self._stopped = False

    @catch_exceptions(MdsApiException)
    def run(self):
        while not self._stopped:
            api = self.mds.NotificationsApi()
            resp = api.v2_notification_pull_get()

            if resp.notifications:
                for n in resp.notifications:
                    # Ensure we have subscribed for the path we received a notification for
                    if n.ep not in self.queues and n.path not in self.queues[n.ep]:
                        LOG.warning(
                            "Ignoring notification on %s (%s) as no subscription is registered" %
                            (n.ep, n.path))

                    # Decode b64 encoded data
                    payload = base64.b64decode(n.payload) if self._b64decode else n.payload
                    self.queues[n.ep][n.path].put(payload)

            if resp.async_responses:
                for r in resp.async_responses:
                    # Check if we have a payload, and decode it if required
                    payload = r.payload if r.payload else None
                    should_b64 = self._b64decode and payload
                    payload = base64.b64decode(payload) if should_b64 else payload

                    self.db[r.id] = {
                        "payload": payload,
                        "error": r.error,
                        "status_code": r.status
                    }

    def stop(self):
        self._stopped = True


class DeviceDetail(DeviceDetailBackend):
    """Describes device object from the catalog."""

    def __init__(self, device_obj):
        """Override __init__ and allow passing in backend object."""
        super(DeviceDetail, self).__init__(**device_obj.to_dict())


class Filter(DeviceQueryDetail):
    """Describes device query object / filter."""

    def __init__(self, device_query_obj):
        """Override __init__ and allow passing in backend object."""
        super(Filter, self).__init__(**device_query_obj.to_dict())


