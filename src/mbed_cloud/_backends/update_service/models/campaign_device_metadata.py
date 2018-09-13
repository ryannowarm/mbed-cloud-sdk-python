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


class CampaignDeviceMetadata(object):
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
        'campaign': 'str',
        'created_at': 'datetime',
        'deployment_state': 'str',
        'description': 'str',
        'device_id': 'str',
        'etag': 'str',
        'id': 'str',
        'mechanism': 'str',
        'mechanism_url': 'str',
        'name': 'str',
        'object': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'campaign': 'campaign',
        'created_at': 'created_at',
        'deployment_state': 'deployment_state',
        'description': 'description',
        'device_id': 'device_id',
        'etag': 'etag',
        'id': 'id',
        'mechanism': 'mechanism',
        'mechanism_url': 'mechanism_url',
        'name': 'name',
        'object': 'object',
        'updated_at': 'updated_at'
    }

    def __init__(self, campaign=None, created_at=None, deployment_state=None, description=None, device_id=None, etag=None, id=None, mechanism=None, mechanism_url=None, name=None, object=None, updated_at=None):
        """
        CampaignDeviceMetadata - a model defined in Swagger
        """

        self._campaign = campaign
        self._created_at = created_at
        self._deployment_state = deployment_state
        self._description = description
        self._device_id = device_id
        self._etag = etag
        self._id = id
        self._mechanism = mechanism
        self._mechanism_url = mechanism_url
        self._name = name
        self._object = object
        self._updated_at = updated_at
        self.discriminator = None

    @property
    def campaign(self):
        """
        Gets the campaign of this CampaignDeviceMetadata.
        The device's campaign ID

        :return: The campaign of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this CampaignDeviceMetadata.
        The device's campaign ID

        :param campaign: The campaign of this CampaignDeviceMetadata.
        :type: str
        """

        self._campaign = campaign

    @property
    def created_at(self):
        """
        Gets the created_at of this CampaignDeviceMetadata.
        The time the campaign was created

        :return: The created_at of this CampaignDeviceMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CampaignDeviceMetadata.
        The time the campaign was created

        :param created_at: The created_at of this CampaignDeviceMetadata.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deployment_state(self):
        """
        Gets the deployment_state of this CampaignDeviceMetadata.
        The state of the update campaign on the device

        :return: The deployment_state of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._deployment_state

    @deployment_state.setter
    def deployment_state(self, deployment_state):
        """
        Sets the deployment_state of this CampaignDeviceMetadata.
        The state of the update campaign on the device

        :param deployment_state: The deployment_state of this CampaignDeviceMetadata.
        :type: str
        """
        allowed_values = ["pending", "updated_connector_channel", "failed_connector_channel_update", "deployed", "manifestremoved", "deregistered"]
        if deployment_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_state` ({0}), must be one of {1}"
                .format(deployment_state, allowed_values)
            )

        self._deployment_state = deployment_state

    @property
    def description(self):
        """
        Gets the description of this CampaignDeviceMetadata.
        Description

        :return: The description of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CampaignDeviceMetadata.
        Description

        :param description: The description of this CampaignDeviceMetadata.
        :type: str
        """
        if description is not None and len(description) > 2000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2000`")

        self._description = description

    @property
    def device_id(self):
        """
        Gets the device_id of this CampaignDeviceMetadata.
        The device ID

        :return: The device_id of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this CampaignDeviceMetadata.
        The device ID

        :param device_id: The device_id of this CampaignDeviceMetadata.
        :type: str
        """

        self._device_id = device_id

    @property
    def etag(self):
        """
        Gets the etag of this CampaignDeviceMetadata.
        API resource entity version

        :return: The etag of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CampaignDeviceMetadata.
        API resource entity version

        :param etag: The etag of this CampaignDeviceMetadata.
        :type: str
        """

        self._etag = etag

    @property
    def id(self):
        """
        Gets the id of this CampaignDeviceMetadata.
        The metadata record ID

        :return: The id of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignDeviceMetadata.
        The metadata record ID

        :param id: The id of this CampaignDeviceMetadata.
        :type: str
        """

        self._id = id

    @property
    def mechanism(self):
        """
        Gets the mechanism of this CampaignDeviceMetadata.
        How the firmware is delivered (connector or direct)

        :return: The mechanism of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this CampaignDeviceMetadata.
        How the firmware is delivered (connector or direct)

        :param mechanism: The mechanism of this CampaignDeviceMetadata.
        :type: str
        """

        self._mechanism = mechanism

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this CampaignDeviceMetadata.
        The Device Management Connect URL

        :return: The mechanism_url of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this CampaignDeviceMetadata.
        The Device Management Connect URL

        :param mechanism_url: The mechanism_url of this CampaignDeviceMetadata.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def name(self):
        """
        Gets the name of this CampaignDeviceMetadata.
        The record name

        :return: The name of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignDeviceMetadata.
        The record name

        :param name: The name of this CampaignDeviceMetadata.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

        self._name = name

    @property
    def object(self):
        """
        Gets the object of this CampaignDeviceMetadata.
        The entity name: always 'update-campaign-device-metadata'

        :return: The object of this CampaignDeviceMetadata.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CampaignDeviceMetadata.
        The entity name: always 'update-campaign-device-metadata'

        :param object: The object of this CampaignDeviceMetadata.
        :type: str
        """

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CampaignDeviceMetadata.
        The record was modified in the database format: date-time

        :return: The updated_at of this CampaignDeviceMetadata.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CampaignDeviceMetadata.
        The record was modified in the database format: date-time

        :param updated_at: The updated_at of this CampaignDeviceMetadata.
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, CampaignDeviceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
