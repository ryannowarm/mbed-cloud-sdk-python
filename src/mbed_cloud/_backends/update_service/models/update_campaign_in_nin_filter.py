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


class UpdateCampaignInNinFilter(object):
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
        'description': 'str',
        'device_filter': 'str',
        'etag': 'datetime',
        'finished': 'datetime',
        'id': 'str',
        'name': 'str',
        'root_manifest_id': 'str',
        'started_at': 'datetime',
        'state': 'str',
        'updated_at': 'datetime',
        'when': 'datetime'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'device_filter': 'device_filter',
        'etag': 'etag',
        'finished': 'finished',
        'id': 'id',
        'name': 'name',
        'root_manifest_id': 'root_manifest_id',
        'started_at': 'started_at',
        'state': 'state',
        'updated_at': 'updated_at',
        'when': 'when'
    }

    def __init__(self, created_at=None, description=None, device_filter=None, etag=None, finished=None, id=None, name=None, root_manifest_id=None, started_at=None, state=None, updated_at=None, when=None):
        """
        UpdateCampaignInNinFilter - a model defined in Swagger
        """

        self._created_at = created_at
        self._description = description
        self._device_filter = device_filter
        self._etag = etag
        self._finished = finished
        self._id = id
        self._name = name
        self._root_manifest_id = root_manifest_id
        self._started_at = started_at
        self._state = state
        self._updated_at = updated_at
        self._when = when
        self.discriminator = None

    @property
    def created_at(self):
        """
        Gets the created_at of this UpdateCampaignInNinFilter.

        :return: The created_at of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UpdateCampaignInNinFilter.

        :param created_at: The created_at of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this UpdateCampaignInNinFilter.

        :return: The description of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCampaignInNinFilter.

        :param description: The description of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._description = description

    @property
    def device_filter(self):
        """
        Gets the device_filter of this UpdateCampaignInNinFilter.

        :return: The device_filter of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._device_filter

    @device_filter.setter
    def device_filter(self, device_filter):
        """
        Sets the device_filter of this UpdateCampaignInNinFilter.

        :param device_filter: The device_filter of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._device_filter = device_filter

    @property
    def etag(self):
        """
        Gets the etag of this UpdateCampaignInNinFilter.

        :return: The etag of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this UpdateCampaignInNinFilter.

        :param etag: The etag of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._etag = etag

    @property
    def finished(self):
        """
        Gets the finished of this UpdateCampaignInNinFilter.

        :return: The finished of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """
        Sets the finished of this UpdateCampaignInNinFilter.

        :param finished: The finished of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._finished = finished

    @property
    def id(self):
        """
        Gets the id of this UpdateCampaignInNinFilter.

        :return: The id of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateCampaignInNinFilter.

        :param id: The id of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UpdateCampaignInNinFilter.

        :return: The name of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCampaignInNinFilter.

        :param name: The name of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._name = name

    @property
    def root_manifest_id(self):
        """
        Gets the root_manifest_id of this UpdateCampaignInNinFilter.

        :return: The root_manifest_id of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._root_manifest_id

    @root_manifest_id.setter
    def root_manifest_id(self, root_manifest_id):
        """
        Sets the root_manifest_id of this UpdateCampaignInNinFilter.

        :param root_manifest_id: The root_manifest_id of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._root_manifest_id = root_manifest_id

    @property
    def started_at(self):
        """
        Gets the started_at of this UpdateCampaignInNinFilter.

        :return: The started_at of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this UpdateCampaignInNinFilter.

        :param started_at: The started_at of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def state(self):
        """
        Gets the state of this UpdateCampaignInNinFilter.

        :return: The state of this UpdateCampaignInNinFilter.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateCampaignInNinFilter.

        :param state: The state of this UpdateCampaignInNinFilter.
        :type: str
        """

        self._state = state

    @property
    def updated_at(self):
        """
        Gets the updated_at of this UpdateCampaignInNinFilter.

        :return: The updated_at of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this UpdateCampaignInNinFilter.

        :param updated_at: The updated_at of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def when(self):
        """
        Gets the when of this UpdateCampaignInNinFilter.

        :return: The when of this UpdateCampaignInNinFilter.
        :rtype: datetime
        """
        return self._when

    @when.setter
    def when(self, when):
        """
        Sets the when of this UpdateCampaignInNinFilter.

        :param when: The when of this UpdateCampaignInNinFilter.
        :type: datetime
        """

        self._when = when

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
        if not isinstance(other, UpdateCampaignInNinFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
