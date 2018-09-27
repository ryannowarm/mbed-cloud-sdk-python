"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class User(Entity):
    """Represents the `User` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "address",
        "created_at",
        "creation_time",
        "email",
        "email_verified",
        "full_name",
        "group_ids",
        "id",
        "last_login_time",
        "login_history",
        "marketing_accepted",
        "password",
        "password_changed_time",
        "phone_number",
        "status",
        "terms_accepted",
        "two_factor_authentication",
        "updated_at",
        "username",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {
        "groups": "group_ids",
        "is_marketing_accepted": "marketing_accepted",
        "is_gtc_accepted": "terms_accepted",
        "is_totp_enabled": "two_factor_authentication",
    }

    def __init__(
        self,
        _client=None,
        account_id=None,
        address=None,
        created_at=None,
        creation_time=None,
        email=None,
        email_verified=None,
        full_name=None,
        group_ids=None,
        id=None,
        last_login_time=None,
        login_history=None,
        marketing_accepted=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        terms_accepted=None,
        two_factor_authentication=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance

        :param account_id: The UUID of the account.
        :type account_id: str
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param email: The email address.
        :type email: str
        :param email_verified: A flag indicating whether the user's email address has been
            verified or not.
        :type email_verified: bool
        :param full_name: The full name of the user.
        :type full_name: str
        :param group_ids: A list of IDs of the groups this user belongs to.
        :type group_ids: list
        :param id: Entity ID.
        :type id: str
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param marketing_accepted: A flag indicating that receiving marketing information has been
            accepted.
        :type marketing_accepted: bool
        :param password: The password when creating a new user. It will be generated when
            not present in the request.
        :type password: str
        :param password_changed_time: A timestamp of the latest change of the user password, in
            milliseconds.
        :type password_changed_time: int
        :param phone_number: Phone number.
        :type phone_number: str
        :param status: The status of the user. ENROLLING state indicates that the user is
            in the middle of the enrollment process. INVITED means that the
            user has not accepted the invitation request. RESET means that the
            password must be changed immediately. INACTIVE users are locked
            out and not permitted to use the system.
        :type status: str
        :param terms_accepted: A flag indicating that the General Terms and Conditions has been
            accepted.
        :type terms_accepted: bool
        :param two_factor_authentication: A flag indicating whether 2-factor authentication (TOTP) has been
            enabled.
        :type two_factor_authentication: bool
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username containing alphanumerical letters and -,._@+=
            characters.
        :type username: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        from mbed_cloud.sdk._modules.accounts.login_history import LoginHistory

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._address = fields.StringField(value=address)
        self._created_at = fields.DateTimeField(value=created_at)
        self._creation_time = fields.IntegerField(value=creation_time)
        self._email = fields.StringField(value=email)
        self._email_verified = fields.BooleanField(value=email_verified)
        self._full_name = fields.StringField(value=full_name)
        self._group_ids = fields.ListField(value=group_ids)
        self._id = fields.StringField(value=id)
        self._last_login_time = fields.IntegerField(value=last_login_time)
        self._login_history = fields.ListField(value=login_history, entity=LoginHistory)
        self._marketing_accepted = fields.BooleanField(value=marketing_accepted)
        self._password = fields.StringField(value=password)
        self._password_changed_time = fields.IntegerField(value=password_changed_time)
        self._phone_number = fields.StringField(value=phone_number)
        self._status = fields.StringField(value=status, enum=enums.UserStatusEnum)
        self._terms_accepted = fields.BooleanField(value=terms_accepted)
        self._two_factor_authentication = fields.BooleanField(
            value=two_factor_authentication
        )
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._username = fields.StringField(value=username)

    @property
    def account_id(self):
        """The UUID of the account.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

    @property
    def address(self):
        """Address.
        
        api example: '110 Fulbourn Rd, Cambridge, United Kingdom'
        
        :rtype: str
        """

        return self._address.value

    @address.setter
    def address(self, value):
        """Set value of `address`

        :param value: value to set
        :type value: str
        """

        self._address.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """

        self._created_at.set(value)

    @property
    def creation_time(self):
        """A timestamp of the user creation in the storage, in milliseconds.
        
        api example: 1518630727683
        
        :rtype: int
        """

        return self._creation_time.value

    @creation_time.setter
    def creation_time(self, value):
        """Set value of `creation_time`

        :param value: value to set
        :type value: int
        """

        self._creation_time.set(value)

    @property
    def email(self):
        """The email address.
        
        api example: 'user@arm.com'
        
        :rtype: str
        """

        return self._email.value

    @email.setter
    def email(self, value):
        """Set value of `email`

        :param value: value to set
        :type value: str
        """

        self._email.set(value)

    @property
    def email_verified(self):
        """A flag indicating whether the user's email address has been verified or not.
        
        api example: True
        
        :rtype: bool
        """

        return self._email_verified.value

    @email_verified.setter
    def email_verified(self, value):
        """Set value of `email_verified`

        :param value: value to set
        :type value: bool
        """

        self._email_verified.set(value)

    @property
    def full_name(self):
        """The full name of the user.
        
        api example: 'User Doe'
        
        :rtype: str
        """

        return self._full_name.value

    @full_name.setter
    def full_name(self, value):
        """Set value of `full_name`

        :param value: value to set
        :type value: str
        """

        self._full_name.set(value)

    @property
    def group_ids(self):
        """A list of IDs of the groups this user belongs to.
        
        :rtype: list
        """

        return self._group_ids.value

    @group_ids.setter
    def group_ids(self, value):
        """Set value of `group_ids`

        :param value: value to set
        :type value: list
        """

        self._group_ids.set(value)

    @property
    def id(self):
        """Entity ID.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def last_login_time(self):
        """A timestamp of the latest login of the user, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._last_login_time.value

    @last_login_time.setter
    def last_login_time(self, value):
        """Set value of `last_login_time`

        :param value: value to set
        :type value: int
        """

        self._last_login_time.set(value)

    @property
    def login_history(self):
        """Timestamps, succeedings, IP addresses and user agent information of the last
        five logins of the user, with timestamps in RFC3339 format.
        
        :rtype: list[LoginHistory]
        """

        return self._login_history.value

    @login_history.setter
    def login_history(self, value):
        """Set value of `login_history`

        :param value: value to set
        :type value: list[LoginHistory]
        """

        self._login_history.set(value)

    @property
    def marketing_accepted(self):
        """A flag indicating that receiving marketing information has been accepted.
        
        api example: True
        
        :rtype: bool
        """

        return self._marketing_accepted.value

    @marketing_accepted.setter
    def marketing_accepted(self, value):
        """Set value of `marketing_accepted`

        :param value: value to set
        :type value: bool
        """

        self._marketing_accepted.set(value)

    @property
    def password(self):
        """The password when creating a new user. It will be generated when not present
        in the request.
        
        api example: 'PZf9eEUH43DAPE9ULINFeuj'
        
        :rtype: str
        """

        return self._password.value

    @password.setter
    def password(self, value):
        """Set value of `password`

        :param value: value to set
        :type value: str
        """

        self._password.set(value)

    @property
    def password_changed_time(self):
        """A timestamp of the latest change of the user password, in milliseconds.
        
        api example: 1518630727688
        
        :rtype: int
        """

        return self._password_changed_time.value

    @password_changed_time.setter
    def password_changed_time(self, value):
        """Set value of `password_changed_time`

        :param value: value to set
        :type value: int
        """

        self._password_changed_time.set(value)

    @property
    def phone_number(self):
        """Phone number.
        
        api example: '+44 (1223) 400 400'
        
        :rtype: str
        """

        return self._phone_number.value

    @phone_number.setter
    def phone_number(self, value):
        """Set value of `phone_number`

        :param value: value to set
        :type value: str
        """

        self._phone_number.set(value)

    @property
    def status(self):
        """The status of the user. ENROLLING state indicates that the user is in the
        middle of the enrollment process. INVITED means that the user has not accepted
        the invitation request. RESET means that the password must be changed
        immediately. INACTIVE users are locked out and not permitted to use the
        system.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """

        return self._status.value

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """

        self._status.set(value)

    @property
    def terms_accepted(self):
        """A flag indicating that the General Terms and Conditions has been accepted.
        
        api example: True
        
        :rtype: bool
        """

        return self._terms_accepted.value

    @terms_accepted.setter
    def terms_accepted(self, value):
        """Set value of `terms_accepted`

        :param value: value to set
        :type value: bool
        """

        self._terms_accepted.set(value)

    @property
    def two_factor_authentication(self):
        """A flag indicating whether 2-factor authentication (TOTP) has been enabled.
        
        api example: True
        
        :rtype: bool
        """

        return self._two_factor_authentication.value

    @two_factor_authentication.setter
    def two_factor_authentication(self, value):
        """Set value of `two_factor_authentication`

        :param value: value to set
        :type value: bool
        """

        self._two_factor_authentication.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """

        self._updated_at.set(value)

    @property
    def username(self):
        """A username containing alphanumerical letters and -,._@+= characters.
        
        api example: 'admin'
        
        :rtype: str
        """

        return self._username.value

    @username.setter
    def username(self, value):
        """Set value of `username`

        :param value: value to set
        :type value: str
        """

        self._username.set(value)

    def add_to_groups(self, add_to_group_ids):
        """Add user to a list of groups.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}/groups
        
        :param add_to_group_ids: A list of IDs of the groups to be updated.
        :type add_to_group_ids: list
        
        :rtype: User
        """

        return self._client.call_api(
            method="post",
            path="/v3/users/{user-id}/groups",
            body_params=fields.ListField(add_to_group_ids).to_api(),
            path_params={"user-id": self._id.to_api()},
            unpack=self,
        )

    def create(self, action="create"):
        """Create a new user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users
        
        :param action: Action, either 'create' or 'invite'.
        :type action: str
        
        :rtype: User
        """

        from mbed_cloud.sdk.common._custom_methods import (
            subtenant_account_switch_create
        )

        return subtenant_account_switch_create(
            self=self, foreign_key=self.__class__, action=action
        )

    def _create_on_aggregator(self, action="create"):
        """Create a new user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users
        
        :param action: Action, either 'create' or 'invite'.
        :type action: str
        
        :rtype: User
        """

        return self._client.call_api(
            method="post",
            path="/v3/users",
            body_params={
                "address": self._address.to_api(),
                "email": self._email.to_api(),
                "full_name": self._full_name.to_api(),
                "groups": self._group_ids.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "password": self._password.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "username": self._username.to_api(),
            },
            query_params={"action": fields.StringField(action).to_api()},
            unpack=self,
        )

    def _create_on_subtenant(self, action="create"):
        """Create a new user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{accountID}/users
        
        :param action: Create or invite user.
        :type action: str
        
        :rtype: User
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{accountID}/users",
            body_params={
                "address": self._address.to_api(),
                "email": self._email.to_api(),
                "full_name": self._full_name.to_api(),
                "groups": self._group_ids.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "password": self._password.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "username": self._username.to_api(),
            },
            path_params={"accountID": self._account_id.to_api()},
            query_params={"action": fields.StringField(action).to_api()},
            unpack=self,
        )

    def delete(self):
        """Delete a user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}
        
        :rtype: User
        """

        return self._client.call_api(
            method="delete",
            path="/v3/users/{user-id}",
            path_params={"": self._id.to_api()},
            unpack=self,
        )

    def get(self):
        """Details of the user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{accountID}/users/{user-id}
        
        :rtype: User
        """

        from mbed_cloud.sdk.common._custom_methods import subtenant_account_switch_get

        return subtenant_account_switch_get(self=self, foreign_key=self.__class__)

    def _get_on_aggregator(self):
        """Details of a user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}
        
        :rtype: User
        """

        return self._client.call_api(
            method="get",
            path="/v3/users/{user-id}",
            path_params={"user-id": self._id.to_api()},
            unpack=self,
        )

    def _get_on_subtenant(self):
        """Details of the user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{accountID}/users/{user-id}
        
        :rtype: User
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{accountID}/users/{user-id}",
            path_params={
                "accountID": self._account_id.to_api(),
                "user-id": self._id.to_api(),
            },
            unpack=self,
        )

    def groups(self, after=None, include=None, limit=50, order="ASC"):
        """Get groups of the user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}/groups
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import PolicyGroup

        return paginate(
            self=self,
            foreign_key=PolicyGroup,
            after=after,
            include=include,
            limit=limit,
            order=order,
            wraps=self._paginate_groups,
        )

    def list(self, after=None, include=None, limit=50, order="ASC"):
        """Get the details of all users.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import User

        return paginate(
            self=self,
            foreign_key=User,
            after=after,
            include=include,
            limit=limit,
            order=order,
            wraps=self._paginate_list,
        )

    def _paginate_groups(self, after=None, include=None, limit=50, order="ASC"):
        """Get groups of the user.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}/groups
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/users/{user-id}/groups",
            path_params={"user-id": self._id.to_api()},
            query_params={
                "after": fields.StringField(after).to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(
                    order, enum=enums.SubtenantAccountOrderEnum
                ).to_api(),
            },
            unpack=False,
        )

    def _paginate_list(self, after=None, include=None, limit=50, order="ASC"):
        """Get the details of all users.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/users",
            query_params={
                "after": fields.StringField(after).to_api(),
                "include": fields.StringField(include).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "order": fields.StringField(
                    order, enum=enums.SubtenantAccountOrderEnum
                ).to_api(),
            },
            unpack=False,
        )

    def update(self):
        """Update user details.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/users/{user-id}
        
        :rtype: User
        """

        return self._client.call_api(
            method="put",
            path="/v3/users/{user-id}",
            body_params={
                "address": self._address.to_api(),
                "full_name": self._full_name.to_api(),
                "groups": self._group_ids.to_api(),
                "is_marketing_accepted": self._marketing_accepted.to_api(),
                "phone_number": self._phone_number.to_api(),
                "is_gtc_accepted": self._terms_accepted.to_api(),
                "is_totp_enabled": self._two_factor_authentication.to_api(),
                "username": self._username.to_api(),
            },
            path_params={"user-id": self._id.to_api()},
            unpack=self,
        )

    def validate_email(self):
        """Validate the user email.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{accountID}/users/{user-id}/validate-email
        
        :rtype: User
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{accountID}/users/{user-id}/validate-email",
            path_params={
                "accountID": self._account_id.to_api(),
                "user-id": self._id.to_api(),
            },
            unpack=self,
        )
