# coding: utf-8

"""
    Device Catalog API

    This is the API Documentation for the mbed device catalog update service.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bootstrap_expiration_date=None, bootstrapped_timestamp=None, connector_expiration_date=None, updated_at=None, mechanism=None, device_class=None, id=None, description=None, endpoint_name=None, auto_update=None, device_execution_mode=None, custom_attributes=None, state=None, etag=None, serial_number=None, firmware_checksum=None, manifest_timestamp=None, vendor_id=None, account_id=None, deployed_state=None, object=None, trust_class=None, deployment=None, mechanism_url=None, trust_level=None, name=None, device_key=None, created_at=None, manifest=None, ca_id=None):
        """
        DeviceData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bootstrap_expiration_date': 'datetime',
            'bootstrapped_timestamp': 'datetime',
            'connector_expiration_date': 'datetime',
            'updated_at': 'datetime',
            'mechanism': 'str',
            'device_class': 'str',
            'id': 'str',
            'description': 'str',
            'endpoint_name': 'str',
            'auto_update': 'bool',
            'device_execution_mode': 'int',
            'custom_attributes': 'object',
            'state': 'str',
            'etag': 'datetime',
            'serial_number': 'str',
            'firmware_checksum': 'str',
            'manifest_timestamp': 'datetime',
            'vendor_id': 'str',
            'account_id': 'str',
            'deployed_state': 'str',
            'object': 'str',
            'trust_class': 'int',
            'deployment': 'str',
            'mechanism_url': 'str',
            'trust_level': 'int',
            'name': 'str',
            'device_key': 'str',
            'created_at': 'datetime',
            'manifest': 'str',
            'ca_id': 'str'
        }

        self.attribute_map = {
            'bootstrap_expiration_date': 'bootstrap_expiration_date',
            'bootstrapped_timestamp': 'bootstrapped_timestamp',
            'connector_expiration_date': 'connector_expiration_date',
            'updated_at': 'updated_at',
            'mechanism': 'mechanism',
            'device_class': 'device_class',
            'id': 'id',
            'description': 'description',
            'endpoint_name': 'endpoint_name',
            'auto_update': 'auto_update',
            'device_execution_mode': 'device_execution_mode',
            'custom_attributes': 'custom_attributes',
            'state': 'state',
            'etag': 'etag',
            'serial_number': 'serial_number',
            'firmware_checksum': 'firmware_checksum',
            'manifest_timestamp': 'manifest_timestamp',
            'vendor_id': 'vendor_id',
            'account_id': 'account_id',
            'deployed_state': 'deployed_state',
            'object': 'object',
            'trust_class': 'trust_class',
            'deployment': 'deployment',
            'mechanism_url': 'mechanism_url',
            'trust_level': 'trust_level',
            'name': 'name',
            'device_key': 'device_key',
            'created_at': 'created_at',
            'manifest': 'manifest',
            'ca_id': 'ca_id'
        }

        self._bootstrap_expiration_date = bootstrap_expiration_date
        self._bootstrapped_timestamp = bootstrapped_timestamp
        self._connector_expiration_date = connector_expiration_date
        self._updated_at = updated_at
        self._mechanism = mechanism
        self._device_class = device_class
        self._id = id
        self._description = description
        self._endpoint_name = endpoint_name
        self._auto_update = auto_update
        self._device_execution_mode = device_execution_mode
        self._custom_attributes = custom_attributes
        self._state = state
        self._etag = etag
        self._serial_number = serial_number
        self._firmware_checksum = firmware_checksum
        self._manifest_timestamp = manifest_timestamp
        self._vendor_id = vendor_id
        self._account_id = account_id
        self._deployed_state = deployed_state
        self._object = object
        self._trust_class = trust_class
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._trust_level = trust_level
        self._name = name
        self._device_key = device_key
        self._created_at = created_at
        self._manifest = manifest
        self._ca_id = ca_id

    @property
    def bootstrap_expiration_date(self):
        """
        Gets the bootstrap_expiration_date of this DeviceData.

        :return: The bootstrap_expiration_date of this DeviceData.
        :rtype: datetime
        """
        return self._bootstrap_expiration_date

    @bootstrap_expiration_date.setter
    def bootstrap_expiration_date(self, bootstrap_expiration_date):
        """
        Sets the bootstrap_expiration_date of this DeviceData.

        :param bootstrap_expiration_date: The bootstrap_expiration_date of this DeviceData.
        :type: datetime
        """

        self._bootstrap_expiration_date = bootstrap_expiration_date

    @property
    def bootstrapped_timestamp(self):
        """
        Gets the bootstrapped_timestamp of this DeviceData.

        :return: The bootstrapped_timestamp of this DeviceData.
        :rtype: datetime
        """
        return self._bootstrapped_timestamp

    @bootstrapped_timestamp.setter
    def bootstrapped_timestamp(self, bootstrapped_timestamp):
        """
        Sets the bootstrapped_timestamp of this DeviceData.

        :param bootstrapped_timestamp: The bootstrapped_timestamp of this DeviceData.
        :type: datetime
        """

        self._bootstrapped_timestamp = bootstrapped_timestamp

    @property
    def connector_expiration_date(self):
        """
        Gets the connector_expiration_date of this DeviceData.

        :return: The connector_expiration_date of this DeviceData.
        :rtype: datetime
        """
        return self._connector_expiration_date

    @connector_expiration_date.setter
    def connector_expiration_date(self, connector_expiration_date):
        """
        Sets the connector_expiration_date of this DeviceData.

        :param connector_expiration_date: The connector_expiration_date of this DeviceData.
        :type: datetime
        """

        self._connector_expiration_date = connector_expiration_date

    @property
    def updated_at(self):
        """
        Gets the updated_at of this DeviceData.

        :return: The updated_at of this DeviceData.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this DeviceData.

        :param updated_at: The updated_at of this DeviceData.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceData.

        :return: The mechanism of this DeviceData.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceData.

        :param mechanism: The mechanism of this DeviceData.
        :type: str
        """

        self._mechanism = mechanism

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceData.

        :return: The device_class of this DeviceData.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceData.

        :param device_class: The device_class of this DeviceData.
        :type: str
        """

        self._device_class = device_class

    @property
    def id(self):
        """
        Gets the id of this DeviceData.

        :return: The id of this DeviceData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceData.

        :param id: The id of this DeviceData.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeviceData.

        :return: The description of this DeviceData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceData.

        :param description: The description of this DeviceData.
        :type: str
        """

        self._description = description

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceData.

        :return: The endpoint_name of this DeviceData.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceData.

        :param endpoint_name: The endpoint_name of this DeviceData.
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceData.

        :return: The auto_update of this DeviceData.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceData.

        :param auto_update: The auto_update of this DeviceData.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def device_execution_mode(self):
        """
        Gets the device_execution_mode of this DeviceData.

        :return: The device_execution_mode of this DeviceData.
        :rtype: int
        """
        return self._device_execution_mode

    @device_execution_mode.setter
    def device_execution_mode(self, device_execution_mode):
        """
        Sets the device_execution_mode of this DeviceData.

        :param device_execution_mode: The device_execution_mode of this DeviceData.
        :type: int
        """

        self._device_execution_mode = device_execution_mode

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceData.

        :return: The custom_attributes of this DeviceData.
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceData.

        :param custom_attributes: The custom_attributes of this DeviceData.
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def state(self):
        """
        Gets the state of this DeviceData.

        :return: The state of this DeviceData.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceData.

        :param state: The state of this DeviceData.
        :type: str
        """

        self._state = state

    @property
    def etag(self):
        """
        Gets the etag of this DeviceData.

        :return: The etag of this DeviceData.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeviceData.

        :param etag: The etag of this DeviceData.
        :type: datetime
        """

        self._etag = etag

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceData.

        :return: The serial_number of this DeviceData.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceData.

        :param serial_number: The serial_number of this DeviceData.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def firmware_checksum(self):
        """
        Gets the firmware_checksum of this DeviceData.

        :return: The firmware_checksum of this DeviceData.
        :rtype: str
        """
        return self._firmware_checksum

    @firmware_checksum.setter
    def firmware_checksum(self, firmware_checksum):
        """
        Sets the firmware_checksum of this DeviceData.

        :param firmware_checksum: The firmware_checksum of this DeviceData.
        :type: str
        """

        self._firmware_checksum = firmware_checksum

    @property
    def manifest_timestamp(self):
        """
        Gets the manifest_timestamp of this DeviceData.

        :return: The manifest_timestamp of this DeviceData.
        :rtype: datetime
        """
        return self._manifest_timestamp

    @manifest_timestamp.setter
    def manifest_timestamp(self, manifest_timestamp):
        """
        Sets the manifest_timestamp of this DeviceData.

        :param manifest_timestamp: The manifest_timestamp of this DeviceData.
        :type: datetime
        """

        self._manifest_timestamp = manifest_timestamp

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceData.

        :return: The vendor_id of this DeviceData.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceData.

        :param vendor_id: The vendor_id of this DeviceData.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def account_id(self):
        """
        Gets the account_id of this DeviceData.

        :return: The account_id of this DeviceData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this DeviceData.

        :param account_id: The account_id of this DeviceData.
        :type: str
        """

        self._account_id = account_id

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceData.

        :return: The deployed_state of this DeviceData.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceData.

        :param deployed_state: The deployed_state of this DeviceData.
        :type: str
        """
        allowed_values = ["development", "production"]
        if deployed_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployed_state` ({0}), must be one of {1}"
                .format(deployed_state, allowed_values)
            )

        self._deployed_state = deployed_state

    @property
    def object(self):
        """
        Gets the object of this DeviceData.

        :return: The object of this DeviceData.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceData.

        :param object: The object of this DeviceData.
        :type: str
        """

        self._object = object

    @property
    def trust_class(self):
        """
        Gets the trust_class of this DeviceData.

        :return: The trust_class of this DeviceData.
        :rtype: int
        """
        return self._trust_class

    @trust_class.setter
    def trust_class(self, trust_class):
        """
        Sets the trust_class of this DeviceData.

        :param trust_class: The trust_class of this DeviceData.
        :type: int
        """

        self._trust_class = trust_class

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceData.

        :return: The deployment of this DeviceData.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceData.

        :param deployment: The deployment of this DeviceData.
        :type: str
        """

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceData.

        :return: The mechanism_url of this DeviceData.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceData.

        :param mechanism_url: The mechanism_url of this DeviceData.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def trust_level(self):
        """
        Gets the trust_level of this DeviceData.

        :return: The trust_level of this DeviceData.
        :rtype: int
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """
        Sets the trust_level of this DeviceData.

        :param trust_level: The trust_level of this DeviceData.
        :type: int
        """

        self._trust_level = trust_level

    @property
    def name(self):
        """
        Gets the name of this DeviceData.

        :return: The name of this DeviceData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceData.

        :param name: The name of this DeviceData.
        :type: str
        """

        self._name = name

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceData.

        :return: The device_key of this DeviceData.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceData.

        :param device_key: The device_key of this DeviceData.
        :type: str
        """

        self._device_key = device_key

    @property
    def created_at(self):
        """
        Gets the created_at of this DeviceData.

        :return: The created_at of this DeviceData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeviceData.

        :param created_at: The created_at of this DeviceData.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceData.

        :return: The manifest of this DeviceData.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceData.

        :param manifest: The manifest of this DeviceData.
        :type: str
        """

        self._manifest = manifest

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceData.

        :return: The ca_id of this DeviceData.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceData.

        :param ca_id: The ca_id of this DeviceData.
        :type: str
        """

        self._ca_id = ca_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DeviceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
