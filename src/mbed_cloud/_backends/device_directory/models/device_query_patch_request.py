# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Device Directory service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceQueryPatchRequest(object):
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
        'name': 'str',
        'query': 'str'
    }

    attribute_map = {
        'name': 'name',
        'query': 'query'
    }

    def __init__(self, name=None, query=None):
        """
        DeviceQueryPatchRequest - a model defined in Swagger
        """

        self._name = name
        self._query = query
        self.discriminator = None

    @property
    def name(self):
        """
        Gets the name of this DeviceQueryPatchRequest.
        The name of the query.

        :return: The name of this DeviceQueryPatchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceQueryPatchRequest.
        The name of the query.

        :param name: The name of this DeviceQueryPatchRequest.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")

        self._name = name

    @property
    def query(self):
        """
        Gets the query of this DeviceQueryPatchRequest.
        The device query.

        :return: The query of this DeviceQueryPatchRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this DeviceQueryPatchRequest.
        The device query.

        :param query: The query of this DeviceQueryPatchRequest.
        :type: str
        """
        if query is not None and len(query) > 1000:
            raise ValueError("Invalid value for `query`, length must be less than or equal to `1000`")

        self._query = query

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
        if not isinstance(other, DeviceQueryPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
