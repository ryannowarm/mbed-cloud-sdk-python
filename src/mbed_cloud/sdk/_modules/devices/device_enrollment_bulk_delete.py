"""
Entity module

This file is auto-generated from API Specifications.
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class DeviceEnrollmentBulkDelete(Entity):
    """Represents the `DeviceEnrollmentBulkDelete` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "completed_at",
        "created_at",
        "errors_count",
        "errors_report_file",
        "full_report_file",
        "id",
        "processed_count",
        "status",
        "total_count",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        completed_at=None,
        created_at=None,
        errors_count=None,
        errors_report_file=None,
        full_report_file=None,
        id=None,
        processed_count=None,
        status=None,
        total_count=None,
    ):
        """Creates a local `DeviceEnrollmentBulkDelete` instance

        :param account_id: ID
        :type account_id: str
        :param completed_at: The time of completing the bulk creation task.
        :type completed_at: datetime
        :param created_at: The time of receiving the bulk creation task.
        :type created_at: datetime
        :param errors_count: The number of enrollment identities with failed processing.
        :type errors_count: int
        :param errors_report_file: 
        :type errors_report_file: str
        :param full_report_file: 
        :type full_report_file: str
        :param id: Bulk ID
        :type id: str
        :param processed_count: The number of enrollment identities processed until now.
        :type processed_count: int
        :param status: The state of the process is 'new' at the time of creation. If the
            creation is still in progress, the state is shown as 'processing'.
            When the request has been fully processed, the state changes to
            'completed'.
        :type status: str
        :param total_count: Total number of enrollment identities found in the input CSV.
        :type total_count: int
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._completed_at = fields.DateTimeField(value=completed_at)
        self._created_at = fields.DateTimeField(value=created_at)
        self._errors_count = fields.IntegerField(value=errors_count)
        self._errors_report_file = fields.StringField(value=errors_report_file)
        self._full_report_file = fields.StringField(value=full_report_file)
        self._id = fields.StringField(value=id)
        self._processed_count = fields.IntegerField(value=processed_count)
        self._status = fields.StringField(
            value=status, enum=enums.DeviceEnrollmentBulkDeleteStatusEnum
        )
        self._total_count = fields.IntegerField(value=total_count)

    @property
    def account_id(self):
        """ID
        
        api example: '00005a4e027f0a580a01081c00000000'
        
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
    def completed_at(self):
        """The time of completing the bulk creation task.
        
        :rtype: datetime
        """

        return self._completed_at.value

    @completed_at.setter
    def completed_at(self, value):
        """Set value of `completed_at`

        :param value: value to set
        :type value: datetime
        """

        self._completed_at.set(value)

    @property
    def created_at(self):
        """The time of receiving the bulk creation task.
        
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
    def errors_count(self):
        """The number of enrollment identities with failed processing.
        
        :rtype: int
        """

        return self._errors_count.value

    @errors_count.setter
    def errors_count(self, value):
        """Set value of `errors_count`

        :param value: value to set
        :type value: int
        """

        self._errors_count.set(value)

    @property
    def errors_report_file(self):
        """
        
        api example: 'https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-
            uploads/2d238a89038b4ddb84699dd36a901063/errors_report.csv'
        
        :rtype: str
        """

        return self._errors_report_file.value

    @errors_report_file.setter
    def errors_report_file(self, value):
        """Set value of `errors_report_file`

        :param value: value to set
        :type value: str
        """

        self._errors_report_file.set(value)

    @property
    def full_report_file(self):
        """
        
        api example: 'https://api.us-east-1.mbedcloud.com/v3/device-enrollments-bulk-
            uploads/2d238a89038b4ddb84699dd36a901063/full_report.csv'
        
        :rtype: str
        """

        return self._full_report_file.value

    @full_report_file.setter
    def full_report_file(self, value):
        """Set value of `full_report_file`

        :param value: value to set
        :type value: str
        """

        self._full_report_file.set(value)

    @property
    def id(self):
        """Bulk ID
        
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
    def processed_count(self):
        """The number of enrollment identities processed until now.
        
        :rtype: int
        """

        return self._processed_count.value

    @processed_count.setter
    def processed_count(self, value):
        """Set value of `processed_count`

        :param value: value to set
        :type value: int
        """

        self._processed_count.set(value)

    @property
    def status(self):
        """The state of the process is 'new' at the time of creation. If the creation is
        still in progress, the state is shown as 'processing'. When the request has
        been fully processed, the state changes to 'completed'.
        
        api example: 'new'
        
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
    def total_count(self):
        """Total number of enrollment identities found in the input CSV.
        
        api example: 10
        
        :rtype: int
        """

        return self._total_count.value

    @total_count.setter
    def total_count(self, value):
        """Set value of `total_count`

        :param value: value to set
        :type value: int
        """

        self._total_count.set(value)

    def delete(self, enrollment_identities):
        """Bulk delete

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/device-enrollments-bulk-deletes
        
        :param enrollment_identities: The `CSV` file containing the enrollment IDs. The maximum file size is
            10MB.
        :type enrollment_identities: file
        
        :rtype: DeviceEnrollmentBulkDelete
        """

        return self._client.call_api(
            method="post",
            path="/v3/device-enrollments-bulk-deletes",
            stream_params={
                "enrollment_identities": fields.FileField(
                    enrollment_identities
                ).to_api()
            },
            unpack=self,
        )

    def download_errors_report_file(self):
        """Download the error report file for the bulk enrollment deletion.

        
        
        :rtype: file
        """

        from mbed_cloud.sdk.common._custom_methods import download_errors_report_file

        return download_errors_report_file(self=self, foreign_key=self.__class__)

    def download_full_report_file(self):
        """Download the full report file for the bulk enrollment deletion.

        
        
        :rtype: file
        """

        from mbed_cloud.sdk.common._custom_methods import download_full_report_file

        return download_full_report_file(self=self, foreign_key=self.__class__)

    def get(self):
        """Get bulk delete entity

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/device-enrollments-bulk-deletes/{id}
        
        :rtype: DeviceEnrollmentBulkDelete
        """

        return self._client.call_api(
            method="get",
            path="/v3/device-enrollments-bulk-deletes/{id}",
            path_params={"id": self._id.to_api()},
            unpack=self,
        )