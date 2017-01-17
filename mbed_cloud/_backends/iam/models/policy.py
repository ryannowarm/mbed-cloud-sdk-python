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


class Policy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action=None, resource=None, allow=False):
        """
        Policy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'resource': 'str',
            'allow': 'bool'
        }

        self.attribute_map = {
            'action': 'action',
            'resource': 'resource',
            'allow': 'allow'
        }

        self._action = action
        self._resource = resource
        self._allow = allow

    @property
    def action(self):
        """
        Gets the action of this Policy.
        Comma separated list of actions, empty string represents all actions.

        :return: The action of this Policy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Policy.
        Comma separated list of actions, empty string represents all actions.

        :param action: The action of this Policy.
        :type: str
        """

        self._action = action

    @property
    def resource(self):
        """
        Gets the resource of this Policy.
        Resource that is protected by this policy.

        :return: The resource of this Policy.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this Policy.
        Resource that is protected by this policy.

        :param resource: The resource of this Policy.
        :type: str
        """

        self._resource = resource

    @property
    def allow(self):
        """
        Gets the allow of this Policy.
        True or false controlling whether an action is allowed or not.

        :return: The allow of this Policy.
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """
        Sets the allow of this Policy.
        True or false controlling whether an action is allowed or not.

        :param allow: The allow of this Policy.
        :type: bool
        """

        self._allow = allow

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other