# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.git_hub_costs_integration_accounts_response import (
    GitHubCostsIntegrationAccountsResponse,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_response import GitHubCostsIntegrationAccountResponse
from datadog_api_client.v2.model.git_hub_costs_integration_account_create_request import (
    GitHubCostsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_update_request import (
    GitHubCostsIntegrationAccountUpdateRequest,
)


class GitHubCostsIntegrationApi:
    """
    Manage your Datadog GitHub Costs integration accounts and account resources
    directly through the Datadog API. See the
    `GitHub Costs integration page <https://docs.datadoghq.com/integrations/github-costs/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_git_hub_costs_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCostsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/github-costs/accounts",
                "operation_id": "create_git_hub_costs_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GitHubCostsIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_git_hub_costs_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/github-costs/accounts/{account_id}",
                "operation_id": "delete_git_hub_costs_integration_account",
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

        self._get_git_hub_costs_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCostsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/github-costs/accounts/{account_id}",
                "operation_id": "get_git_hub_costs_integration_account",
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

        self._list_git_hub_costs_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCostsIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/github-costs/accounts",
                "operation_id": "list_git_hub_costs_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_git_hub_costs_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCostsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/integration-interfaces/github-costs/accounts/{account_id}",
                "operation_id": "update_git_hub_costs_integration_account",
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
                    "openapi_types": (GitHubCostsIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_git_hub_costs_integration_account(
        self,
        body: GitHubCostsIntegrationAccountCreateRequest,
    ) -> GitHubCostsIntegrationAccountResponse:
        """Create a GitHub Costs integration account.

        Create a GitHub Costs integration account.

        :type body: GitHubCostsIntegrationAccountCreateRequest
        :rtype: GitHubCostsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_git_hub_costs_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_git_hub_costs_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a GitHub Costs integration account.

        Delete a GitHub Costs integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_git_hub_costs_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_git_hub_costs_integration_account(
        self,
        account_id: str,
    ) -> GitHubCostsIntegrationAccountResponse:
        """Get a GitHub Costs integration account.

        Get a GitHub Costs integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: GitHubCostsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_git_hub_costs_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_git_hub_costs_integration_accounts(
        self,
    ) -> GitHubCostsIntegrationAccountsResponse:
        """List GitHub Costs integration accounts.

        List GitHub Costs integration accounts.

        :rtype: GitHubCostsIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_git_hub_costs_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_git_hub_costs_integration_account(
        self,
        account_id: str,
        body: GitHubCostsIntegrationAccountUpdateRequest,
    ) -> GitHubCostsIntegrationAccountResponse:
        """Update a GitHub Costs integration account.

        Update a GitHub Costs integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: GitHubCostsIntegrationAccountUpdateRequest
        :rtype: GitHubCostsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_git_hub_costs_integration_account_endpoint.call_with_http_info(**kwargs)
