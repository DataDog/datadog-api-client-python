# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.api_keys_response import APIKeysResponse
from datadog_api_client.v2.model.api_keys_sort import APIKeysSort
from datadog_api_client.v2.model.api_key_response import APIKeyResponse
from datadog_api_client.v2.model.api_key_create_request import APIKeyCreateRequest
from datadog_api_client.v2.model.api_key_update_request import APIKeyUpdateRequest
from datadog_api_client.v2.model.list_application_keys_response import ListApplicationKeysResponse
from datadog_api_client.v2.model.application_keys_sort import ApplicationKeysSort
from datadog_api_client.v2.model.application_key_response import ApplicationKeyResponse
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest


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
                "response_type": (APIKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/api_keys",
                "operation_id": "create_api_key",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (APIKeyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_current_user_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/current_user/application_keys",
                "operation_id": "create_current_user_application_key",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKeyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_api_key_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/api_keys/{api_key_id}",
                "operation_id": "delete_api_key",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "api_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "api_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_application_key_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/application_keys/{app_key_id}",
                "operation_id": "delete_application_key",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_current_user_application_key_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/current_user/application_keys/{app_key_id}",
                "operation_id": "delete_current_user_application_key",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (APIKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/api_keys/{api_key_id}",
                "operation_id": "get_api_key",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "api_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "api_key_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
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
                "endpoint_path": "/api/v2/application_keys/{app_key_id}",
                "operation_id": "get_application_key",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_current_user_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/current_user/application_keys/{app_key_id}",
                "operation_id": "get_current_user_application_key",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
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
                "response_type": (APIKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/api_keys",
                "operation_id": "list_api_keys",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (APIKeysSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_created_at_start": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][start]",
                    "location": "query",
                },
                "filter_created_at_end": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][end]",
                    "location": "query",
                },
                "filter_modified_at_start": {
                    "openapi_types": (str,),
                    "attribute": "filter[modified_at][start]",
                    "location": "query",
                },
                "filter_modified_at_end": {
                    "openapi_types": (str,),
                    "attribute": "filter[modified_at][end]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ListApplicationKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/application_keys",
                "operation_id": "list_application_keys",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (ApplicationKeysSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_created_at_start": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][start]",
                    "location": "query",
                },
                "filter_created_at_end": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][end]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_current_user_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ListApplicationKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/current_user/application_keys",
                "operation_id": "list_current_user_application_keys",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (ApplicationKeysSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_created_at_start": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][start]",
                    "location": "query",
                },
                "filter_created_at_end": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][end]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (APIKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/api_keys/{api_key_id}",
                "operation_id": "update_api_key",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "api_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "api_key_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (APIKeyUpdateRequest,),
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
                "endpoint_path": "/api/v2/application_keys/{app_key_id}",
                "operation_id": "update_application_key",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKeyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_current_user_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/current_user/application_keys/{app_key_id}",
                "operation_id": "update_current_user_application_key",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKeyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_api_key(self, body, **kwargs):
        """Create an API key.

        Create an API key.

        :type body: APIKeyCreateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: APIKeyResponse
        """
        kwargs["body"] = body

        return self._create_api_key_endpoint.call_with_http_info(**kwargs)

    def create_current_user_application_key(self, body, **kwargs):
        """Create an application key for current user.

        Create an application key for current user

        :type body: ApplicationKeyCreateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["body"] = body

        return self._create_current_user_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_api_key(self, api_key_id, **kwargs):
        """Delete an API key.

        Delete an API key.

        :param api_key_id: The ID of the API key.
        :type api_key_id: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs["api_key_id"] = api_key_id

        return self._delete_api_key_endpoint.call_with_http_info(**kwargs)

    def delete_application_key(self, app_key_id, **kwargs):
        """Delete an application key.

        Delete an application key

        :param app_key_id: The ID of the application key.
        :type app_key_id: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs["app_key_id"] = app_key_id

        return self._delete_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_current_user_application_key(self, app_key_id, **kwargs):
        """Delete an application key owned by current user.

        Delete an application key owned by current user

        :param app_key_id: The ID of the application key.
        :type app_key_id: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs["app_key_id"] = app_key_id

        return self._delete_current_user_application_key_endpoint.call_with_http_info(**kwargs)

    def get_api_key(self, api_key_id, **kwargs):
        """Get API key.

        Get an API key.

        :param api_key_id: The ID of the API key.
        :type api_key_id: str
        :param include: Comma separated list of resource paths for related resources to include in the response. Supported resource paths are ``created_by`` and ``modified_by``.
        :type include: str, optional

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: APIKeyResponse
        """
        kwargs["api_key_id"] = api_key_id

        return self._get_api_key_endpoint.call_with_http_info(**kwargs)

    def get_application_key(self, app_key_id, **kwargs):
        """Get an application key.

        Get an application key for your org.

        :param app_key_id: The ID of the application key.
        :type app_key_id: str
        :param include: Resource path for related resources to include in the response. Only ``owned_by`` is supported.
        :type include: str, optional

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["app_key_id"] = app_key_id

        return self._get_application_key_endpoint.call_with_http_info(**kwargs)

    def get_current_user_application_key(self, app_key_id, **kwargs):
        """Get one application key owned by current user.

        Get an application key owned by current user

        :param app_key_id: The ID of the application key.
        :type app_key_id: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["app_key_id"] = app_key_id

        return self._get_current_user_application_key_endpoint.call_with_http_info(**kwargs)

    def list_api_keys(self, **kwargs):
        """Get all API keys.

        List all API keys available for your account.

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: API key attribute used to sort results. Sort order is ascending
            by default. In order to specify a descending sort, prefix the
            attribute with a minus sign.
        :type sort: APIKeysSort, optional
        :param filter: Filter API keys by the specified string.
        :type filter: str, optional
        :param filter_created_at_start: Only include API keys created on or after the specified date.
        :type filter_created_at_start: str, optional
        :param filter_created_at_end: Only include API keys created on or before the specified date.
        :type filter_created_at_end: str, optional
        :param filter_modified_at_start: Only include API keys modified on or after the specified date.
        :type filter_modified_at_start: str, optional
        :param filter_modified_at_end: Only include API keys modified on or before the specified date.
        :type filter_modified_at_end: str, optional
        :param include: Comma separated list of resource paths for related resources to include in the response. Supported resource paths are ``created_by`` and ``modified_by``.
        :type include: str, optional

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: APIKeysResponse
        """
        return self._list_api_keys_endpoint.call_with_http_info(**kwargs)

    def list_application_keys(self, **kwargs):
        """Get all application keys.

        List all application keys available for your org

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Application key attribute used to sort results. Sort order is ascending
            by default. In order to specify a descending sort, prefix the
            attribute with a minus sign.
        :type sort: ApplicationKeysSort, optional
        :param filter: Filter application keys by the specified string.
        :type filter: str, optional
        :param filter_created_at_start: Only include application keys created on or after the specified date.
        :type filter_created_at_start: str, optional
        :param filter_created_at_end: Only include application keys created on or before the specified date.
        :type filter_created_at_end: str, optional

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ListApplicationKeysResponse
        """
        return self._list_application_keys_endpoint.call_with_http_info(**kwargs)

    def list_current_user_application_keys(self, **kwargs):
        """Get all application keys owned by current user.

        List all application keys available for current user

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Application key attribute used to sort results. Sort order is ascending
            by default. In order to specify a descending sort, prefix the
            attribute with a minus sign.
        :type sort: ApplicationKeysSort, optional
        :param filter: Filter application keys by the specified string.
        :type filter: str, optional
        :param filter_created_at_start: Only include application keys created on or after the specified date.
        :type filter_created_at_start: str, optional
        :param filter_created_at_end: Only include application keys created on or before the specified date.
        :type filter_created_at_end: str, optional

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ListApplicationKeysResponse
        """
        return self._list_current_user_application_keys_endpoint.call_with_http_info(**kwargs)

    def update_api_key(self, api_key_id, body, **kwargs):
        """Edit an API key.

        Update an API key.

        :param api_key_id: The ID of the API key.
        :type api_key_id: str
        :type body: APIKeyUpdateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: APIKeyResponse
        """
        kwargs["api_key_id"] = api_key_id

        kwargs["body"] = body

        return self._update_api_key_endpoint.call_with_http_info(**kwargs)

    def update_application_key(self, app_key_id, body, **kwargs):
        """Edit an application key.

        Edit an application key

        :param app_key_id: The ID of the application key.
        :type app_key_id: str
        :type body: ApplicationKeyUpdateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["app_key_id"] = app_key_id

        kwargs["body"] = body

        return self._update_application_key_endpoint.call_with_http_info(**kwargs)

    def update_current_user_application_key(self, app_key_id, body, **kwargs):
        """Edit an application key owned by current user.

        Edit an application key owned by current user

        :param app_key_id: The ID of the application key.
        :type app_key_id: str
        :type body: ApplicationKeyUpdateRequest

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: ApplicationKeyResponse
        """
        kwargs["app_key_id"] = app_key_id

        kwargs["body"] = body

        return self._update_current_user_application_key_endpoint.call_with_http_info(**kwargs)
