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


class DeviceQuery(object):
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
        'created_at': 'datetime',
        'object': 'str',
        'updated_at': 'datetime',
        'etag': 'datetime',
        'query': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'object': 'object',
        'updated_at': 'updated_at',
        'etag': 'etag',
        'query': 'query',
        'id': 'id'
    }

    def __init__(self, name=None, created_at=None, object=None, updated_at=None, etag=None, query=None, id=None):
        """
        DeviceQuery - a model defined in Swagger
        """

        self._name = name
        self._created_at = created_at
        self._object = object
        self._updated_at = updated_at
        self._etag = etag
        self._query = query
        self._id = id
        self.discriminator = None

    @property
    def name(self):
        """
        Gets the name of this DeviceQuery.
        The name of the query.

        :return: The name of this DeviceQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceQuery.
        The name of the query.

        :param name: The name of this DeviceQuery.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this DeviceQuery.
        The timestamp of when the device was created in the device directory.

        :return: The created_at of this DeviceQuery.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DeviceQuery.
        The timestamp of when the device was created in the device directory.

        :param created_at: The created_at of this DeviceQuery.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this DeviceQuery.
        The API resource entity.

        :return: The object of this DeviceQuery.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceQuery.
        The API resource entity.

        :param object: The object of this DeviceQuery.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this DeviceQuery.
        The time the object was updated.

        :return: The updated_at of this DeviceQuery.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this DeviceQuery.
        The time the object was updated.

        :param updated_at: The updated_at of this DeviceQuery.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def etag(self):
        """
        Gets the etag of this DeviceQuery.
        The entity instance signature.

        :return: The etag of this DeviceQuery.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this DeviceQuery.
        The entity instance signature.

        :param etag: The etag of this DeviceQuery.
        :type: datetime
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def query(self):
        """
        Gets the query of this DeviceQuery.
        The device query.

        :return: The query of this DeviceQuery.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this DeviceQuery.
        The device query.

        :param query: The query of this DeviceQuery.
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")

        self._query = query

    @property
    def id(self):
        """
        Gets the id of this DeviceQuery.
        The ID of the query.

        :return: The id of this DeviceQuery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceQuery.
        The ID of the query.

        :param id: The id of this DeviceQuery.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

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
        if not isinstance(other, DeviceQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
