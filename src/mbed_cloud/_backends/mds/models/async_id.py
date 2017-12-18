# coding: utf-8

"""
    Connect API

    Mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AsyncID(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'async_response_id': 'str'
    }

    attribute_map = {
        'async_response_id': 'async-response-id'
    }

    def __init__(self, async_response_id=None):
        """
        AsyncID - a model defined in Swagger
        """

        self._async_response_id = async_response_id
        self.discriminator = None

    @property
    def async_response_id(self):
        """
        Gets the async_response_id of this AsyncID.
        Asynchronous response unique ID.

        :return: The async_response_id of this AsyncID.
        :rtype: str
        """
        return self._async_response_id

    @async_response_id.setter
    def async_response_id(self, async_response_id):
        """
        Sets the async_response_id of this AsyncID.
        Asynchronous response unique ID.

        :param async_response_id: The async_response_id of this AsyncID.
        :type: str
        """

        self._async_response_id = async_response_id

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
        if not isinstance(other, AsyncID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other