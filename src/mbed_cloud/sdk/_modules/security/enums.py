"""
Enum module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object

from mbed_cloud.sdk.common.enum import BaseEnum


class CertificateEnrollmentEnrollResultEnum(BaseEnum):
    """Represents the `CertificateEnrollmentEnrollResultEnum` options

    as used by Mbed Cloud "security" functionality
    """

    FAILURE = "failure"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    SUCCESS = "success"

    values = frozenset(("failure", "forbidden", "not_found", "success"))


class CertificateEnrollmentEnrollStatusEnum(BaseEnum):
    """Represents the `CertificateEnrollmentEnrollStatusEnum` options

    as used by Mbed Cloud "security" functionality
    """

    COMPLETED = "completed"
    NEW = "new"

    values = frozenset(("completed", "new"))


class CertificateIssuerIssuerTypeEnum(BaseEnum):
    """Represents the `CertificateIssuerIssuerTypeEnum` options

    as used by Mbed Cloud "security" functionality
    """

    CFSSL_AUTH = "CFSSL_AUTH"
    GLOBAL_SIGN = "GLOBAL_SIGN"

    values = frozenset(("CFSSL_AUTH", "GLOBAL_SIGN"))


class CertificateOrderEnum(BaseEnum):
    """Represents the `CertificateOrderEnum` options

    as used by Mbed Cloud "security" functionality
    """

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))


class CertificateServiceEnum(BaseEnum):
    """Represents the `CertificateServiceEnum` options

    as used by Mbed Cloud "security" functionality
    """

    BOOTSTRAP = "bootstrap"
    LWM2M = "lwm2m"

    values = frozenset(("bootstrap", "lwm2m"))


class CertificateStatusEnum(BaseEnum):
    """Represents the `CertificateStatusEnum` options

    as used by Mbed Cloud "security" functionality
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))
