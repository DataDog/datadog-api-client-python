# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v1.model.api_key_list_response import ApiKeyListResponse
from datadog_api_client.v1.model.api_key_response import ApiKeyResponse
from datadog_api_client.v1.model.api_key import ApiKey
from datadog_api_client.v1.model.application_key_list_response import ApplicationKeyListResponse
from datadog_api_client.v1.model.application_key_response import ApplicationKeyResponse
from datadog_api_client.v1.model.application_key import ApplicationKey


class KeyManagementApi:
    """
    Manage your Datadog API and application keys. You need an API key and an
    application key for a user with the required permissions to interact with these endpoints.

    Consult the following pages to view and manage your keys:

    * `API Keys <https://app.datadoghq.com/organization-settings/api-keys>`_
    * `Application Keys <https://app.datadoghq.com/personal-settings/application-keys>`_
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "create_api_key",
                "http_method": "POST",
                "version": "v1",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "create_application_key",
                "http_method": "POST",
                "version": "v1",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "delete_api_key",
                "http_method": "DELETE",
                "version": "v1",
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
            },
            api_client=api_client,
        )

        self._delete_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "delete_application_key",
                "http_method": "DELETE",
                "version": "v1",
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
            },
            api_client=api_client,
        )

        self._get_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "get_api_key",
                "http_method": "GET",
                "version": "v1",
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
            },
            api_client=api_client,
        )

        self._get_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "get_application_key",
                "http_method": "GET",
                "version": "v1",
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
            },
            api_client=api_client,
        )

        self._list_api_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/api_key",
                "operation_id": "list_api_keys",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/application_key",
                "operation_id": "list_application_keys",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_api_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApiKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/api_key/{key}",
                "operation_id": "update_api_key",
                "http_method": "PUT",
                "version": "v1",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/application_key/{key}",
                "operation_id": "update_application_key",
                "http_method": "PUT",
                "version": "v1",
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

    def create_api_key(
        self,
        body: ApiKey,
    ) -> ApiKeyResponse:
        """Create an API key. **Deprecated**.

        This endpoint is deprecated. Use `Create an API key <https://docs.datadoghq.com/api/latest/key-management/#create-an-api-key>`_ ( ``POST /api/v2/api_keys`` ) instead.

        Creates an API key with a given name.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :type body: ApiKey
        :rtype: ApiKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        warnings.warn("create_api_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._create_api_key_endpoint.call_with_http_info(**kwargs)

    def create_application_key(
        self,
        body: ApplicationKey,
    ) -> ApplicationKeyResponse:
        """Create an application key. **Deprecated**.

        This endpoint is deprecated. Use `Create an application key for current user <https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key-for-current-user>`_ ( ``POST /api/v2/current_user/application_keys`` ) instead.

        Create an application key with a given name.
        This endpoint is disabled for organizations in `One-Time Read mode <https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode>`_.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :type body: ApplicationKey
        :rtype: ApplicationKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        warnings.warn("create_application_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._create_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_api_key(
        self,
        key: str,
    ) -> ApiKeyResponse:
        """Delete an API key. **Deprecated**.

        This endpoint is deprecated. Use `Delete an API key <https://docs.datadoghq.com/api/latest/key-management/#delete-an-api-key>`_ ( ``DELETE /api/v2/api_keys/{api_key_id}`` ) instead.

        Delete a given API key.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific API key you are working with.
        :type key: str
        :rtype: ApiKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        warnings.warn("delete_api_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._delete_api_key_endpoint.call_with_http_info(**kwargs)

    def delete_application_key(
        self,
        key: str,
    ) -> ApplicationKeyResponse:
        """Delete an application key. **Deprecated**.

        This endpoint is deprecated. To delete your own application key, use
        `Delete an application key owned by current user <https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key-owned-by-current-user>`_
        ( ``DELETE /api/v2/current_user/application_keys/{app_key_id}`` ), which requires the ``user_app_keys`` permission.
        To delete an application key for your organization, use
        `Delete an application key <https://docs.datadoghq.com/api/latest/key-management/#delete-an-application-key>`_
        ( ``DELETE /api/v2/application_keys/{app_key_id}`` ), which requires the ``org_app_keys_write`` permission.

        Delete a given application key.
        This endpoint is disabled for organizations in `One-Time Read mode <https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode>`_.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific APP key you are working with.
        :type key: str
        :rtype: ApplicationKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        warnings.warn("delete_application_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._delete_application_key_endpoint.call_with_http_info(**kwargs)

    def get_api_key(
        self,
        key: str,
    ) -> ApiKeyResponse:
        """Get API key. **Deprecated**.

        This endpoint is deprecated. Use `Get API key <https://docs.datadoghq.com/api/latest/key-management/#get-api-key>`_ ( ``GET /api/v2/api_keys/{api_key_id}`` ) instead.

        Get a given API key.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific API key you are working with.
        :type key: str
        :rtype: ApiKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        warnings.warn("get_api_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._get_api_key_endpoint.call_with_http_info(**kwargs)

    def get_application_key(
        self,
        key: str,
    ) -> ApplicationKeyResponse:
        """Get an application key. **Deprecated**.

        This endpoint is deprecated. To get your own application key, use
        `Get one application key owned by current user <https://docs.datadoghq.com/api/latest/key-management/#get-one-application-key-owned-by-current-user>`_
        ( ``GET /api/v2/current_user/application_keys/{app_key_id}`` ), which requires the ``user_app_keys`` permission.
        To get an application key for your organization, use
        `Get an application key <https://docs.datadoghq.com/api/latest/key-management/#get-an-application-key>`_
        ( ``GET /api/v2/application_keys/{app_key_id}`` ), which requires the ``org_app_keys_read`` permission.

        Get a given application key.
        This endpoint is disabled for organizations in `One-Time Read mode <https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode>`_.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific APP key you are working with.
        :type key: str
        :rtype: ApplicationKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        warnings.warn("get_application_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._get_application_key_endpoint.call_with_http_info(**kwargs)

    def list_api_keys(
        self,
    ) -> ApiKeyListResponse:
        """Get all API keys. **Deprecated**.

        This endpoint is deprecated. Use `Get all API keys <https://docs.datadoghq.com/api/latest/key-management/#get-all-api-keys>`_ ( ``GET /api/v2/api_keys`` ) instead.

        Get all API keys available for your account.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :rtype: ApiKeyListResponse
        """
        kwargs: Dict[str, Any] = {}
        warnings.warn("list_api_keys is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_api_keys_endpoint.call_with_http_info(**kwargs)

    def list_application_keys(
        self,
    ) -> ApplicationKeyListResponse:
        """Get all application keys. **Deprecated**.

        This endpoint is deprecated. To list your own application keys, use
        `Get all application keys owned by current user <https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys-owned-by-current-user>`_
        ( ``GET /api/v2/current_user/application_keys`` ), which requires the ``user_app_keys`` permission.
        To list application keys across your organization, use
        `Get all application keys <https://docs.datadoghq.com/api/latest/key-management/#get-all-application-keys>`_
        ( ``GET /api/v2/application_keys`` ), which requires the ``org_app_keys_read`` permission.

        Get all application keys available for your Datadog account.
        This endpoint is disabled for organizations in `One-Time Read mode <https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode>`_.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :rtype: ApplicationKeyListResponse
        """
        kwargs: Dict[str, Any] = {}
        warnings.warn("list_application_keys is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_application_keys_endpoint.call_with_http_info(**kwargs)

    def update_api_key(
        self,
        key: str,
        body: ApiKey,
    ) -> ApiKeyResponse:
        """Edit an API key. **Deprecated**.

        This endpoint is deprecated. Use `Edit an API key <https://docs.datadoghq.com/api/latest/key-management/#edit-an-api-key>`_ ( ``PATCH /api/v2/api_keys/{api_key_id}`` ) instead.

        Edit an API key name.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific API key you are working with.
        :type key: str
        :type body: ApiKey
        :rtype: ApiKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        kwargs["body"] = body

        warnings.warn("update_api_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._update_api_key_endpoint.call_with_http_info(**kwargs)

    def update_application_key(
        self,
        key: str,
        body: ApplicationKey,
    ) -> ApplicationKeyResponse:
        """Edit an application key. **Deprecated**.

        This endpoint is deprecated. To edit your own application key, use
        `Edit an application key owned by current user <https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key-owned-by-current-user>`_
        ( ``PATCH /api/v2/current_user/application_keys/{app_key_id}`` ), which requires the ``user_app_keys`` permission.
        To edit an application key for your organization, use
        `Edit an application key <https://docs.datadoghq.com/api/latest/key-management/#edit-an-application-key>`_
        ( ``PATCH /api/v2/application_keys/{app_key_id}`` ), which requires the ``org_app_keys_write`` permission.

        Edit an application key name.
        This endpoint is disabled for organizations in `One-Time Read mode <https://docs.datadoghq.com/account_management/api-app-keys/#one-time-read-mode>`_.

        **Note** : This endpoint is disabled for the Government sites (US1-FED and US2-FED). Use the `V2 Key Management <https://docs.datadoghq.com/api/latest/key-management/>`_ endpoints instead.

        :param key: The specific APP key you are working with.
        :type key: str
        :type body: ApplicationKey
        :rtype: ApplicationKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["key"] = key

        kwargs["body"] = body

        warnings.warn("update_application_key is deprecated", DeprecationWarning, stacklevel=2)
        return self._update_application_key_endpoint.call_with_http_info(**kwargs)
