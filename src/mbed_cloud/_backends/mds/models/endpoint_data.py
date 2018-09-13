# coding: utf-8

"""
    Connect API

    Pelion Device Management Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. Device Management Connect allows connectivity to devices by queueing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EndpointData(object):
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
        'ep': 'str',
        'ept': 'str',
        'original_ep': 'str',
        'q': 'bool',
        'resources': 'list[ResourcesData]'
    }

    attribute_map = {
        'ep': 'ep',
        'ept': 'ept',
        'original_ep': 'original-ep',
        'q': 'q',
        'resources': 'resources'
    }

    def __init__(self, ep=None, ept=None, original_ep=None, q=None, resources=None):
        """
        EndpointData - a model defined in Swagger
        """

        self._ep = ep
        self._ept = ept
        self._original_ep = original_ep
        self._q = q
        self._resources = resources
        self.discriminator = None

    @property
    def ep(self):
        """
        Gets the ep of this EndpointData.
        Unique Device Management device ID.

        :return: The ep of this EndpointData.
        :rtype: str
        """
        return self._ep

    @ep.setter
    def ep(self, ep):
        """
        Sets the ep of this EndpointData.
        Unique Device Management device ID.

        :param ep: The ep of this EndpointData.
        :type: str
        """

        self._ep = ep

    @property
    def ept(self):
        """
        Gets the ept of this EndpointData.
        Endpoint type.

        :return: The ept of this EndpointData.
        :rtype: str
        """
        return self._ept

    @ept.setter
    def ept(self, ept):
        """
        Sets the ept of this EndpointData.
        Endpoint type.

        :param ept: The ept of this EndpointData.
        :type: str
        """

        self._ept = ept

    @property
    def original_ep(self):
        """
        Gets the original_ep of this EndpointData.
        In case of a self-provided endpoint name that is used to initiate the device registration, Device Management provides a new device ID to be used from that point on. The new Pelion platform provided Device ID is forwarded as the 'ep' property and the original self-provided one as the optional 'original-ep' property in a registration notification. The name and ID can then be mapped accordingly. Device Management saves the original endpoint name in the Device Directory for future device registrations so that you don't need to do the mapping again. 

        :return: The original_ep of this EndpointData.
        :rtype: str
        """
        return self._original_ep

    @original_ep.setter
    def original_ep(self, original_ep):
        """
        Sets the original_ep of this EndpointData.
        In case of a self-provided endpoint name that is used to initiate the device registration, Device Management provides a new device ID to be used from that point on. The new Pelion platform provided Device ID is forwarded as the 'ep' property and the original self-provided one as the optional 'original-ep' property in a registration notification. The name and ID can then be mapped accordingly. Device Management saves the original endpoint name in the Device Directory for future device registrations so that you don't need to do the mapping again. 

        :param original_ep: The original_ep of this EndpointData.
        :type: str
        """

        self._original_ep = original_ep

    @property
    def q(self):
        """
        Gets the q of this EndpointData.
        Queue mode (default value is false).

        :return: The q of this EndpointData.
        :rtype: bool
        """
        return self._q

    @q.setter
    def q(self, q):
        """
        Sets the q of this EndpointData.
        Queue mode (default value is false).

        :param q: The q of this EndpointData.
        :type: bool
        """

        self._q = q

    @property
    def resources(self):
        """
        Gets the resources of this EndpointData.

        :return: The resources of this EndpointData.
        :rtype: list[ResourcesData]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this EndpointData.

        :param resources: The resources of this EndpointData.
        :type: list[ResourcesData]
        """

        self._resources = resources

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
        if not isinstance(other, EndpointData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
