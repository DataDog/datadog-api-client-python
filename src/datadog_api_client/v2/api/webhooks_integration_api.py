# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.webhooks_auth_methods_response import WebhooksAuthMethodsResponse
from datadog_api_client.v2.model.webhooks_auth_method_protocol import WebhooksAuthMethodProtocol
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response import (
    WebhooksOAuth2ClientCredentialsResponse,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_create_request import (
    WebhooksOAuth2ClientCredentialsCreateRequest,
)
from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_request import (
    WebhooksOAuth2ClientCredentialsUpdateRequest,
)


class WebhooksIntegrationApi:
    """
    Configure your `Datadog Webhooks integration <https://docs.datadoghq.com/integrations/webhooks/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_o_auth2_client_credentials_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksOAuth2ClientCredentialsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/webhooks/configuration/auth-method/oauth2-client-credentials",
                "operation_id": "create_o_auth2_client_credentials",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksOAuth2ClientCredentialsCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_o_auth2_client_credentials_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/webhooks/configuration/auth-method/oauth2-client-credentials/{auth_method_id}",
                "operation_id": "delete_o_auth2_client_credentials",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "auth_method_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "auth_method_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_all_auth_methods_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksAuthMethodsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/webhooks/configuration/auth-method",
                "operation_id": "get_all_auth_methods",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (WebhooksAuthMethodProtocol,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_o_auth2_client_credentials_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksOAuth2ClientCredentialsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/webhooks/configuration/auth-method/oauth2-client-credentials/{auth_method_id}",
                "operation_id": "get_o_auth2_client_credentials",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "auth_method_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "auth_method_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_o_auth2_client_credentials_endpoint = _Endpoint(
            settings={
                "response_type": (WebhooksOAuth2ClientCredentialsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/webhooks/configuration/auth-method/oauth2-client-credentials/{auth_method_id}",
                "operation_id": "update_o_auth2_client_credentials",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "auth_method_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "auth_method_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WebhooksOAuth2ClientCredentialsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_o_auth2_client_credentials(
        self,
        body: WebhooksOAuth2ClientCredentialsCreateRequest,
    ) -> WebhooksOAuth2ClientCredentialsResponse:
        """Create an OAuth2 client credentials auth method.

        Create a new OAuth2 client credentials auth method for the Webhooks
        integration. The ``client_secret`` is stored securely and never returned.

        :param body: OAuth2 client credentials payload.
        :type body: WebhooksOAuth2ClientCredentialsCreateRequest
        :rtype: WebhooksOAuth2ClientCredentialsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_o_auth2_client_credentials_endpoint.call_with_http_info(**kwargs)

    def delete_o_auth2_client_credentials(
        self,
        auth_method_id: str,
    ) -> None:
        """Delete an OAuth2 client credentials auth method.

        Delete an OAuth2 client credentials auth method by ID.

        :param auth_method_id: The UUID of the auth method.
        :type auth_method_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["auth_method_id"] = auth_method_id

        return self._delete_o_auth2_client_credentials_endpoint.call_with_http_info(**kwargs)

    def get_all_auth_methods(
        self,
        *,
        include: Union[WebhooksAuthMethodProtocol, UnsetType] = unset,
    ) -> WebhooksAuthMethodsResponse:
        """Get all auth methods.

        Get a list of all auth methods configured for the Webhooks integration in
        your organization.

        :param include: Comma-separated list of relationships to include in the response.
        :type include: WebhooksAuthMethodProtocol, optional
        :rtype: WebhooksAuthMethodsResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        return self._get_all_auth_methods_endpoint.call_with_http_info(**kwargs)

    def get_o_auth2_client_credentials(
        self,
        auth_method_id: str,
    ) -> WebhooksOAuth2ClientCredentialsResponse:
        """Get an OAuth2 client credentials auth method.

        Get a single OAuth2 client credentials auth method by ID.

        :param auth_method_id: The UUID of the auth method.
        :type auth_method_id: str
        :rtype: WebhooksOAuth2ClientCredentialsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["auth_method_id"] = auth_method_id

        return self._get_o_auth2_client_credentials_endpoint.call_with_http_info(**kwargs)

    def update_o_auth2_client_credentials(
        self,
        auth_method_id: str,
        body: WebhooksOAuth2ClientCredentialsUpdateRequest,
    ) -> WebhooksOAuth2ClientCredentialsResponse:
        """Update an OAuth2 client credentials auth method.

        Update an existing OAuth2 client credentials auth method.

        :param auth_method_id: The UUID of the auth method.
        :type auth_method_id: str
        :param body: OAuth2 client credentials payload.
        :type body: WebhooksOAuth2ClientCredentialsUpdateRequest
        :rtype: WebhooksOAuth2ClientCredentialsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["auth_method_id"] = auth_method_id

        kwargs["body"] = body

        return self._update_o_auth2_client_credentials_endpoint.call_with_http_info(**kwargs)
