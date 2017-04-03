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


class TrustedCertificateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, signature=None, cert_data=None, name=None, service=None, description=None):
        """
        TrustedCertificateReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'signature': 'str',
            'cert_data': 'str',
            'name': 'str',
            'service': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'signature': 'signature',
            'cert_data': 'cert_data',
            'name': 'name',
            'service': 'service',
            'description': 'description'
        }

        self._signature = signature
        self._cert_data = cert_data
        self._name = name
        self._service = service
        self._description = description

    @property
    def signature(self):
        """
        Gets the signature of this TrustedCertificateReq.
        Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256.

        :return: The signature of this TrustedCertificateReq.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this TrustedCertificateReq.
        Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256.

        :param signature: The signature of this TrustedCertificateReq.
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")

        self._signature = signature

    @property
    def cert_data(self):
        """
        Gets the cert_data of this TrustedCertificateReq.
        X509.v3 trusted certificate in PEM or base64 encoded DER format.

        :return: The cert_data of this TrustedCertificateReq.
        :rtype: str
        """
        return self._cert_data

    @cert_data.setter
    def cert_data(self, cert_data):
        """
        Sets the cert_data of this TrustedCertificateReq.
        X509.v3 trusted certificate in PEM or base64 encoded DER format.

        :param cert_data: The cert_data of this TrustedCertificateReq.
        :type: str
        """
        if cert_data is None:
            raise ValueError("Invalid value for `cert_data`, must not be `None`")

        self._cert_data = cert_data

    @property
    def name(self):
        """
        Gets the name of this TrustedCertificateReq.
        Certificate name.

        :return: The name of this TrustedCertificateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TrustedCertificateReq.
        Certificate name.

        :param name: The name of this TrustedCertificateReq.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def service(self):
        """
        Gets the service of this TrustedCertificateReq.
        Service name where the certificate must be used.

        :return: The service of this TrustedCertificateReq.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this TrustedCertificateReq.
        Service name where the certificate must be used.

        :param service: The service of this TrustedCertificateReq.
        :type: str
        """
        allowed_values = ["lwm2m", "bootstrap"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def description(self):
        """
        Gets the description of this TrustedCertificateReq.
        Human readable description of this certificate.

        :return: The description of this TrustedCertificateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TrustedCertificateReq.
        Human readable description of this certificate.

        :param description: The description of this TrustedCertificateReq.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, TrustedCertificateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
