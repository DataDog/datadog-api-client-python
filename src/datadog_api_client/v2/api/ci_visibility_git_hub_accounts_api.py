# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.ci_app_git_hub_accounts_response import CIAppGitHubAccountsResponse
from datadog_api_client.v2.model.ci_app_git_hub_account_response import CIAppGitHubAccountResponse
from datadog_api_client.v2.model.ci_app_git_hub_account_update_request import CIAppGitHubAccountUpdateRequest


class CIVisibilityGitHubAccountsApi:
    """
    Manage CI Visibility opt-in status for your GitHub accounts and repositories. See the
    `CI Visibility GitHub Actions setup page <https://docs.datadoghq.com/continuous_integration/pipelines/github/>`_
    for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_ci_app_git_hub_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (CIAppGitHubAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ci/github/accounts",
                "operation_id": "list_ci_app_git_hub_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_ci_app_git_hub_account_endpoint = _Endpoint(
            settings={
                "response_type": (CIAppGitHubAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ci/github/accounts",
                "operation_id": "update_ci_app_git_hub_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CIAppGitHubAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def list_ci_app_git_hub_accounts(
        self,
    ) -> CIAppGitHubAccountsResponse:
        """List GitHub CI Visibility status.

        Retrieve the list of GitHub accounts (organizations or users) available to this Datadog organization
        through its GitHub App installation, along with each account's and repository's CI Visibility opt-in status.

        :rtype: CIAppGitHubAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ci_app_git_hub_accounts_endpoint.call_with_http_info(**kwargs)

    def update_ci_app_git_hub_account(
        self,
        body: CIAppGitHubAccountUpdateRequest,
    ) -> CIAppGitHubAccountResponse:
        """Update GitHub CI Visibility status.

        Enable or disable CI Visibility for a GitHub account, one of its repositories, or both in the same request.
        The account (and, optionally, repository) are identified by name. Account-level and repository-level
        changes are independent and may both be supplied in the same request. At least one of ``enabled`` or
        ``repository.enabled`` must be provided. If the account name matches installations on more than one host,
        ``host`` must be supplied to disambiguate, otherwise a 409 is returned. Returns a 404 if the CI Visibility
        GitHub integration is not enabled for this organization, or if the given account or repository cannot be
        found by name.

        :type body: CIAppGitHubAccountUpdateRequest
        :rtype: CIAppGitHubAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_ci_app_git_hub_account_endpoint.call_with_http_info(**kwargs)
