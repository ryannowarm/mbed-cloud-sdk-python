# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def deploy_info_get(self, **kwargs):
        """
        <p>Reads the deploy_info.json file and returns the Build and Git ID to the caller.</p> <p>Will return a 500 error if the file is missing, cannot be parsed or the keys are missing.</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.deploy_info_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.deploy_info_get_with_http_info(**kwargs)
        else:
            (data) = self.deploy_info_get_with_http_info(**kwargs)
            return data

    def deploy_info_get_with_http_info(self, **kwargs):
        """
        <p>Reads the deploy_info.json file and returns the Build and Git ID to the caller.</p> <p>Will return a 500 error if the file is missing, cannot be parsed or the keys are missing.</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.deploy_info_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deploy_info_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/v3/ds_deploy_info'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_create(self, body, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_create(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WriteUpdateCampaignSerializer body: Update campaign object to create (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_create_with_http_info(body, **kwargs)
        else:
            (data) = self.update_campaign_create_with_http_info(body, **kwargs)
            return data

    def update_campaign_create_with_http_info(self, body, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Create update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_create_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WriteUpdateCampaignSerializer body: Update campaign object to create (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_campaign_create`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_destroy(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_destroy(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_destroy_with_http_info(campaign_id, **kwargs)
        else:
            (data) = self.update_campaign_destroy_with_http_info(campaign_id, **kwargs)
            return data

    def update_campaign_destroy_with_http_info(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Delete update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_destroy_with_http_info(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_destroy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_destroy`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_list(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit:
        :param str order:
        :param str after:
        :param str filter:
        :param str include:
        :return: UpdateCampaignPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_list_with_http_info(**kwargs)
        else:
            (data) = self.update_campaign_list_with_http_info(**kwargs)
            return data

    def update_campaign_list_with_http_info(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>List all update campaigns</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit:
        :param str order:
        :param str after:
        :param str filter:
        :param str include:
        :return: UpdateCampaignPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'filter', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v3/update-campaigns/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'include' in params:
            query_params['include'] = params['include']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignPage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_partial_update(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_partial_update(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: DEPRECATED: The ID of the campaign
        :param str description: An optional description of the campaign
        :param str device_filter: The filter for the devices the campaign will target
        :param datetime finished: The timestamp when the update campaign finished
        :param str name: A name for this campaign
        :param str object: The API resource entity
        :param str root_manifest_id:
        :param str state: The state of the campaign
        :param datetime when: The timestamp at which update campaign scheduled to start
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_partial_update_with_http_info(**kwargs)
        else:
            (data) = self.update_campaign_partial_update_with_http_info(**kwargs)
            return data

    def update_campaign_partial_update_with_http_info(self, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign fields</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_partial_update_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: DEPRECATED: The ID of the campaign
        :param str description: An optional description of the campaign
        :param str device_filter: The filter for the devices the campaign will target
        :param datetime finished: The timestamp when the update campaign finished
        :param str name: A name for this campaign
        :param str object: The API resource entity
        :param str root_manifest_id:
        :param str state: The state of the campaign
        :param datetime when: The timestamp at which update campaign scheduled to start
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'description', 'device_filter', 'finished', 'name', 'object', 'root_manifest_id', 'state', 'when']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_partial_update" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'campaign_id' in params:
            form_params.append(('campaign_id', params['campaign_id']))
        if 'description' in params:
            form_params.append(('description', params['description']))
        if 'device_filter' in params:
            form_params.append(('device_filter', params['device_filter']))
        if 'finished' in params:
            form_params.append(('finished', params['finished']))
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'object' in params:
            form_params.append(('object', params['object']))
        if 'root_manifest_id' in params:
            form_params.append(('root_manifest_id', params['root_manifest_id']))
        if 'state' in params:
            form_params.append(('state', params['state']))
        if 'when' in params:
            form_params.append(('when', params['when']))

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_retrieve(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_retrieve(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_retrieve_with_http_info(campaign_id, **kwargs)
        else:
            (data) = self.update_campaign_retrieve_with_http_info(campaign_id, **kwargs)
            return data

    def update_campaign_retrieve_with_http_info(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Retrieve campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_retrieve_with_http_info(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the campaign (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_retrieve`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_status(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Show the status of an update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_status(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaignStatusSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_status_with_http_info(campaign_id, **kwargs)
        else:
            (data) = self.update_campaign_status_with_http_info(campaign_id, **kwargs)
            return data

    def update_campaign_status_with_http_info(self, campaign_id, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Show the status of an update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_status_with_http_info(campaign_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: The ID of the update campaign (required)
        :return: UpdateCampaignStatusSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_status`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/status/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignStatusSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_campaign_update(self, campaign_id, body, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_update(campaign_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID to update (required)
        :param WriteUpdateCampaignSerializer body: Update campaign object to create (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_campaign_update_with_http_info(campaign_id, body, **kwargs)
        else:
            (data) = self.update_campaign_update_with_http_info(campaign_id, body, **kwargs)
            return data

    def update_campaign_update_with_http_info(self, campaign_id, body, **kwargs):
        """
        <p>The APIs for creating and manipulating update campaigns. Update campaigns are used to control firmware update to a list of devices specified by a filter.  </p> <p>Update campaign</p>
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_campaign_update_with_http_info(campaign_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str campaign_id: Campaign ID to update (required)
        :param WriteUpdateCampaignSerializer body: Update campaign object to create (required)
        :return: UpdateCampaignSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_campaign_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params) or (params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `update_campaign_update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_campaign_update`")


        collection_formats = {}

        resource_path = '/v3/update-campaigns/{campaign_id}/'.replace('{format}', 'json')
        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateCampaignSerializer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)