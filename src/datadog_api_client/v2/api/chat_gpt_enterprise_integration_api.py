# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_accounts_response import (
    ChatGPTEnterpriseIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_response import (
    ChatGPTEnterpriseIntegrationAccountResponse,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_create_request import (
    ChatGPTEnterpriseIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_update_request import (
    ChatGPTEnterpriseIntegrationAccountUpdateRequest,
)


class ChatGPTEnterpriseIntegrationApi:
    """
    Manage your Datadog ChatGPT Enterprise integration accounts and account resources
    directly through the Datadog API. See the
    `ChatGPT Enterprise integration page <https://docs.datadoghq.com/integrations/chatgpt-enterprise/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_chat_gpt_enterprise_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ChatGPTEnterpriseIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/chatgpt-enterprise/accounts",
                "operation_id": "create_chat_gpt_enterprise_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ChatGPTEnterpriseIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_chat_gpt_enterprise_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/chatgpt-enterprise/accounts/{account_id}",
                "operation_id": "delete_chat_gpt_enterprise_integration_account",
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

        self._get_chat_gpt_enterprise_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ChatGPTEnterpriseIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/chatgpt-enterprise/accounts/{account_id}",
                "operation_id": "get_chat_gpt_enterprise_integration_account",
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

        self._list_chat_gpt_enterprise_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (ChatGPTEnterpriseIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/chatgpt-enterprise/accounts",
                "operation_id": "list_chat_gpt_enterprise_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_chat_gpt_enterprise_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ChatGPTEnterpriseIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/chatgpt-enterprise/accounts/{account_id}",
                "operation_id": "update_chat_gpt_enterprise_integration_account",
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
                    "openapi_types": (ChatGPTEnterpriseIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_chat_gpt_enterprise_integration_account(
        self,
        body: ChatGPTEnterpriseIntegrationAccountCreateRequest,
    ) -> ChatGPTEnterpriseIntegrationAccountResponse:
        """Create a ChatGPT Enterprise integration account.

        Create a ChatGPT Enterprise integration account.

        :type body: ChatGPTEnterpriseIntegrationAccountCreateRequest
        :rtype: ChatGPTEnterpriseIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_chat_gpt_enterprise_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_chat_gpt_enterprise_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a ChatGPT Enterprise integration account.

        Delete a ChatGPT Enterprise integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_chat_gpt_enterprise_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_chat_gpt_enterprise_integration_account(
        self,
        account_id: str,
    ) -> ChatGPTEnterpriseIntegrationAccountResponse:
        """Get a ChatGPT Enterprise integration account.

        Get a ChatGPT Enterprise integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: ChatGPTEnterpriseIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_chat_gpt_enterprise_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_chat_gpt_enterprise_integration_accounts(
        self,
    ) -> ChatGPTEnterpriseIntegrationAccountsResponse:
        """List ChatGPT Enterprise integration accounts.

        List ChatGPT Enterprise integration accounts.

        :rtype: ChatGPTEnterpriseIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_chat_gpt_enterprise_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_chat_gpt_enterprise_integration_account(
        self,
        account_id: str,
        body: ChatGPTEnterpriseIntegrationAccountUpdateRequest,
    ) -> ChatGPTEnterpriseIntegrationAccountResponse:
        """Update a ChatGPT Enterprise integration account.

        Update a ChatGPT Enterprise integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: ChatGPTEnterpriseIntegrationAccountUpdateRequest
        :rtype: ChatGPTEnterpriseIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_chat_gpt_enterprise_integration_account_endpoint.call_with_http_info(**kwargs)
