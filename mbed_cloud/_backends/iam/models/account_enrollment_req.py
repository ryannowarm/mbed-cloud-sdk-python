# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and API keys

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountEnrollmentReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, username=None, code=None, is_gtc_accepted=None, is_marketing_accepted=None, password=None, aliases=None):
        """
        AccountEnrollmentReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'username': 'str',
            'code': 'str',
            'is_gtc_accepted': 'bool',
            'is_marketing_accepted': 'bool',
            'password': 'str',
            'aliases': 'list[str]'
        }

        self.attribute_map = {
            'username': 'username',
            'code': 'code',
            'is_gtc_accepted': 'is_gtc_accepted',
            'is_marketing_accepted': 'is_marketing_accepted',
            'password': 'password',
            'aliases': 'aliases'
        }

        self._username = username
        self._code = code
        self._is_gtc_accepted = is_gtc_accepted
        self._is_marketing_accepted = is_marketing_accepted
        self._password = password
        self._aliases = aliases

    @property
    def username(self):
        """
        Gets the username of this AccountEnrollmentReq.
        A username for the new account admin containing alphanumerical letters and -,._@+= characters.

        :return: The username of this AccountEnrollmentReq.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this AccountEnrollmentReq.
        A username for the new account admin containing alphanumerical letters and -,._@+= characters.

        :param username: The username of this AccountEnrollmentReq.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def code(self):
        """
        Gets the code of this AccountEnrollmentReq.
        Verification code.

        :return: The code of this AccountEnrollmentReq.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this AccountEnrollmentReq.
        Verification code.

        :param code: The code of this AccountEnrollmentReq.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def is_gtc_accepted(self):
        """
        Gets the is_gtc_accepted of this AccountEnrollmentReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :return: The is_gtc_accepted of this AccountEnrollmentReq.
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """
        Sets the is_gtc_accepted of this AccountEnrollmentReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :param is_gtc_accepted: The is_gtc_accepted of this AccountEnrollmentReq.
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def is_marketing_accepted(self):
        """
        Gets the is_marketing_accepted of this AccountEnrollmentReq.
        A flag indicating that receiving marketing information has been accepted.

        :return: The is_marketing_accepted of this AccountEnrollmentReq.
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """
        Sets the is_marketing_accepted of this AccountEnrollmentReq.
        A flag indicating that receiving marketing information has been accepted.

        :param is_marketing_accepted: The is_marketing_accepted of this AccountEnrollmentReq.
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def password(self):
        """
        Gets the password of this AccountEnrollmentReq.
        The password for the new account admin.

        :return: The password of this AccountEnrollmentReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AccountEnrollmentReq.
        The password for the new account admin.

        :param password: The password of this AccountEnrollmentReq.
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountEnrollmentReq.
        An array of aliases.

        :return: The aliases of this AccountEnrollmentReq.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountEnrollmentReq.
        An array of aliases.

        :param aliases: The aliases of this AccountEnrollmentReq.
        :type: list[str]
        """

        self._aliases = aliases

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
        if not isinstance(other, AccountEnrollmentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
