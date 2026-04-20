# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.secure_embed_create_response import SecureEmbedCreateResponse
from datadog_api_client.v2.model.secure_embed_create_request import SecureEmbedCreateRequest
from datadog_api_client.v2.model.secure_embed_get_response import SecureEmbedGetResponse
from datadog_api_client.v2.model.secure_embed_update_response import SecureEmbedUpdateResponse
from datadog_api_client.v2.model.secure_embed_update_request import SecureEmbedUpdateRequest


class DashboardSecureEmbedApi:
    """
    Manage securely embedded Datadog dashboards. Secure embeds use HMAC-SHA256 signed sessions
    for authentication, enabling customers to embed dashboards in their own applications with
    server-side auth control. Unlike public dashboards (open URL) or invite dashboards
    (email-based access), secure embeds provide programmatic access control.

    **Requirements:**

    * **Embed** sharing must be enabled under **Organization Settings** > **Public Sharing** > **Shared Dashboards**.
    * You need `an API key and an application key <https://docs.datadoghq.com/account_management/api-app-keys/>`_ to interact with these endpoints.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_dashboard_secure_embed_endpoint = _Endpoint(
            settings={
                "response_type": (SecureEmbedCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboard/{dashboard_id}/shared/secure-embed",
                "operation_id": "create_dashboard_secure_embed",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecureEmbedCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_secure_embed_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboard/{dashboard_id}/shared/secure-embed/{token}",
                "operation_id": "delete_dashboard_secure_embed",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "token": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "token",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_dashboard_secure_embed_endpoint = _Endpoint(
            settings={
                "response_type": (SecureEmbedGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboard/{dashboard_id}/shared/secure-embed/{token}",
                "operation_id": "get_dashboard_secure_embed",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "token": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "token",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_dashboard_secure_embed_endpoint = _Endpoint(
            settings={
                "response_type": (SecureEmbedUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboard/{dashboard_id}/shared/secure-embed/{token}",
                "operation_id": "update_dashboard_secure_embed",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "token": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "token",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecureEmbedUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dashboard_secure_embed(
        self,
        dashboard_id: str,
        body: SecureEmbedCreateRequest,
    ) -> SecureEmbedCreateResponse:
        """Create a secure embed for a dashboard.

        Create a secure embed share for a dashboard. The response includes a one-time ``credential`` used for HMAC-SHA256 signing. Store it securely — it cannot be retrieved again.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param body: Secure embed creation request body.
        :type body: SecureEmbedCreateRequest
        :rtype: SecureEmbedCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["body"] = body

        return self._create_dashboard_secure_embed_endpoint.call_with_http_info(**kwargs)

    def delete_dashboard_secure_embed(
        self,
        dashboard_id: str,
        token: str,
    ) -> None:
        """Delete a secure embed for a dashboard.

        Delete a secure embed share for a dashboard.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param token: The share token identifying the secure embed.
        :type token: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["token"] = token

        return self._delete_dashboard_secure_embed_endpoint.call_with_http_info(**kwargs)

    def get_dashboard_secure_embed(
        self,
        dashboard_id: str,
        token: str,
    ) -> SecureEmbedGetResponse:
        """Get a secure embed for a dashboard.

        Retrieve an existing secure embed configuration for a dashboard.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param token: The share token identifying the secure embed.
        :type token: str
        :rtype: SecureEmbedGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["token"] = token

        return self._get_dashboard_secure_embed_endpoint.call_with_http_info(**kwargs)

    def update_dashboard_secure_embed(
        self,
        dashboard_id: str,
        token: str,
        body: SecureEmbedUpdateRequest,
    ) -> SecureEmbedUpdateResponse:
        """Update a secure embed for a dashboard.

        Partially update a secure embed configuration. All fields are optional (PATCH semantics).

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param token: The share token identifying the secure embed.
        :type token: str
        :param body: Secure embed update request body.
        :type body: SecureEmbedUpdateRequest
        :rtype: SecureEmbedUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["token"] = token

        kwargs["body"] = body

        return self._update_dashboard_secure_embed_endpoint.call_with_http_info(**kwargs)
