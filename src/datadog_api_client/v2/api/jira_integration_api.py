# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.jira_accounts_response import JiraAccountsResponse
from datadog_api_client.v2.model.jira_issue_templates_response import JiraIssueTemplatesResponse
from datadog_api_client.v2.model.jira_issue_template_response import JiraIssueTemplateResponse
from datadog_api_client.v2.model.jira_issue_template_create_request import JiraIssueTemplateCreateRequest
from datadog_api_client.v2.model.jira_issue_template_update_request import JiraIssueTemplateUpdateRequest


class JiraIntegrationApi:
    """
    Manage your Jira Integration. Atlassian Jira is a project management and issue tracking tool for teams to coordinate work and handle tasks efficiently.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_jira_issue_template_endpoint = _Endpoint(
            settings={
                "response_type": (JiraIssueTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/issue-templates",
                "operation_id": "create_jira_issue_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (JiraIssueTemplateCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_jira_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/accounts/{account_id}",
                "operation_id": "delete_jira_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_jira_issue_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/issue-templates/{issue_template_id}",
                "operation_id": "delete_jira_issue_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "issue_template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "issue_template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_jira_issue_template_endpoint = _Endpoint(
            settings={
                "response_type": (JiraIssueTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/issue-templates/{issue_template_id}",
                "operation_id": "get_jira_issue_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "issue_template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "issue_template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_jira_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (JiraAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/accounts",
                "operation_id": "list_jira_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_jira_issue_templates_endpoint = _Endpoint(
            settings={
                "response_type": (JiraIssueTemplatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/issue-templates",
                "operation_id": "list_jira_issue_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_jira_issue_template_endpoint = _Endpoint(
            settings={
                "response_type": (JiraIssueTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/jira/issue-templates/{issue_template_id}",
                "operation_id": "update_jira_issue_template",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "issue_template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "issue_template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (JiraIssueTemplateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_jira_issue_template(
        self,
        body: JiraIssueTemplateCreateRequest,
    ) -> JiraIssueTemplateResponse:
        """Create Jira issue template.

        Create a new Jira issue template.

        :type body: JiraIssueTemplateCreateRequest
        :rtype: JiraIssueTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_jira_issue_template_endpoint.call_with_http_info(**kwargs)

    def delete_jira_account(
        self,
        account_id: UUID,
    ) -> None:
        """Delete Jira account.

        Delete a Jira account by ID.

        :param account_id: The ID of the Jira account to delete
        :type account_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_jira_account_endpoint.call_with_http_info(**kwargs)

    def delete_jira_issue_template(
        self,
        issue_template_id: UUID,
    ) -> None:
        """Delete Jira issue template.

        Delete a Jira issue template by ID.

        :param issue_template_id: The ID of the Jira issue template to delete
        :type issue_template_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_template_id"] = issue_template_id

        return self._delete_jira_issue_template_endpoint.call_with_http_info(**kwargs)

    def get_jira_issue_template(
        self,
        issue_template_id: UUID,
    ) -> JiraIssueTemplateResponse:
        """Get Jira issue template.

        Get a Jira issue template by ID.

        :param issue_template_id: The ID of the Jira issue template to retrieve
        :type issue_template_id: UUID
        :rtype: JiraIssueTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_template_id"] = issue_template_id

        return self._get_jira_issue_template_endpoint.call_with_http_info(**kwargs)

    def list_jira_accounts(
        self,
    ) -> JiraAccountsResponse:
        """List Jira accounts.

        Get all Jira accounts for the organization.

        :rtype: JiraAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_jira_accounts_endpoint.call_with_http_info(**kwargs)

    def list_jira_issue_templates(
        self,
    ) -> JiraIssueTemplatesResponse:
        """List Jira issue templates.

        Get all Jira issue templates for the organization.

        :rtype: JiraIssueTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_jira_issue_templates_endpoint.call_with_http_info(**kwargs)

    def update_jira_issue_template(
        self,
        issue_template_id: UUID,
        body: JiraIssueTemplateUpdateRequest,
    ) -> JiraIssueTemplateResponse:
        """Update Jira issue template.

        Update a Jira issue template by ID.

        :param issue_template_id: The ID of the Jira issue template to update
        :type issue_template_id: UUID
        :type body: JiraIssueTemplateUpdateRequest
        :rtype: JiraIssueTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_template_id"] = issue_template_id

        kwargs["body"] = body

        return self._update_jira_issue_template_endpoint.call_with_http_info(**kwargs)
