# coding: utf-8

"""
    Provisioning endpoints - production line certificates.

    A producton line certificate is used to associate a specific installation of the Factory Tool with an mbed Cloud account.  The production line certificate is generated by the Factory Tool, and needs to be uploaded using these APIs. 

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Body(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comment=None, production_line_certificate=None):
        """
        Body - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comment': 'str',
            'production_line_certificate': 'str'
        }

        self.attribute_map = {
            'comment': 'comment',
            'production_line_certificate': 'production-line-certificate'
        }

        self._comment = comment
        self._production_line_certificate = production_line_certificate

    @property
    def comment(self):
        """
        Gets the comment of this Body.
        Comment of the production line certificate (max length is 256 characters).

        :return: The comment of this Body.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Body.
        Comment of the production line certificate (max length is 256 characters).

        :param comment: The comment of this Body.
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")

        self._comment = comment

    @property
    def production_line_certificate(self):
        """
        Gets the production_line_certificate of this Body.
        Production line certificate public key (from the Factory Tool, raw format - 65 bytes, Base64 encoded).

        :return: The production_line_certificate of this Body.
        :rtype: str
        """
        return self._production_line_certificate

    @production_line_certificate.setter
    def production_line_certificate(self, production_line_certificate):
        """
        Sets the production_line_certificate of this Body.
        Production line certificate public key (from the Factory Tool, raw format - 65 bytes, Base64 encoded).

        :param production_line_certificate: The production_line_certificate of this Body.
        :type: str
        """
        if production_line_certificate is None:
            raise ValueError("Invalid value for `production_line_certificate`, must not be `None`")

        self._production_line_certificate = production_line_certificate

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