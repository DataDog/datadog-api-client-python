# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.open_ai_codex_integration_accounts_response import (
    OpenAICodexIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_response import OpenAICodexIntegrationAccountResponse
from datadog_api_client.v2.model.open_ai_codex_integration_account_create_request import (
    OpenAICodexIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_update_request import (
    OpenAICodexIntegrationAccountUpdateRequest,
)


class OpenAICodexIntegrationApi:
    """
    Manage your Datadog OpenAI Codex integration accounts and account resources
    directly through the Datadog API. See the
    `OpenAI Codex integration page <https://docs.datadoghq.com/integrations/openai-codex/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_open_ai_codex_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (OpenAICodexIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/openai-codex/accounts",
                "operation_id": "create_open_ai_codex_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OpenAICodexIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_open_ai_codex_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/openai-codex/accounts/{account_id}",
                "operation_id": "delete_open_ai_codex_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_open_ai_codex_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (OpenAICodexIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/openai-codex/accounts/{account_id}",
                "operation_id": "get_open_ai_codex_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_open_ai_codex_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (OpenAICodexIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/openai-codex/accounts",
                "operation_id": "list_open_ai_codex_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_open_ai_codex_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (OpenAICodexIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/openai-codex/accounts/{account_id}",
                "operation_id": "update_open_ai_codex_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OpenAICodexIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_open_ai_codex_integration_account(
        self,
        body: OpenAICodexIntegrationAccountCreateRequest,
    ) -> OpenAICodexIntegrationAccountResponse:
        """Create an OpenAI Codex integration account.

        Create an OpenAI Codex integration account.

        :type body: OpenAICodexIntegrationAccountCreateRequest
        :rtype: OpenAICodexIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_open_ai_codex_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_open_ai_codex_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete an OpenAI Codex integration account.

        Delete an OpenAI Codex integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_open_ai_codex_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_open_ai_codex_integration_account(
        self,
        account_id: str,
    ) -> OpenAICodexIntegrationAccountResponse:
        """Get an OpenAI Codex integration account.

        Get an OpenAI Codex integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: OpenAICodexIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_open_ai_codex_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_open_ai_codex_integration_accounts(
        self,
    ) -> OpenAICodexIntegrationAccountsResponse:
        """List OpenAI Codex integration accounts.

        List OpenAI Codex integration accounts.

        :rtype: OpenAICodexIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_open_ai_codex_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_open_ai_codex_integration_account(
        self,
        account_id: str,
        body: OpenAICodexIntegrationAccountUpdateRequest,
    ) -> OpenAICodexIntegrationAccountResponse:
        """Update an OpenAI Codex integration account.

        Update an OpenAI Codex integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: OpenAICodexIntegrationAccountUpdateRequest
        :rtype: OpenAICodexIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_open_ai_codex_integration_account_endpoint.call_with_http_info(**kwargs)
