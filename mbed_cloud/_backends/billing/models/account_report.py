# coding: utf-8

"""
    mbed-billing REST API documentation for API-server

    This document contains the public REST API definitions of the mbed-billing service's API server component.

    OpenAPI spec version: 1.3.4-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billing_data=None, account=None, children=None, aggregated=None):
        """
        AccountReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'billing_data': 'BillingData',
            'account': 'Account',
            'children': 'list[ChildAccountReport]',
            'aggregated': 'BillingData'
        }

        self.attribute_map = {
            'billing_data': 'billing_data',
            'account': 'account',
            'children': 'children',
            'aggregated': 'aggregated'
        }

        self._billing_data = billing_data
        self._account = account
        self._children = children
        self._aggregated = aggregated

    @property
    def billing_data(self):
        """
        Gets the billing_data of this AccountReport.

        :return: The billing_data of this AccountReport.
        :rtype: BillingData
        """
        return self._billing_data

    @billing_data.setter
    def billing_data(self, billing_data):
        """
        Sets the billing_data of this AccountReport.

        :param billing_data: The billing_data of this AccountReport.
        :type: BillingData
        """
        if billing_data is None:
            raise ValueError("Invalid value for `billing_data`, must not be `None`")

        self._billing_data = billing_data

    @property
    def account(self):
        """
        Gets the account of this AccountReport.

        :return: The account of this AccountReport.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this AccountReport.

        :param account: The account of this AccountReport.
        :type: Account
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")

        self._account = account

    @property
    def children(self):
        """
        Gets the children of this AccountReport.

        :return: The children of this AccountReport.
        :rtype: list[ChildAccountReport]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this AccountReport.

        :param children: The children of this AccountReport.
        :type: list[ChildAccountReport]
        """
        if children is None:
            raise ValueError("Invalid value for `children`, must not be `None`")

        self._children = children

    @property
    def aggregated(self):
        """
        Gets the aggregated of this AccountReport.

        :return: The aggregated of this AccountReport.
        :rtype: BillingData
        """
        return self._aggregated

    @aggregated.setter
    def aggregated(self, aggregated):
        """
        Sets the aggregated of this AccountReport.

        :param aggregated: The aggregated of this AccountReport.
        :type: BillingData
        """
        if aggregated is None:
            raise ValueError("Invalid value for `aggregated`, must not be `None`")

        self._aggregated = aggregated

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
        if not isinstance(other, AccountReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
