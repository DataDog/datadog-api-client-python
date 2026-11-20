# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.claude_compliance_integration_accounts_response import (
    ClaudeComplianceIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_response import (
    ClaudeComplianceIntegrationAccountResponse,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_create_request import (
    ClaudeComplianceIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_update_request import (
    ClaudeComplianceIntegrationAccountUpdateRequest,
)


class ClaudeComplianceIntegrationApi:
    """
    Manage your Datadog Claude Compliance integration accounts and account resources
    directly through the Datadog API. See the
    `Claude Compliance integration page <https://docs.datadoghq.com/integrations/anthropic-compliance-logs/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_claude_compliance_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ClaudeComplianceIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/claude-compliance/accounts",
                "operation_id": "create_claude_compliance_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ClaudeComplianceIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_claude_compliance_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/claude-compliance/accounts/{account_id}",
                "operation_id": "delete_claude_compliance_integration_account",
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

        self._get_claude_compliance_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ClaudeComplianceIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/claude-compliance/accounts/{account_id}",
                "operation_id": "get_claude_compliance_integration_account",
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

        self._list_claude_compliance_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (ClaudeComplianceIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/claude-compliance/accounts",
                "operation_id": "list_claude_compliance_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_claude_compliance_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (ClaudeComplianceIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/claude-compliance/accounts/{account_id}",
                "operation_id": "update_claude_compliance_integration_account",
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
                    "openapi_types": (ClaudeComplianceIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_claude_compliance_integration_account(
        self,
        body: ClaudeComplianceIntegrationAccountCreateRequest,
    ) -> ClaudeComplianceIntegrationAccountResponse:
        """Create a Claude Compliance integration account.

        Create a Claude Compliance integration account.

        :type body: ClaudeComplianceIntegrationAccountCreateRequest
        :rtype: ClaudeComplianceIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_claude_compliance_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_claude_compliance_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a Claude Compliance integration account.

        Delete a Claude Compliance integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_claude_compliance_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_claude_compliance_integration_account(
        self,
        account_id: str,
    ) -> ClaudeComplianceIntegrationAccountResponse:
        """Get a Claude Compliance integration account.

        Get a Claude Compliance integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: ClaudeComplianceIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_claude_compliance_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_claude_compliance_integration_accounts(
        self,
    ) -> ClaudeComplianceIntegrationAccountsResponse:
        """List Claude Compliance integration accounts.

        List Claude Compliance integration accounts.

        :rtype: ClaudeComplianceIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_claude_compliance_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_claude_compliance_integration_account(
        self,
        account_id: str,
        body: ClaudeComplianceIntegrationAccountUpdateRequest,
    ) -> ClaudeComplianceIntegrationAccountResponse:
        """Update a Claude Compliance integration account.

        Update a Claude Compliance integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: ClaudeComplianceIntegrationAccountUpdateRequest
        :rtype: ClaudeComplianceIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_claude_compliance_integration_account_endpoint.call_with_http_info(**kwargs)
