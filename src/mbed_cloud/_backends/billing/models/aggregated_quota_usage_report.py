# coding: utf-8

"""
    Billing API

    Billing API allows users to retrieve billing reports and service package details.

    OpenAPI spec version: 1.4.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AggregatedQuotaUsageReport(object):
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
        'account_id': 'str',
        'amount': 'int',
        'campaign_name': 'str',
        'time': 'datetime',
        'type': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'amount': 'amount',
        'campaign_name': 'campaign_name',
        'time': 'time',
        'type': 'type'
    }

    def __init__(self, account_id=None, amount=None, campaign_name=None, time=None, type=None):
        """
        AggregatedQuotaUsageReport - a model defined in Swagger
        """

        self._account_id = account_id
        self._amount = amount
        self._campaign_name = campaign_name
        self._time = time
        self._type = type
        self.discriminator = None

    @property
    def account_id(self):
        """
        Gets the account_id of this AggregatedQuotaUsageReport.

        :return: The account_id of this AggregatedQuotaUsageReport.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this AggregatedQuotaUsageReport.

        :param account_id: The account_id of this AggregatedQuotaUsageReport.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def amount(self):
        """
        Gets the amount of this AggregatedQuotaUsageReport.
        Amount of quota usage entry. Negative if it is quota consumption.

        :return: The amount of this AggregatedQuotaUsageReport.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this AggregatedQuotaUsageReport.
        Amount of quota usage entry. Negative if it is quota consumption.

        :param amount: The amount of this AggregatedQuotaUsageReport.
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def campaign_name(self):
        """
        Gets the campaign_name of this AggregatedQuotaUsageReport.
        Campaign name of quota usage entry. Null if quota usage entry type is not reservation or reservation release.

        :return: The campaign_name of this AggregatedQuotaUsageReport.
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """
        Sets the campaign_name of this AggregatedQuotaUsageReport.
        Campaign name of quota usage entry. Null if quota usage entry type is not reservation or reservation release.

        :param campaign_name: The campaign_name of this AggregatedQuotaUsageReport.
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def time(self):
        """
        Gets the time of this AggregatedQuotaUsageReport.
        Added time of quota usage entry in RFC3339 date-time with millisecond accuracy and UTC time zone.

        :return: The time of this AggregatedQuotaUsageReport.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this AggregatedQuotaUsageReport.
        Added time of quota usage entry in RFC3339 date-time with millisecond accuracy and UTC time zone.

        :param time: The time of this AggregatedQuotaUsageReport.
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def type(self):
        """
        Gets the type of this AggregatedQuotaUsageReport.
        Type of quota usage entry.

        :return: The type of this AggregatedQuotaUsageReport.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AggregatedQuotaUsageReport.
        Type of quota usage entry.

        :param type: The type of this AggregatedQuotaUsageReport.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["reservation", "reservation_release", "reservation_termination", "package_renewal", "package_creation", "package_termination"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, AggregatedQuotaUsageReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
