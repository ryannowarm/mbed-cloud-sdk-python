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


class AccountCreationResp(object):
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
        'end_market': 'str',
        'admin_id': 'str',
        'admin_name': 'str',
        'postal_code': 'str',
        'id': 'str',
        'aliases': 'list[str]',
        'address_line2': 'str',
        'city': 'str',
        'address_line1': 'str',
        'display_name': 'str',
        'state': 'str',
        'admin_password': 'str',
        'email': 'str',
        'phone_number': 'str',
        'contract_number': 'str',
        'company': 'str',
        'admin_key': 'str',
        'admin_full_name': 'str',
        'country': 'str',
        'customer_number': 'str',
        'contact': 'str',
        'admin_email': 'str'
    }

    attribute_map = {
        'end_market': 'end_market',
        'admin_id': 'admin_id',
        'admin_name': 'admin_name',
        'postal_code': 'postal_code',
        'id': 'id',
        'aliases': 'aliases',
        'address_line2': 'address_line2',
        'city': 'city',
        'address_line1': 'address_line1',
        'display_name': 'display_name',
        'state': 'state',
        'admin_password': 'admin_password',
        'email': 'email',
        'phone_number': 'phone_number',
        'contract_number': 'contract_number',
        'company': 'company',
        'admin_key': 'admin_key',
        'admin_full_name': 'admin_full_name',
        'country': 'country',
        'customer_number': 'customer_number',
        'contact': 'contact',
        'admin_email': 'admin_email'
    }

    def __init__(self, end_market=None, admin_id=None, admin_name=None, postal_code=None, id=None, aliases=None, address_line2=None, city=None, address_line1=None, display_name=None, state=None, admin_password=None, email=None, phone_number=None, contract_number=None, company=None, admin_key=None, admin_full_name=None, country=None, customer_number=None, contact=None, admin_email=None):
        """
        AccountCreationResp - a model defined in Swagger
        """

        self._end_market = end_market
        self._admin_id = admin_id
        self._admin_name = admin_name
        self._postal_code = postal_code
        self._id = id
        self._aliases = aliases
        self._address_line2 = address_line2
        self._city = city
        self._address_line1 = address_line1
        self._display_name = display_name
        self._state = state
        self._admin_password = admin_password
        self._email = email
        self._phone_number = phone_number
        self._contract_number = contract_number
        self._company = company
        self._admin_key = admin_key
        self._admin_full_name = admin_full_name
        self._country = country
        self._customer_number = customer_number
        self._contact = contact
        self._admin_email = admin_email
        self.discriminator = None

    @property
    def end_market(self):
        """
        Gets the end_market of this AccountCreationResp.
        The end market of the account to be created.

        :return: The end_market of this AccountCreationResp.
        :rtype: str
        """
        return self._end_market

    @end_market.setter
    def end_market(self, end_market):
        """
        Sets the end_market of this AccountCreationResp.
        The end market of the account to be created.

        :param end_market: The end_market of this AccountCreationResp.
        :type: str
        """
        if end_market is None:
            raise ValueError("Invalid value for `end_market`, must not be `None`")

        self._end_market = end_market

    @property
    def admin_id(self):
        """
        Gets the admin_id of this AccountCreationResp.
        The ID of the admin user created.

        :return: The admin_id of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_id

    @admin_id.setter
    def admin_id(self, admin_id):
        """
        Sets the admin_id of this AccountCreationResp.
        The ID of the admin user created.

        :param admin_id: The admin_id of this AccountCreationResp.
        :type: str
        """
        if admin_id is None:
            raise ValueError("Invalid value for `admin_id`, must not be `None`")

        self._admin_id = admin_id

    @property
    def admin_name(self):
        """
        Gets the admin_name of this AccountCreationResp.
        The username of the admin user to be created, containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :return: The admin_name of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """
        Sets the admin_name of this AccountCreationResp.
        The username of the admin user to be created, containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :param admin_name: The admin_name of this AccountCreationResp.
        :type: str
        """

        self._admin_name = admin_name

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountCreationResp.
        The postal code part of the postal address, not longer than 100 characters.

        :return: The postal_code of this AccountCreationResp.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountCreationResp.
        The postal code part of the postal address, not longer than 100 characters.

        :param postal_code: The postal_code of this AccountCreationResp.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def id(self):
        """
        Gets the id of this AccountCreationResp.
        Account ID.

        :return: The id of this AccountCreationResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccountCreationResp.
        Account ID.

        :param id: The id of this AccountCreationResp.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountCreationResp.
        An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters.

        :return: The aliases of this AccountCreationResp.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountCreationResp.
        An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters.

        :param aliases: The aliases of this AccountCreationResp.
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountCreationResp.
        Postal address line 2, not longer than 100 characters.

        :return: The address_line2 of this AccountCreationResp.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountCreationResp.
        Postal address line 2, not longer than 100 characters.

        :param address_line2: The address_line2 of this AccountCreationResp.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """
        Gets the city of this AccountCreationResp.
        The city part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :return: The city of this AccountCreationResp.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountCreationResp.
        The city part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :param city: The city of this AccountCreationResp.
        :type: str
        """

        self._city = city

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountCreationResp.
        Postal address line 1, not longer than 100 characters. Required for commercial accounts only.

        :return: The address_line1 of this AccountCreationResp.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountCreationResp.
        Postal address line 1, not longer than 100 characters. Required for commercial accounts only.

        :param address_line1: The address_line1 of this AccountCreationResp.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountCreationResp.
        The display name for the account, not longer than 100 characters.

        :return: The display_name of this AccountCreationResp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountCreationResp.
        The display name for the account, not longer than 100 characters.

        :param display_name: The display_name of this AccountCreationResp.
        :type: str
        """

        self._display_name = display_name

    @property
    def state(self):
        """
        Gets the state of this AccountCreationResp.
        The state part of the postal address, not longer than 100 characters.

        :return: The state of this AccountCreationResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountCreationResp.
        The state part of the postal address, not longer than 100 characters.

        :param state: The state of this AccountCreationResp.
        :type: str
        """

        self._state = state

    @property
    def admin_password(self):
        """
        Gets the admin_password of this AccountCreationResp.
        The password when creating a new user. It will be generated when not present in the request.

        :return: The admin_password of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this AccountCreationResp.
        The password when creating a new user. It will be generated when not present in the request.

        :param admin_password: The admin_password of this AccountCreationResp.
        :type: str
        """

        self._admin_password = admin_password

    @property
    def email(self):
        """
        Gets the email of this AccountCreationResp.
        The company email address for this account, not longer than 254 characters. Required for commercial accounts only.

        :return: The email of this AccountCreationResp.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountCreationResp.
        The company email address for this account, not longer than 254 characters. Required for commercial accounts only.

        :param email: The email of this AccountCreationResp.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountCreationResp.
        The phone number of a representative of the company, not longer than 100 characters.

        :return: The phone_number of this AccountCreationResp.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountCreationResp.
        The phone number of a representative of the company, not longer than 100 characters.

        :param phone_number: The phone_number of this AccountCreationResp.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def contract_number(self):
        """
        Gets the contract_number of this AccountCreationResp.
        Contract number of the customer.

        :return: The contract_number of this AccountCreationResp.
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """
        Sets the contract_number of this AccountCreationResp.
        Contract number of the customer.

        :param contract_number: The contract_number of this AccountCreationResp.
        :type: str
        """

        self._contract_number = contract_number

    @property
    def company(self):
        """
        Gets the company of this AccountCreationResp.
        The name of the company, not longer than 100 characters. Required for commercial accounts only.

        :return: The company of this AccountCreationResp.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountCreationResp.
        The name of the company, not longer than 100 characters. Required for commercial accounts only.

        :param company: The company of this AccountCreationResp.
        :type: str
        """

        self._company = company

    @property
    def admin_key(self):
        """
        Gets the admin_key of this AccountCreationResp.
        The admin API key created for the account.

        :return: The admin_key of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_key

    @admin_key.setter
    def admin_key(self, admin_key):
        """
        Sets the admin_key of this AccountCreationResp.
        The admin API key created for the account.

        :param admin_key: The admin_key of this AccountCreationResp.
        :type: str
        """

        self._admin_key = admin_key

    @property
    def admin_full_name(self):
        """
        Gets the admin_full_name of this AccountCreationResp.
        The full name of the admin user to be created.

        :return: The admin_full_name of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_full_name

    @admin_full_name.setter
    def admin_full_name(self, admin_full_name):
        """
        Sets the admin_full_name of this AccountCreationResp.
        The full name of the admin user to be created.

        :param admin_full_name: The admin_full_name of this AccountCreationResp.
        :type: str
        """

        self._admin_full_name = admin_full_name

    @property
    def country(self):
        """
        Gets the country of this AccountCreationResp.
        The country part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :return: The country of this AccountCreationResp.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountCreationResp.
        The country part of the postal address, not longer than 100 characters. Required for commercial accounts only.

        :param country: The country of this AccountCreationResp.
        :type: str
        """

        self._country = country

    @property
    def customer_number(self):
        """
        Gets the customer_number of this AccountCreationResp.
        Customer number of the customer.

        :return: The customer_number of this AccountCreationResp.
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """
        Sets the customer_number of this AccountCreationResp.
        Customer number of the customer.

        :param customer_number: The customer_number of this AccountCreationResp.
        :type: str
        """

        self._customer_number = customer_number

    @property
    def contact(self):
        """
        Gets the contact of this AccountCreationResp.
        The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only.

        :return: The contact of this AccountCreationResp.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountCreationResp.
        The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only.

        :param contact: The contact of this AccountCreationResp.
        :type: str
        """

        self._contact = contact

    @property
    def admin_email(self):
        """
        Gets the admin_email of this AccountCreationResp.
        The email address of the account admin, not longer than 254 characters.

        :return: The admin_email of this AccountCreationResp.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this AccountCreationResp.
        The email address of the account admin, not longer than 254 characters.

        :param admin_email: The admin_email of this AccountCreationResp.
        :type: str
        """

        self._admin_email = admin_email

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
        if not isinstance(other, AccountCreationResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
