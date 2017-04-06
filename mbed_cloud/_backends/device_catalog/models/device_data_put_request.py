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


class DeviceDataPutRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, endpoint_name=None, auto_update=None, object=None, custom_attributes=None, device_key=None, ca_id=None, name=None):
        """
        DeviceDataPutRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'endpoint_name': 'str',
            'auto_update': 'bool',
            'object': 'str',
            'custom_attributes': 'object',
            'device_key': 'str',
            'ca_id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'endpoint_name': 'endpoint_name',
            'auto_update': 'auto_update',
            'object': 'object',
            'custom_attributes': 'custom_attributes',
            'device_key': 'device_key',
            'ca_id': 'ca_id',
            'name': 'name'
        }

        self._description = description
        self._endpoint_name = endpoint_name
        self._auto_update = auto_update
        self._object = object
        self._custom_attributes = custom_attributes
        self._device_key = device_key
        self._ca_id = ca_id
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DeviceDataPutRequest.

        :return: The description of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceDataPutRequest.

        :param description: The description of this DeviceDataPutRequest.
        :type: str
        """

        self._description = description

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceDataPutRequest.

        :return: The endpoint_name of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceDataPutRequest.

        :param endpoint_name: The endpoint_name of this DeviceDataPutRequest.
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceDataPutRequest.

        :return: The auto_update of this DeviceDataPutRequest.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceDataPutRequest.

        :param auto_update: The auto_update of this DeviceDataPutRequest.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def object(self):
        """
        Gets the object of this DeviceDataPutRequest.

        :return: The object of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceDataPutRequest.

        :param object: The object of this DeviceDataPutRequest.
        :type: str
        """

        self._object = object

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceDataPutRequest.

        :return: The custom_attributes of this DeviceDataPutRequest.
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceDataPutRequest.

        :param custom_attributes: The custom_attributes of this DeviceDataPutRequest.
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceDataPutRequest.

        :return: The device_key of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceDataPutRequest.

        :param device_key: The device_key of this DeviceDataPutRequest.
        :type: str
        """
        if device_key is None:
            raise ValueError("Invalid value for `device_key`, must not be `None`")

        self._device_key = device_key

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceDataPutRequest.

        :return: The ca_id of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceDataPutRequest.

        :param ca_id: The ca_id of this DeviceDataPutRequest.
        :type: str
        """
        if ca_id is None:
            raise ValueError("Invalid value for `ca_id`, must not be `None`")

        self._ca_id = ca_id

    @property
    def name(self):
        """
        Gets the name of this DeviceDataPutRequest.

        :return: The name of this DeviceDataPutRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDataPutRequest.

        :param name: The name of this DeviceDataPutRequest.
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
        if not isinstance(other, DeviceDataPutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other