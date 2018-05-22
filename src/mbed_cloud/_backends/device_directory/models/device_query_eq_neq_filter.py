# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the Mbed Device Directory service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceQueryEqNeqFilter(object):
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
        'created_at': 'datetime',
        'etag': 'datetime',
        'id': 'str',
        'name': 'str',
        'query': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'created_at',
        'etag': 'etag',
        'id': 'id',
        'name': 'name',
        'query': 'query',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, etag=None, id=None, name=None, query=None, updated_at=None):
        """
        DeviceQueryEqNeqFilter - a model defined in Swagger
        """

        self._created_at = created_at
        self._etag = etag
        self._id = id
        self._name = name
        self._query = query
        self._updated_at = updated_at
        self.discriminator = None

    @property
    def created_at(self):
        """
        Gets the created_at of this DeviceQueryEqNeqFilter.

        :return: The created_at of this DeviceQueryEqNeqFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeviceQueryEqNeqFilter.

        :param created_at: The created_at of this DeviceQueryEqNeqFilter.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def etag(self):
        """
        Gets the etag of this DeviceQueryEqNeqFilter.

        :return: The etag of this DeviceQueryEqNeqFilter.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeviceQueryEqNeqFilter.

        :param etag: The etag of this DeviceQueryEqNeqFilter.
        :type: datetime
        """

        self._etag = etag

    @property
    def id(self):
        """
        Gets the id of this DeviceQueryEqNeqFilter.

        :return: The id of this DeviceQueryEqNeqFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceQueryEqNeqFilter.

        :param id: The id of this DeviceQueryEqNeqFilter.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DeviceQueryEqNeqFilter.

        :return: The name of this DeviceQueryEqNeqFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceQueryEqNeqFilter.

        :param name: The name of this DeviceQueryEqNeqFilter.
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """
        Gets the query of this DeviceQueryEqNeqFilter.

        :return: The query of this DeviceQueryEqNeqFilter.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this DeviceQueryEqNeqFilter.

        :param query: The query of this DeviceQueryEqNeqFilter.
        :type: str
        """

        self._query = query

    @property
    def updated_at(self):
        """
        Gets the updated_at of this DeviceQueryEqNeqFilter.

        :return: The updated_at of this DeviceQueryEqNeqFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this DeviceQueryEqNeqFilter.

        :param updated_at: The updated_at of this DeviceQueryEqNeqFilter.
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, DeviceQueryEqNeqFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
