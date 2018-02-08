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


class TrustedCertificateRootReq(object):
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
        'status': 'str',
        'enrollment_mode': 'bool',
        'certificate': 'str',
        'name': 'str',
        'service': 'str',
        'signature': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'enrollment_mode': 'enrollment_mode',
        'certificate': 'certificate',
        'name': 'name',
        'service': 'service',
        'signature': 'signature',
        'description': 'description'
    }

    def __init__(self, status=None, enrollment_mode=None, certificate=None, name=None, service=None, signature=None, description=None):
        """
        TrustedCertificateRootReq - a model defined in Swagger
        """

        self._status = status
        self._enrollment_mode = enrollment_mode
        self._certificate = certificate
        self._name = name
        self._service = service
        self._signature = signature
        self._description = description
        self.discriminator = None

    @property
    def status(self):
        """
        Gets the status of this TrustedCertificateRootReq.
        Status of the certificate.

        :return: The status of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TrustedCertificateRootReq.
        Status of the certificate.

        :param status: The status of this TrustedCertificateRootReq.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def enrollment_mode(self):
        """
        Gets the enrollment_mode of this TrustedCertificateRootReq.
        If true, signature parameter is not required. Default value is false.

        :return: The enrollment_mode of this TrustedCertificateRootReq.
        :rtype: bool
        """
        return self._enrollment_mode

    @enrollment_mode.setter
    def enrollment_mode(self, enrollment_mode):
        """
        Sets the enrollment_mode of this TrustedCertificateRootReq.
        If true, signature parameter is not required. Default value is false.

        :param enrollment_mode: The enrollment_mode of this TrustedCertificateRootReq.
        :type: bool
        """

        self._enrollment_mode = enrollment_mode

    @property
    def certificate(self):
        """
        Gets the certificate of this TrustedCertificateRootReq.
        X509.v3 trusted certificate in PEM format.

        :return: The certificate of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this TrustedCertificateRootReq.
        X509.v3 trusted certificate in PEM format.

        :param certificate: The certificate of this TrustedCertificateRootReq.
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")

        self._certificate = certificate

    @property
    def name(self):
        """
        Gets the name of this TrustedCertificateRootReq.
        Certificate name, not longer than 100 characters.

        :return: The name of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TrustedCertificateRootReq.
        Certificate name, not longer than 100 characters.

        :param name: The name of this TrustedCertificateRootReq.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def service(self):
        """
        Gets the service of this TrustedCertificateRootReq.
        Service name where the certificate must be used.

        :return: The service of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this TrustedCertificateRootReq.
        Service name where the certificate must be used.

        :param service: The service of this TrustedCertificateRootReq.
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")
        allowed_values = ["lwm2m", "bootstrap"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def signature(self):
        """
        Gets the signature of this TrustedCertificateRootReq.
        Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256. Optional if enrollment_mode is 'true'.

        :return: The signature of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this TrustedCertificateRootReq.
        Base64 encoded signature of the account ID signed by the certificate to be uploaded. Signature must be hashed with SHA256. Optional if enrollment_mode is 'true'.

        :param signature: The signature of this TrustedCertificateRootReq.
        :type: str
        """

        self._signature = signature

    @property
    def description(self):
        """
        Gets the description of this TrustedCertificateRootReq.
        Human readable description of this certificate, not longer than 500 characters.

        :return: The description of this TrustedCertificateRootReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TrustedCertificateRootReq.
        Human readable description of this certificate, not longer than 500 characters.

        :param description: The description of this TrustedCertificateRootReq.
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
        if not isinstance(other, TrustedCertificateRootReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
