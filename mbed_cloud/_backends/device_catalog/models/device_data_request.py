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


class DeviceDataRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, manifest_timestamp=None, vendor_id=None, description=None, deployed_state=None, firmware_checksum=None, auto_update=None, mechanism=None, device_class=None, trust_level=None, custom_attributes=None, manifest=None, trust_class=None, device_key=None, state=None, attestation_method=None, ca_id=None, deployment=None, mechanism_url=None, serial_number=None, endpoint_name=None, name=None):
        """
        DeviceDataRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'manifest_timestamp': 'datetime',
            'vendor_id': 'str',
            'description': 'str',
            'deployed_state': 'str',
            'firmware_checksum': 'str',
            'auto_update': 'bool',
            'mechanism': 'str',
            'device_class': 'str',
            'trust_level': 'int',
            'custom_attributes': 'object',
            'manifest': 'str',
            'trust_class': 'int',
            'device_key': 'str',
            'state': 'str',
            'attestation_method': 'int',
            'ca_id': 'str',
            'deployment': 'str',
            'mechanism_url': 'str',
            'serial_number': 'str',
            'endpoint_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'manifest_timestamp': 'manifest_timestamp',
            'vendor_id': 'vendor_id',
            'description': 'description',
            'deployed_state': 'deployed_state',
            'firmware_checksum': 'firmware_checksum',
            'auto_update': 'auto_update',
            'mechanism': 'mechanism',
            'device_class': 'device_class',
            'trust_level': 'trust_level',
            'custom_attributes': 'custom_attributes',
            'manifest': 'manifest',
            'trust_class': 'trust_class',
            'device_key': 'device_key',
            'state': 'state',
            'attestation_method': 'attestation_method',
            'ca_id': 'ca_id',
            'deployment': 'deployment',
            'mechanism_url': 'mechanism_url',
            'serial_number': 'serial_number',
            'endpoint_name': 'endpoint_name',
            'name': 'name'
        }

        self._manifest_timestamp = manifest_timestamp
        self._vendor_id = vendor_id
        self._description = description
        self._deployed_state = deployed_state
        self._firmware_checksum = firmware_checksum
        self._auto_update = auto_update
        self._mechanism = mechanism
        self._device_class = device_class
        self._trust_level = trust_level
        self._custom_attributes = custom_attributes
        self._manifest = manifest
        self._trust_class = trust_class
        self._device_key = device_key
        self._state = state
        self._attestation_method = attestation_method
        self._ca_id = ca_id
        self._deployment = deployment
        self._mechanism_url = mechanism_url
        self._serial_number = serial_number
        self._endpoint_name = endpoint_name
        self._name = name

    @property
    def manifest_timestamp(self):
        """
        Gets the manifest_timestamp of this DeviceDataRequest.

        :return: The manifest_timestamp of this DeviceDataRequest.
        :rtype: datetime
        """
        return self._manifest_timestamp

    @manifest_timestamp.setter
    def manifest_timestamp(self, manifest_timestamp):
        """
        Sets the manifest_timestamp of this DeviceDataRequest.

        :param manifest_timestamp: The manifest_timestamp of this DeviceDataRequest.
        :type: datetime
        """

        self._manifest_timestamp = manifest_timestamp

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DeviceDataRequest.

        :return: The vendor_id of this DeviceDataRequest.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DeviceDataRequest.

        :param vendor_id: The vendor_id of this DeviceDataRequest.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def description(self):
        """
        Gets the description of this DeviceDataRequest.

        :return: The description of this DeviceDataRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceDataRequest.

        :param description: The description of this DeviceDataRequest.
        :type: str
        """

        self._description = description

    @property
    def deployed_state(self):
        """
        Gets the deployed_state of this DeviceDataRequest.

        :return: The deployed_state of this DeviceDataRequest.
        :rtype: str
        """
        return self._deployed_state

    @deployed_state.setter
    def deployed_state(self, deployed_state):
        """
        Sets the deployed_state of this DeviceDataRequest.

        :param deployed_state: The deployed_state of this DeviceDataRequest.
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
    def firmware_checksum(self):
        """
        Gets the firmware_checksum of this DeviceDataRequest.

        :return: The firmware_checksum of this DeviceDataRequest.
        :rtype: str
        """
        return self._firmware_checksum

    @firmware_checksum.setter
    def firmware_checksum(self, firmware_checksum):
        """
        Sets the firmware_checksum of this DeviceDataRequest.

        :param firmware_checksum: The firmware_checksum of this DeviceDataRequest.
        :type: str
        """

        self._firmware_checksum = firmware_checksum

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceDataRequest.

        :return: The auto_update of this DeviceDataRequest.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceDataRequest.

        :param auto_update: The auto_update of this DeviceDataRequest.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def mechanism(self):
        """
        Gets the mechanism of this DeviceDataRequest.

        :return: The mechanism of this DeviceDataRequest.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this DeviceDataRequest.

        :param mechanism: The mechanism of this DeviceDataRequest.
        :type: str
        """

        self._mechanism = mechanism

    @property
    def device_class(self):
        """
        Gets the device_class of this DeviceDataRequest.

        :return: The device_class of this DeviceDataRequest.
        :rtype: str
        """
        return self._device_class

    @device_class.setter
    def device_class(self, device_class):
        """
        Sets the device_class of this DeviceDataRequest.

        :param device_class: The device_class of this DeviceDataRequest.
        :type: str
        """

        self._device_class = device_class

    @property
    def trust_level(self):
        """
        Gets the trust_level of this DeviceDataRequest.

        :return: The trust_level of this DeviceDataRequest.
        :rtype: int
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """
        Sets the trust_level of this DeviceDataRequest.

        :param trust_level: The trust_level of this DeviceDataRequest.
        :type: int
        """

        self._trust_level = trust_level

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceDataRequest.

        :return: The custom_attributes of this DeviceDataRequest.
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceDataRequest.

        :param custom_attributes: The custom_attributes of this DeviceDataRequest.
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def manifest(self):
        """
        Gets the manifest of this DeviceDataRequest.

        :return: The manifest of this DeviceDataRequest.
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this DeviceDataRequest.

        :param manifest: The manifest of this DeviceDataRequest.
        :type: str
        """

        self._manifest = manifest

    @property
    def trust_class(self):
        """
        Gets the trust_class of this DeviceDataRequest.

        :return: The trust_class of this DeviceDataRequest.
        :rtype: int
        """
        return self._trust_class

    @trust_class.setter
    def trust_class(self, trust_class):
        """
        Sets the trust_class of this DeviceDataRequest.

        :param trust_class: The trust_class of this DeviceDataRequest.
        :type: int
        """

        self._trust_class = trust_class

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceDataRequest.

        :return: The device_key of this DeviceDataRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceDataRequest.

        :param device_key: The device_key of this DeviceDataRequest.
        :type: str
        """

        self._device_key = device_key

    @property
    def state(self):
        """
        Gets the state of this DeviceDataRequest.

        :return: The state of this DeviceDataRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DeviceDataRequest.

        :param state: The state of this DeviceDataRequest.
        :type: str
        """

        self._state = state

    @property
    def attestation_method(self):
        """
        Gets the attestation_method of this DeviceDataRequest.

        :return: The attestation_method of this DeviceDataRequest.
        :rtype: int
        """
        return self._attestation_method

    @attestation_method.setter
    def attestation_method(self, attestation_method):
        """
        Sets the attestation_method of this DeviceDataRequest.

        :param attestation_method: The attestation_method of this DeviceDataRequest.
        :type: int
        """

        self._attestation_method = attestation_method

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceDataRequest.

        :return: The ca_id of this DeviceDataRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceDataRequest.

        :param ca_id: The ca_id of this DeviceDataRequest.
        :type: str
        """

        self._ca_id = ca_id

    @property
    def deployment(self):
        """
        Gets the deployment of this DeviceDataRequest.

        :return: The deployment of this DeviceDataRequest.
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeviceDataRequest.

        :param deployment: The deployment of this DeviceDataRequest.
        :type: str
        """

        self._deployment = deployment

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this DeviceDataRequest.

        :return: The mechanism_url of this DeviceDataRequest.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this DeviceDataRequest.

        :param mechanism_url: The mechanism_url of this DeviceDataRequest.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceDataRequest.

        :return: The serial_number of this DeviceDataRequest.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceDataRequest.

        :param serial_number: The serial_number of this DeviceDataRequest.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceDataRequest.

        :return: The endpoint_name of this DeviceDataRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceDataRequest.

        :param endpoint_name: The endpoint_name of this DeviceDataRequest.
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def name(self):
        """
        Gets the name of this DeviceDataRequest.

        :return: The name of this DeviceDataRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDataRequest.

        :param name: The name of this DeviceDataRequest.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, DeviceDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
