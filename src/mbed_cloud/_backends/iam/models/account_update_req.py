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


class AccountUpdateReq(object):
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
        'address_line2': 'str',
        'city': 'str',
        'address_line1': 'str',
        'display_name': 'str',
        'mfa_status': 'str',
        'state': 'str',
        'country': 'str',
        'company': 'str',
        'idle_timeout': 'str',
        'password_policy': 'PasswordPolicy',
        'expiration_warning_threshold': 'str',
        'contact': 'str',
        'postal_code': 'str',
        'account_properties': 'dict(str, dict(str, str))',
        'notification_emails': 'list[str]',
        'end_market': 'str',
        'phone_number': 'str',
        'email': 'str',
        'aliases': 'list[str]'
    }

    attribute_map = {
        'address_line2': 'address_line2',
        'city': 'city',
        'address_line1': 'address_line1',
        'display_name': 'display_name',
        'mfa_status': 'mfa_status',
        'state': 'state',
        'country': 'country',
        'company': 'company',
        'idle_timeout': 'idle_timeout',
        'password_policy': 'password_policy',
        'expiration_warning_threshold': 'expiration_warning_threshold',
        'contact': 'contact',
        'postal_code': 'postal_code',
        'account_properties': 'account_properties',
        'notification_emails': 'notification_emails',
        'end_market': 'end_market',
        'phone_number': 'phone_number',
        'email': 'email',
        'aliases': 'aliases'
    }

    def __init__(self, address_line2=None, city=None, address_line1=None, display_name=None, mfa_status=None, state=None, country=None, company=None, idle_timeout=None, password_policy=None, expiration_warning_threshold=None, contact=None, postal_code=None, account_properties=None, notification_emails=None, end_market=None, phone_number=None, email=None, aliases=None):
        """
        AccountUpdateReq - a model defined in Swagger
        """

        self._address_line2 = address_line2
        self._city = city
        self._address_line1 = address_line1
        self._display_name = display_name
        self._mfa_status = mfa_status
        self._state = state
        self._country = country
        self._company = company
        self._idle_timeout = idle_timeout
        self._password_policy = password_policy
        self._expiration_warning_threshold = expiration_warning_threshold
        self._contact = contact
        self._postal_code = postal_code
        self._account_properties = account_properties
        self._notification_emails = notification_emails
        self._end_market = end_market
        self._phone_number = phone_number
        self._email = email
        self._aliases = aliases
        self.discriminator = None

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountUpdateReq.
        Postal address line 2, not longer than 100 characters.

        :return: The address_line2 of this AccountUpdateReq.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountUpdateReq.
        Postal address line 2, not longer than 100 characters.

        :param address_line2: The address_line2 of this AccountUpdateReq.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """
        Gets the city of this AccountUpdateReq.
        The city part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :return: The city of this AccountUpdateReq.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountUpdateReq.
        The city part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :param city: The city of this AccountUpdateReq.
        :type: str
        """

        self._city = city

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountUpdateReq.
        Postal address line 1, not longer than 100 characters. Required for commercial accounts only.

        :return: The address_line1 of this AccountUpdateReq.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountUpdateReq.
        Postal address line 1, not longer than 100 characters. Required for commercial accounts only.

        :param address_line1: The address_line1 of this AccountUpdateReq.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountUpdateReq.
        The display name for the account, not longer than 100 characters.

        :return: The display_name of this AccountUpdateReq.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountUpdateReq.
        The display name for the account, not longer than 100 characters.

        :param display_name: The display_name of this AccountUpdateReq.
        :type: str
        """

        self._display_name = display_name

    @property
    def mfa_status(self):
        """
        Gets the mfa_status of this AccountUpdateReq.
        The enforcement status of setting up the multi-factor authentication. 'Enforced' means that setting up the MFA is required after login. 'Optional' means that the MFA is not required.

        :return: The mfa_status of this AccountUpdateReq.
        :rtype: str
        """
        return self._mfa_status

    @mfa_status.setter
    def mfa_status(self, mfa_status):
        """
        Sets the mfa_status of this AccountUpdateReq.
        The enforcement status of setting up the multi-factor authentication. 'Enforced' means that setting up the MFA is required after login. 'Optional' means that the MFA is not required.

        :param mfa_status: The mfa_status of this AccountUpdateReq.
        :type: str
        """
        allowed_values = ["enforced", "optional"]
        if mfa_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mfa_status` ({0}), must be one of {1}"
                .format(mfa_status, allowed_values)
            )

        self._mfa_status = mfa_status

    @property
    def state(self):
        """
        Gets the state of this AccountUpdateReq.
        The state part of the postal address, not longer than 100 characters.

        :return: The state of this AccountUpdateReq.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountUpdateReq.
        The state part of the postal address, not longer than 100 characters.

        :param state: The state of this AccountUpdateReq.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this AccountUpdateReq.
        The country part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :return: The country of this AccountUpdateReq.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountUpdateReq.
        The country part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :param country: The country of this AccountUpdateReq.
        :type: str
        """

        self._country = country

    @property
    def company(self):
        """
        Gets the company of this AccountUpdateReq.
        The name of the company, not longer than 100 characters. Required for commercial accounts only.

        :return: The company of this AccountUpdateReq.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountUpdateReq.
        The name of the company, not longer than 100 characters. Required for commercial accounts only.

        :param company: The company of this AccountUpdateReq.
        :type: str
        """

        self._company = company

    @property
    def idle_timeout(self):
        """
        Gets the idle_timeout of this AccountUpdateReq.
        The reference token expiration time in minutes for this account. Between 1 and 120 minutes.

        :return: The idle_timeout of this AccountUpdateReq.
        :rtype: str
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """
        Sets the idle_timeout of this AccountUpdateReq.
        The reference token expiration time in minutes for this account. Between 1 and 120 minutes.

        :param idle_timeout: The idle_timeout of this AccountUpdateReq.
        :type: str
        """

        self._idle_timeout = idle_timeout

    @property
    def password_policy(self):
        """
        Gets the password_policy of this AccountUpdateReq.
        Password policy for this account.

        :return: The password_policy of this AccountUpdateReq.
        :rtype: PasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """
        Sets the password_policy of this AccountUpdateReq.
        Password policy for this account.

        :param password_policy: The password_policy of this AccountUpdateReq.
        :type: PasswordPolicy
        """

        self._password_policy = password_policy

    @property
    def expiration_warning_threshold(self):
        """
        Gets the expiration_warning_threshold of this AccountUpdateReq.
        Indicates how many days before account expiration a notification email should be sent. Valid values are: 1-180.

        :return: The expiration_warning_threshold of this AccountUpdateReq.
        :rtype: str
        """
        return self._expiration_warning_threshold

    @expiration_warning_threshold.setter
    def expiration_warning_threshold(self, expiration_warning_threshold):
        """
        Sets the expiration_warning_threshold of this AccountUpdateReq.
        Indicates how many days before account expiration a notification email should be sent. Valid values are: 1-180.

        :param expiration_warning_threshold: The expiration_warning_threshold of this AccountUpdateReq.
        :type: str
        """

        self._expiration_warning_threshold = expiration_warning_threshold

    @property
    def contact(self):
        """
        Gets the contact of this AccountUpdateReq.
        The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only.

        :return: The contact of this AccountUpdateReq.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountUpdateReq.
        The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only.

        :param contact: The contact of this AccountUpdateReq.
        :type: str
        """

        self._contact = contact

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountUpdateReq.
        The postal code part of the postal address, not longer than 100 characters.

        :return: The postal_code of this AccountUpdateReq.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountUpdateReq.
        The postal code part of the postal address, not longer than 100 characters.

        :param postal_code: The postal_code of this AccountUpdateReq.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def account_properties(self):
        """
        Gets the account_properties of this AccountUpdateReq.
        Properties for this account.

        :return: The account_properties of this AccountUpdateReq.
        :rtype: dict(str, dict(str, str))
        """
        return self._account_properties

    @account_properties.setter
    def account_properties(self, account_properties):
        """
        Sets the account_properties of this AccountUpdateReq.
        Properties for this account.

        :param account_properties: The account_properties of this AccountUpdateReq.
        :type: dict(str, dict(str, str))
        """

        self._account_properties = account_properties

    @property
    def notification_emails(self):
        """
        Gets the notification_emails of this AccountUpdateReq.
        A list of notification email addresses.

        :return: The notification_emails of this AccountUpdateReq.
        :rtype: list[str]
        """
        return self._notification_emails

    @notification_emails.setter
    def notification_emails(self, notification_emails):
        """
        Sets the notification_emails of this AccountUpdateReq.
        A list of notification email addresses.

        :param notification_emails: The notification_emails of this AccountUpdateReq.
        :type: list[str]
        """

        self._notification_emails = notification_emails

    @property
    def end_market(self):
        """
        Gets the end_market of this AccountUpdateReq.
        The end market for this account, not longer than 100 characters.

        :return: The end_market of this AccountUpdateReq.
        :rtype: str
        """
        return self._end_market

    @end_market.setter
    def end_market(self, end_market):
        """
        Sets the end_market of this AccountUpdateReq.
        The end market for this account, not longer than 100 characters.

        :param end_market: The end_market of this AccountUpdateReq.
        :type: str
        """

        self._end_market = end_market

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountUpdateReq.
        The phone number of a representative of the company, not longer than 100 characters.

        :return: The phone_number of this AccountUpdateReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountUpdateReq.
        The phone number of a representative of the company, not longer than 100 characters.

        :param phone_number: The phone_number of this AccountUpdateReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this AccountUpdateReq.
        The company email address for this account, not longer than 254 characters. Required for commercial accounts only.

        :return: The email of this AccountUpdateReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountUpdateReq.
        The company email address for this account, not longer than 254 characters. Required for commercial accounts only.

        :param email: The email of this AccountUpdateReq.
        :type: str
        """

        self._email = email

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountUpdateReq.
        An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters.

        :return: The aliases of this AccountUpdateReq.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountUpdateReq.
        An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters.

        :param aliases: The aliases of this AccountUpdateReq.
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
        if not isinstance(other, AccountUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
