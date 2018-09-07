# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInvitationRespList(object):
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
        'after': 'str',
        'data': 'list[UserInvitationResp]',
        'has_more': 'bool',
        'limit': 'int',
        'object': 'str',
        'order': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'after': 'after',
        'data': 'data',
        'has_more': 'has_more',
        'limit': 'limit',
        'object': 'object',
        'order': 'order',
        'total_count': 'total_count'
    }

    def __init__(self, after=None, data=None, has_more=None, limit=None, object=None, order=None, total_count=None):
        """
        UserInvitationRespList - a model defined in Swagger
        """

        self._after = after
        self._data = data
        self._has_more = has_more
        self._limit = limit
        self._object = object
        self._order = order
        self._total_count = total_count
        self.discriminator = None

    @property
    def after(self):
        """
        Gets the after of this UserInvitationRespList.
        The entity ID to fetch after the given one.

        :return: The after of this UserInvitationRespList.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this UserInvitationRespList.
        The entity ID to fetch after the given one.

        :param after: The after of this UserInvitationRespList.
        :type: str
        """

        self._after = after

    @property
    def data(self):
        """
        Gets the data of this UserInvitationRespList.
        A list of entities.

        :return: The data of this UserInvitationRespList.
        :rtype: list[UserInvitationResp]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this UserInvitationRespList.
        A list of entities.

        :param data: The data of this UserInvitationRespList.
        :type: list[UserInvitationResp]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def has_more(self):
        """
        Gets the has_more of this UserInvitationRespList.
        Flag indicating whether there is more results.

        :return: The has_more of this UserInvitationRespList.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this UserInvitationRespList.
        Flag indicating whether there is more results.

        :param has_more: The has_more of this UserInvitationRespList.
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")

        self._has_more = has_more

    @property
    def limit(self):
        """
        Gets the limit of this UserInvitationRespList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :return: The limit of this UserInvitationRespList.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this UserInvitationRespList.
        The number of results to return, (range: 2-1000), or equals to `total_count`

        :param limit: The limit of this UserInvitationRespList.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def object(self):
        """
        Gets the object of this UserInvitationRespList.
        Entity name: always 'list'

        :return: The object of this UserInvitationRespList.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UserInvitationRespList.
        Entity name: always 'list'

        :param object: The object of this UserInvitationRespList.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["list"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def order(self):
        """
        Gets the order of this UserInvitationRespList.
        The order of the records to return based on creation time. Available values: ASC, DESC; by default ASC.

        :return: The order of this UserInvitationRespList.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this UserInvitationRespList.
        The order of the records to return based on creation time. Available values: ASC, DESC; by default ASC.

        :param order: The order of this UserInvitationRespList.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def total_count(self):
        """
        Gets the total_count of this UserInvitationRespList.
        The total number or records, if requested. It might be returned also for small lists.

        :return: The total_count of this UserInvitationRespList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this UserInvitationRespList.
        The total number or records, if requested. It might be returned also for small lists.

        :param total_count: The total_count of this UserInvitationRespList.
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count

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
        if not isinstance(other, UserInvitationRespList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other