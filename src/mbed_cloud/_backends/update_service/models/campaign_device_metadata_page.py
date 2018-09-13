# coding: utf-8

"""
    Update Service API

    This is the API documentation for the Device Management deployment service, which is part of the Update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CampaignDeviceMetadataPage(object):
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
        'data': 'list[CampaignDeviceMetadata]',
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
        CampaignDeviceMetadataPage - a model defined in Swagger
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
        Gets the after of this CampaignDeviceMetadataPage.
        The entity ID to fetch after the given one

        :return: The after of this CampaignDeviceMetadataPage.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this CampaignDeviceMetadataPage.
        The entity ID to fetch after the given one

        :param after: The after of this CampaignDeviceMetadataPage.
        :type: str
        """

        self._after = after

    @property
    def data(self):
        """
        Gets the data of this CampaignDeviceMetadataPage.
        A list of entities

        :return: The data of this CampaignDeviceMetadataPage.
        :rtype: list[CampaignDeviceMetadata]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this CampaignDeviceMetadataPage.
        A list of entities

        :param data: The data of this CampaignDeviceMetadataPage.
        :type: list[CampaignDeviceMetadata]
        """

        self._data = data

    @property
    def has_more(self):
        """
        Gets the has_more of this CampaignDeviceMetadataPage.
        A flag indicating whether there are more results

        :return: The has_more of this CampaignDeviceMetadataPage.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this CampaignDeviceMetadataPage.
        A flag indicating whether there are more results

        :param has_more: The has_more of this CampaignDeviceMetadataPage.
        :type: bool
        """

        self._has_more = has_more

    @property
    def limit(self):
        """
        Gets the limit of this CampaignDeviceMetadataPage.
        The number of results to return, (range: 2-1000), or equals to total_count

        :return: The limit of this CampaignDeviceMetadataPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CampaignDeviceMetadataPage.
        The number of results to return, (range: 2-1000), or equals to total_count

        :param limit: The limit of this CampaignDeviceMetadataPage.
        :type: int
        """

        self._limit = limit

    @property
    def object(self):
        """
        Gets the object of this CampaignDeviceMetadataPage.
        The entity name: always 'list'

        :return: The object of this CampaignDeviceMetadataPage.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CampaignDeviceMetadataPage.
        The entity name: always 'list'

        :param object: The object of this CampaignDeviceMetadataPage.
        :type: str
        """

        self._object = object

    @property
    def order(self):
        """
        Gets the order of this CampaignDeviceMetadataPage.
        The order of the records to return. Acceptable values: ASC, DESC. Default: ASC

        :return: The order of this CampaignDeviceMetadataPage.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this CampaignDeviceMetadataPage.
        The order of the records to return. Acceptable values: ASC, DESC. Default: ASC

        :param order: The order of this CampaignDeviceMetadataPage.
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
        Gets the total_count of this CampaignDeviceMetadataPage.
        The total number or records, if requested. It may be returned also for small lists.

        :return: The total_count of this CampaignDeviceMetadataPage.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this CampaignDeviceMetadataPage.
        The total number or records, if requested. It may be returned also for small lists.

        :param total_count: The total_count of this CampaignDeviceMetadataPage.
        :type: int
        """

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
        if not isinstance(other, CampaignDeviceMetadataPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
