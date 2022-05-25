# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.api_key_list_response import ApiKeyListResponse
from datadog_api_client.v1.model.api_key_response import ApiKeyResponse
from datadog_api_client.v1.model.api_key import ApiKey
from datadog_api_client.v1.model.application_key_list_response import ApplicationKeyListResponse
from datadog_api_client.v1.model.application_key_response import ApplicationKeyResponse
from datadog_api_client.v1.model.application_key import ApplicationKey


class KeyManagementApi:
    """
    Manage your Datadog API and application keys. You need an API key and
    an application key for a user with the required permissions to interact
    with these endpoints. The full list of API and application keys can be
    seen on your `Datadog API page <https://app.datadoghq.com/account/settings#api>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "create_api_key",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApiKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "create_application_key",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "delete_api_key",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "delete_application_key",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "get_api_key",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "get_application_key",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_api_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "list_api_keys",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "list_application_keys",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "update_api_key",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApiKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "update_application_key",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_api_key(self, body, **kwargs):
        """Create an API key.

        Creates an API key with a given name.

        :type body: ApiKey

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApiKeyResponse
        """
        kwargs["body"] = body

        return self._create_api_key_endpoint.call_with_http_info(**kwargs)

    def create_application_key(self, body, **kwargs):
        """Create an application key.

        Create an application key with a given name.

        :type body: ApplicationKey

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["body"] = body

        return self._create_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_api_key(self, key, **kwargs):
        """Delete an API key.

        Delete a given API key.

        :param key: The specific API key you are working with.
        :type key: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApiKeyResponse
        """
        kwargs["key"] = key

        return self._delete_api_key_endpoint.call_with_http_info(**kwargs)

    def delete_application_key(self, key, **kwargs):
        """Delete an application key.

        Delete a given application key.

        :param key: The specific APP key you are working with.
        :type key: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["key"] = key

        return self._delete_application_key_endpoint.call_with_http_info(**kwargs)

    def get_api_key(self, key, **kwargs):
        """Get API key.

        Get a given API key.

        :param key: The specific API key you are working with.
        :type key: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApiKeyResponse
        """
        kwargs["key"] = key

        return self._get_api_key_endpoint.call_with_http_info(**kwargs)

    def get_application_key(self, key, **kwargs):
        """Get an application key.

        Get a given application key.

        :param key: The specific APP key you are working with.
        :type key: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["key"] = key

        return self._get_application_key_endpoint.call_with_http_info(**kwargs)

    def list_api_keys(self, **kwargs):
        """Get all API keys.

        Get all API keys available for your account.


        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApiKeyListResponse
        """
        return self._list_api_keys_endpoint.call_with_http_info(**kwargs)

    def list_application_keys(self, **kwargs):
        """Get all application keys.

        Get all application keys available for your Datadog account.


        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyListResponse
        """
        return self._list_application_keys_endpoint.call_with_http_info(**kwargs)

    def update_api_key(self, key, body, **kwargs):
        """Edit an API key.

        Edit an API key name.

        :param key: The specific API key you are working with.
        :type key: str
        :type body: ApiKey

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApiKeyResponse
        """
        kwargs["key"] = key

        kwargs["body"] = body

        return self._update_api_key_endpoint.call_with_http_info(**kwargs)

    def update_application_key(self, key, body, **kwargs):
        """Edit an application key.

        Edit an application key name.

        :param key: The specific APP key you are working with.
        :type key: str
        :type body: ApplicationKey

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["key"] = key

        kwargs["body"] = body

        return self._update_application_key_endpoint.call_with_http_info(**kwargs)
