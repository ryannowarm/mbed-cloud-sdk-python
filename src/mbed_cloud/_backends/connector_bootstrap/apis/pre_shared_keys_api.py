# coding: utf-8

"""
    Bootstrap API

    Bootstrap API allows web applications to control the device bootstrapping process.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class PreSharedKeysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_pre_shared_key(self, endpoint_name, **kwargs):  # noqa: E501
        """Remove a pre-shared key.  # noqa: E501

        Remove a pre-shared key.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" -X DELETE https://api.us-east-1.mbedcloud.com/v2/device-shared-keys/my-endpoint-0001 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_pre_shared_key(endpoint_name, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str endpoint_name: The unique endpoint identifier that this pre-shared key applies to. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.delete_pre_shared_key_with_http_info(endpoint_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_pre_shared_key_with_http_info(endpoint_name, **kwargs)  # noqa: E501
            return data

    def delete_pre_shared_key_with_http_info(self, endpoint_name, **kwargs):  # noqa: E501
        """Remove a pre-shared key.  # noqa: E501

        Remove a pre-shared key.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" -X DELETE https://api.us-east-1.mbedcloud.com/v2/device-shared-keys/my-endpoint-0001 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_pre_shared_key_with_http_info(endpoint_name, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str endpoint_name: The unique endpoint identifier that this pre-shared key applies to. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pre_shared_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params or
                params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `delete_pre_shared_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpoint_name'] = params['endpoint_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/device-shared-keys/{endpoint_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pre_shared_key(self, endpoint_name, **kwargs):  # noqa: E501
        """Get a pre-shared key.  # noqa: E501

        Check if a pre-shared key for an endpoint exists or not. The response does not contain the secret itself.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" https://api.us-east-1.mbedcloud.com/v2/device-shared-keys/my-endpoint-0001 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_pre_shared_key(endpoint_name, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str endpoint_name: The unique endpoint identifier that this pre-shared key applies to. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. (required)
        :return: PreSharedKeyWithoutSecret
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_pre_shared_key_with_http_info(endpoint_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pre_shared_key_with_http_info(endpoint_name, **kwargs)  # noqa: E501
            return data

    def get_pre_shared_key_with_http_info(self, endpoint_name, **kwargs):  # noqa: E501
        """Get a pre-shared key.  # noqa: E501

        Check if a pre-shared key for an endpoint exists or not. The response does not contain the secret itself.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" https://api.us-east-1.mbedcloud.com/v2/device-shared-keys/my-endpoint-0001 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_pre_shared_key_with_http_info(endpoint_name, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str endpoint_name: The unique endpoint identifier that this pre-shared key applies to. [Reserved characters](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) must be percent-encoded. (required)
        :return: PreSharedKeyWithoutSecret
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_name']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pre_shared_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_name' is set
        if ('endpoint_name' not in params or
                params['endpoint_name'] is None):
            raise ValueError("Missing the required parameter `endpoint_name` when calling `get_pre_shared_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpoint_name' in params:
            path_params['endpoint_name'] = params['endpoint_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/device-shared-keys/{endpoint_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PreSharedKeyWithoutSecret',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_pre_shared_keys(self, **kwargs):  # noqa: E501
        """List pre-shared keys.  # noqa: E501

        List pre-shared keys with pagination and default page size of 50 entries.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" https://api.us-east-1.mbedcloud.com/v2/device-shared-keys ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.list_pre_shared_keys(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int limit: The number of entries per page
        :param str after: An offset token for fetching a specific page. Provided by the server.
        :return: ListOfPreSharedKeysWithoutSecret
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.list_pre_shared_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_pre_shared_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_pre_shared_keys_with_http_info(self, **kwargs):  # noqa: E501
        """List pre-shared keys.  # noqa: E501

        List pre-shared keys with pagination and default page size of 50 entries.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" https://api.us-east-1.mbedcloud.com/v2/device-shared-keys ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.list_pre_shared_keys_with_http_info(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int limit: The number of entries per page
        :param str after: An offset token for fetching a specific page. Provided by the server.
        :return: ListOfPreSharedKeysWithoutSecret
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'after']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_pre_shared_keys" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/device-shared-keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListOfPreSharedKeysWithoutSecret',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_pre_shared_key(self, body, **kwargs):  # noqa: E501
        """Upload a pre-shared key to Pelion Device Management.  # noqa: E501

        Upload a pre-shared key (PSK) for an endpoint to allow it to bootstrap. The existing key will not be overwritten but needs to be deleted first in case of re-setting PSK for an endpoint.  **Note**: The PSK APIs are available only to accounts that have this feature enabled.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" -H \"content-type: application/json\" -X POST https://api.us-east-1.mbedcloud.com/v2/device-shared-keys \\      -d '{\"endpoint_name\": \"my-endpoint-0001\", \"secret_hex\": \"4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.upload_pre_shared_key(body, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param PreSharedKey body: Pre-shared key to be uploaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.upload_pre_shared_key_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_pre_shared_key_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upload_pre_shared_key_with_http_info(self, body, **kwargs):  # noqa: E501
        """Upload a pre-shared key to Pelion Device Management.  # noqa: E501

        Upload a pre-shared key (PSK) for an endpoint to allow it to bootstrap. The existing key will not be overwritten but needs to be deleted first in case of re-setting PSK for an endpoint.  **Note**: The PSK APIs are available only to accounts that have this feature enabled.  **Example usage:**  ``` curl -H \"authorization: Bearer ${API_TOKEN}\" -H \"content-type: application/json\" -X POST https://api.us-east-1.mbedcloud.com/v2/device-shared-keys \\      -d '{\"endpoint_name\": \"my-endpoint-0001\", \"secret_hex\": \"4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a\" }' ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.upload_pre_shared_key_with_http_info(body, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param PreSharedKey body: Pre-shared key to be uploaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_pre_shared_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upload_pre_shared_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v2/device-shared-keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
