# billing
This document contains the public REST API definitions of the mbed-billing service.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.4.4
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import billing 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import billing
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import billing
from billing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
billing.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# billing.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = billing.DefaultApi()
month = 'month_example' # str | Queried year and month of billing report

try:
    # Get billing report.
    api_response = api_instance.get_billing_report(month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_billing_report: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://mbed-billing.example.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_billing_report**](docs/DefaultApi.md#get_billing_report) | **GET** /v3/billing-report | Get billing report.
*DefaultApi* | [**get_billing_report_active_devices**](docs/DefaultApi.md#get_billing_report_active_devices) | **GET** /v3/billing-report-active-devices | Get raw active devices billing data for the month.
*DefaultApi* | [**get_billing_report_firmware_updates**](docs/DefaultApi.md#get_billing_report_firmware_updates) | **GET** /v3/billing-report-firmware-updates | Get raw firmware updates billing data for the month.
*DefaultApi* | [**get_service_package_quota**](docs/DefaultApi.md#get_service_package_quota) | **GET** /v3/service-packages-quota | Service package quota
*DefaultApi* | [**get_service_package_quota_history**](docs/DefaultApi.md#get_service_package_quota_history) | **GET** /v3/service-packages-quota-history | Service package quota history
*DefaultApi* | [**get_service_packages**](docs/DefaultApi.md#get_service_packages) | **GET** /v3/service-packages | Get all service packages.


## Documentation For Models

 - [ActiveServicePackage](docs/ActiveServicePackage.md)
 - [AggregatedQuotaUsageReport](docs/AggregatedQuotaUsageReport.md)
 - [BadRequestErrorResponse](docs/BadRequestErrorResponse.md)
 - [BadRequestErrorResponseField](docs/BadRequestErrorResponseField.md)
 - [ForbiddenErrorResponse](docs/ForbiddenErrorResponse.md)
 - [InternalServerErrorResponse](docs/InternalServerErrorResponse.md)
 - [PendingServicePackage](docs/PendingServicePackage.md)
 - [PreviousServicePackage](docs/PreviousServicePackage.md)
 - [QuotaUsageReport](docs/QuotaUsageReport.md)
 - [ReportAccountContactInfo](docs/ReportAccountContactInfo.md)
 - [ReportBillingData](docs/ReportBillingData.md)
 - [ReportNotFoundErrorResponse](docs/ReportNotFoundErrorResponse.md)
 - [ReportResponse](docs/ReportResponse.md)
 - [ServicePackageMetadata](docs/ServicePackageMetadata.md)
 - [ServicePackageQuota](docs/ServicePackageQuota.md)
 - [ServicePackageQuotaHistoryItem](docs/ServicePackageQuotaHistoryItem.md)
 - [ServicePackageQuotaHistoryReservation](docs/ServicePackageQuotaHistoryReservation.md)
 - [ServicePackageQuotaHistoryResponse](docs/ServicePackageQuotaHistoryResponse.md)
 - [ServicePackageQuotaHistoryServicePackage](docs/ServicePackageQuotaHistoryServicePackage.md)
 - [ServicePackageReport](docs/ServicePackageReport.md)
 - [ServicePackagesResponse](docs/ServicePackagesResponse.md)
 - [SubtenantAccountReport](docs/SubtenantAccountReport.md)
 - [SubtenantReportAccountContactInfo](docs/SubtenantReportAccountContactInfo.md)
 - [SubtenantServicePackageReport](docs/SubtenantServicePackageReport.md)
 - [UnauthorizedErrorResponse](docs/UnauthorizedErrorResponse.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


