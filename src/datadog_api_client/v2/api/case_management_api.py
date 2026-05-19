# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.cases_response import CasesResponse
from datadog_api_client.v2.model.case_sortable_field import CaseSortableField
from datadog_api_client.v2.model.case import Case
from datadog_api_client.v2.model.case_response import CaseResponse
from datadog_api_client.v2.model.case_create_request import CaseCreateRequest
from datadog_api_client.v2.model.case_aggregate_response import CaseAggregateResponse
from datadog_api_client.v2.model.case_aggregate_request import CaseAggregateRequest
from datadog_api_client.v2.model.case_bulk_update_request import CaseBulkUpdateRequest
from datadog_api_client.v2.model.case_count_response import CaseCountResponse
from datadog_api_client.v2.model.case_links_response import CaseLinksResponse
from datadog_api_client.v2.model.case_link_response import CaseLinkResponse
from datadog_api_client.v2.model.case_link_create_request import CaseLinkCreateRequest
from datadog_api_client.v2.model.projects_response import ProjectsResponse
from datadog_api_client.v2.model.project_response import ProjectResponse
from datadog_api_client.v2.model.project_create_request import ProjectCreateRequest
from datadog_api_client.v2.model.project_favorites_response import ProjectFavoritesResponse
from datadog_api_client.v2.model.project_update_request import ProjectUpdateRequest
from datadog_api_client.v2.model.case_notification_rules_response import CaseNotificationRulesResponse
from datadog_api_client.v2.model.case_notification_rule_response import CaseNotificationRuleResponse
from datadog_api_client.v2.model.case_notification_rule_create_request import CaseNotificationRuleCreateRequest
from datadog_api_client.v2.model.case_notification_rule_update_request import CaseNotificationRuleUpdateRequest
from datadog_api_client.v2.model.automation_rules_response import AutomationRulesResponse
from datadog_api_client.v2.model.automation_rule_response import AutomationRuleResponse
from datadog_api_client.v2.model.automation_rule_create_request import AutomationRuleCreateRequest
from datadog_api_client.v2.model.automation_rule_update_request import AutomationRuleUpdateRequest
from datadog_api_client.v2.model.case_views_response import CaseViewsResponse
from datadog_api_client.v2.model.case_view_response import CaseViewResponse
from datadog_api_client.v2.model.case_view_create_request import CaseViewCreateRequest
from datadog_api_client.v2.model.case_view_update_request import CaseViewUpdateRequest
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_assign_request import CaseAssignRequest
from datadog_api_client.v2.model.case_update_attributes_request import CaseUpdateAttributesRequest
from datadog_api_client.v2.model.timeline_response import TimelineResponse
from datadog_api_client.v2.model.case_comment_request import CaseCommentRequest
from datadog_api_client.v2.model.case_update_comment_request import CaseUpdateCommentRequest
from datadog_api_client.v2.model.case_update_custom_attribute_request import CaseUpdateCustomAttributeRequest
from datadog_api_client.v2.model.case_update_description_request import CaseUpdateDescriptionRequest
from datadog_api_client.v2.model.case_update_due_date_request import CaseUpdateDueDateRequest
from datadog_api_client.v2.model.case_insights_request import CaseInsightsRequest
from datadog_api_client.v2.model.case_update_priority_request import CaseUpdatePriorityRequest
from datadog_api_client.v2.model.relationship_to_incident_request import RelationshipToIncidentRequest
from datadog_api_client.v2.model.jira_issue_link_request import JiraIssueLinkRequest
from datadog_api_client.v2.model.jira_issue_create_request import JiraIssueCreateRequest
from datadog_api_client.v2.model.notebook_create_request import NotebookCreateRequest
from datadog_api_client.v2.model.project_relationship import ProjectRelationship
from datadog_api_client.v2.model.service_now_ticket_create_request import ServiceNowTicketCreateRequest
from datadog_api_client.v2.model.case_update_resolved_reason_request import CaseUpdateResolvedReasonRequest
from datadog_api_client.v2.model.case_update_status_request import CaseUpdateStatusRequest
from datadog_api_client.v2.model.case_update_title_request import CaseUpdateTitleRequest
from datadog_api_client.v2.model.case_watchers_response import CaseWatchersResponse
from datadog_api_client.v2.model.maintenance_windows_response import MaintenanceWindowsResponse
from datadog_api_client.v2.model.maintenance_window_response import MaintenanceWindowResponse
from datadog_api_client.v2.model.maintenance_window_create_request import MaintenanceWindowCreateRequest
from datadog_api_client.v2.model.maintenance_window_update_request import MaintenanceWindowUpdateRequest


class CaseManagementApi:
    """
    View and manage cases and projects within Case Management. See the `Case Management page <https://docs.datadoghq.com/service_management/case_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._add_case_insights_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/insights",
                "operation_id": "add_case_insights",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseInsightsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._aggregate_cases_endpoint = _Endpoint(
            settings={
                "response_type": (CaseAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/aggregate",
                "operation_id": "aggregate_cases",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseAggregateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._archive_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/archive",
                "operation_id": "archive_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._assign_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/assign",
                "operation_id": "assign_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseAssignRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_update_cases_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/bulk",
                "operation_id": "bulk_update_cases",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseBulkUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._comment_case_endpoint = _Endpoint(
            settings={
                "response_type": (TimelineResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/{case_id}/comment",
                "operation_id": "comment_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseCommentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._count_cases_endpoint = _Endpoint(
            settings={
                "response_type": (CaseCountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/count",
                "operation_id": "count_cases",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query_filter": {
                    "openapi_types": (str,),
                    "attribute": "query_filter",
                    "location": "query",
                },
                "group_bys": {
                    "openapi_types": (str,),
                    "attribute": "group_bys",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases",
                "operation_id": "create_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules",
                "operation_id": "create_case_automation_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AutomationRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_jira_issue_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/jira_issues",
                "operation_id": "create_case_jira_issue",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (JiraIssueCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_link_endpoint = _Endpoint(
            settings={
                "response_type": (CaseLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/link",
                "operation_id": "create_case_link",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseLinkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_notebook_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/notebook",
                "operation_id": "create_case_notebook",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (NotebookCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_service_now_ticket_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/servicenow_tickets",
                "operation_id": "create_case_service_now_ticket",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ServiceNowTicketCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_view_endpoint = _Endpoint(
            settings={
                "response_type": (CaseViewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/views",
                "operation_id": "create_case_view",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseViewCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_maintenance_window_endpoint = _Endpoint(
            settings={
                "response_type": (MaintenanceWindowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/maintenance_windows",
                "operation_id": "create_maintenance_window",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MaintenanceWindowCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_project_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects",
                "operation_id": "create_project",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProjectCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_project_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CaseNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/notification_rules",
                "operation_id": "create_project_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseNotificationRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules/{rule_id}",
                "operation_id": "delete_case_automation_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_case_comment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/{case_id}/comment/{cell_id}",
                "operation_id": "delete_case_comment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "cell_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cell_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_case_custom_attribute_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}",
                "operation_id": "delete_case_custom_attribute",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "custom_attribute_key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_attribute_key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_case_link_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/link/{link_id}",
                "operation_id": "delete_case_link",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_case_view_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/views/{view_id}",
                "operation_id": "delete_case_view",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "view_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "view_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_maintenance_window_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/maintenance_windows/{maintenance_window_id}",
                "operation_id": "delete_maintenance_window",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "maintenance_window_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "maintenance_window_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}",
                "operation_id": "delete_project",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_project_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}",
                "operation_id": "delete_project_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "notification_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "notification_rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._disable_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules/{rule_id}/disable",
                "operation_id": "disable_case_automation_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._enable_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules/{rule_id}/enable",
                "operation_id": "enable_case_automation_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._favorite_case_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/favorites",
                "operation_id": "favorite_case_project",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}",
                "operation_id": "get_case",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules/{rule_id}",
                "operation_id": "get_case_automation_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_case_view_endpoint = _Endpoint(
            settings={
                "response_type": (CaseViewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/views/{view_id}",
                "operation_id": "get_case_view",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "view_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "view_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_project_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}",
                "operation_id": "get_project",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_project_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (CaseNotificationRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/notification_rules",
                "operation_id": "get_project_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_projects_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects",
                "operation_id": "get_projects",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._link_incident_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/incidents",
                "operation_id": "link_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._link_jira_issue_to_case_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/jira_issues",
                "operation_id": "link_jira_issue_to_case",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (JiraIssueLinkRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_case_automation_rules_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules",
                "operation_id": "list_case_automation_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_case_links_endpoint = _Endpoint(
            settings={
                "response_type": (CaseLinksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/link",
                "operation_id": "list_case_links",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "entity_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity_type",
                    "location": "query",
                },
                "entity_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "entity_id",
                    "location": "query",
                },
                "relationship": {
                    "openapi_types": (str,),
                    "attribute": "relationship",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_case_timeline_endpoint = _Endpoint(
            settings={
                "response_type": (TimelineResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/timelines",
                "operation_id": "list_case_timeline",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
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
                "sort_ascending": {
                    "openapi_types": (bool,),
                    "attribute": "sort[ascending]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_case_views_endpoint = _Endpoint(
            settings={
                "response_type": (CaseViewsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/views",
                "operation_id": "list_case_views",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_case_watchers_endpoint = _Endpoint(
            settings={
                "response_type": (CaseWatchersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/watchers",
                "operation_id": "list_case_watchers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_maintenance_windows_endpoint = _Endpoint(
            settings={
                "response_type": (MaintenanceWindowsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/maintenance_windows",
                "operation_id": "list_maintenance_windows",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_user_case_project_favorites_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectFavoritesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/favorites",
                "operation_id": "list_user_case_project_favorites",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._move_case_to_project_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/project",
                "operation_id": "move_case_to_project",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ProjectRelationship,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._remove_case_insights_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/insights",
                "operation_id": "remove_case_insights",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseInsightsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_cases_endpoint = _Endpoint(
            settings={
                "response_type": (CasesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases",
                "operation_id": "search_cases",
                "http_method": "GET",
                "version": "v2",
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
                "sort_field": {
                    "openapi_types": (CaseSortableField,),
                    "attribute": "sort[field]",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "sort_asc": {
                    "openapi_types": (bool,),
                    "attribute": "sort[asc]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unarchive_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/unarchive",
                "operation_id": "unarchive_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._unassign_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/unassign",
                "operation_id": "unassign_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._unfavorite_case_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/favorites",
                "operation_id": "unfavorite_case_project",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._unlink_jira_issue_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/relationships/jira_issues",
                "operation_id": "unlink_jira_issue",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._unwatch_case_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/watchers/{user_uuid}",
                "operation_id": "unwatch_case",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "user_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._update_attributes_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/attributes",
                "operation_id": "update_attributes",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateAttributesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_automation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AutomationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/rules/{rule_id}",
                "operation_id": "update_case_automation_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AutomationRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_comment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/comment/{cell_id}",
                "operation_id": "update_case_comment",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "cell_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cell_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateCommentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_custom_attribute_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}",
                "operation_id": "update_case_custom_attribute",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "custom_attribute_key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_attribute_key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateCustomAttributeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_description_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/description",
                "operation_id": "update_case_description",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateDescriptionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_due_date_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/due_date",
                "operation_id": "update_case_due_date",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateDueDateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_resolved_reason_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/resolved_reason",
                "operation_id": "update_case_resolved_reason",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateResolvedReasonRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_title_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/title",
                "operation_id": "update_case_title",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateTitleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_view_endpoint = _Endpoint(
            settings={
                "response_type": (CaseViewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/views/{view_id}",
                "operation_id": "update_case_view",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "view_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "view_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseViewUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_maintenance_window_endpoint = _Endpoint(
            settings={
                "response_type": (MaintenanceWindowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/maintenance_windows/{maintenance_window_id}",
                "operation_id": "update_maintenance_window",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "maintenance_window_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "maintenance_window_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MaintenanceWindowUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_priority_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/priority",
                "operation_id": "update_priority",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdatePriorityRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_project_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}",
                "operation_id": "update_project",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ProjectUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_project_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}/notification_rules/{notification_rule_id}",
                "operation_id": "update_project_notification_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
                "notification_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "notification_rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseNotificationRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_status_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/status",
                "operation_id": "update_status",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateStatusRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._watch_case_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/watchers/{user_uuid}",
                "operation_id": "watch_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "user_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

    def add_case_insights(
        self,
        case_id: str,
        body: CaseInsightsRequest,
    ) -> CaseResponse:
        """Add insights to a case.

        Adds one or more insights to a case. Insights are references to related Datadog resources (such as monitors, security signals, incidents, or error tracking issues) that provide investigative context. Up to 100 insights can be added per request. Each insight requires a type (see ``CaseInsightType`` for allowed values), a ref (URL path to the resource), and a resource_id.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case insights request.
        :type body: CaseInsightsRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._add_case_insights_endpoint.call_with_http_info(**kwargs)

    def aggregate_cases(
        self,
        body: CaseAggregateRequest,
    ) -> CaseAggregateResponse:
        """Aggregate cases.

        Performs an aggregation query over cases, grouping results by specified fields and returning counts per group along with a total. Useful for dashboards and analytics.

        :param body: Case aggregate request payload.
        :type body: CaseAggregateRequest
        :rtype: CaseAggregateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._aggregate_cases_endpoint.call_with_http_info(**kwargs)

    def archive_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Archive case.

        Archive case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Archive case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._archive_case_endpoint.call_with_http_info(**kwargs)

    def assign_case(
        self,
        case_id: str,
        body: CaseAssignRequest,
    ) -> CaseResponse:
        """Assign case.

        Assign case to a user

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Assign case payload
        :type body: CaseAssignRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._assign_case_endpoint.call_with_http_info(**kwargs)

    def bulk_update_cases(
        self,
        body: CaseBulkUpdateRequest,
    ) -> None:
        """Bulk update cases.

        Applies a single action (such as changing priority, status, assignment, or archiving) to multiple cases at once. The list of case IDs and the action type with its payload are specified in the request body.

        :param body: Case bulk update request payload.
        :type body: CaseBulkUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_update_cases_endpoint.call_with_http_info(**kwargs)

    def comment_case(
        self,
        case_id: str,
        body: CaseCommentRequest,
    ) -> TimelineResponse:
        """Comment case.

        Comment case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case comment payload
        :type body: CaseCommentRequest
        :rtype: TimelineResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._comment_case_endpoint.call_with_http_info(**kwargs)

    def count_cases(
        self,
        *,
        query_filter: Union[str, UnsetType] = unset,
        group_bys: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> CaseCountResponse:
        """Count cases.

        Returns case counts, optionally grouped by one or more fields (for example, status, priority). Supports a query filter to narrow the scope.

        :param query_filter: Filter query for cases.
        :type query_filter: str, optional
        :param group_bys: Comma-separated fields to group by.
        :type group_bys: str, optional
        :param limit: Maximum facet values to return.
        :type limit: int, optional
        :rtype: CaseCountResponse
        """
        kwargs: Dict[str, Any] = {}
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter

        if group_bys is not unset:
            kwargs["group_bys"] = group_bys

        if limit is not unset:
            kwargs["limit"] = limit

        return self._count_cases_endpoint.call_with_http_info(**kwargs)

    def create_case(
        self,
        body: CaseCreateRequest,
    ) -> CaseResponse:
        """Create a case.

        Create a Case

        :param body: Case payload
        :type body: CaseCreateRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_case_endpoint.call_with_http_info(**kwargs)

    def create_case_automation_rule(
        self,
        project_id: str,
        body: AutomationRuleCreateRequest,
    ) -> AutomationRuleResponse:
        """Create an automation rule.

        Creates an automation rule for a project. The rule defines a trigger event (for example, case created, status transitioned) and an action to execute.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param body: Automation rule payload.
        :type body: AutomationRuleCreateRequest
        :rtype: AutomationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._create_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def create_case_jira_issue(
        self,
        case_id: str,
        body: JiraIssueCreateRequest,
    ) -> None:
        """Create Jira issue for case.

        Create a new Jira issue and link it to a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Jira issue creation request
        :type body: JiraIssueCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._create_case_jira_issue_endpoint.call_with_http_info(**kwargs)

    def create_case_link(
        self,
        body: CaseLinkCreateRequest,
    ) -> CaseLinkResponse:
        """Create a case link.

        Creates a directional link between two cases (for example, case A blocks case B). The parent and child cases and their relationship type must be specified.

        :param body: Case link create request.
        :type body: CaseLinkCreateRequest
        :rtype: CaseLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_case_link_endpoint.call_with_http_info(**kwargs)

    def create_case_notebook(
        self,
        case_id: str,
        body: NotebookCreateRequest,
    ) -> None:
        """Create investigation notebook for case.

        Create a new investigation notebook and link it to a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Notebook creation request
        :type body: NotebookCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._create_case_notebook_endpoint.call_with_http_info(**kwargs)

    def create_case_service_now_ticket(
        self,
        case_id: str,
        body: ServiceNowTicketCreateRequest,
    ) -> None:
        """Create ServiceNow ticket for case.

        Create a new ServiceNow incident ticket and link it to a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: ServiceNow ticket creation request
        :type body: ServiceNowTicketCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._create_case_service_now_ticket_endpoint.call_with_http_info(**kwargs)

    def create_case_view(
        self,
        body: CaseViewCreateRequest,
    ) -> CaseViewResponse:
        """Create a case view.

        Creates a new saved case view with a name, filter query, and associated project. Optionally, a notification rule can be linked to the view.

        :param body: Case view payload.
        :type body: CaseViewCreateRequest
        :rtype: CaseViewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_case_view_endpoint.call_with_http_info(**kwargs)

    def create_maintenance_window(
        self,
        body: MaintenanceWindowCreateRequest,
    ) -> MaintenanceWindowResponse:
        """Create a maintenance window.

        Creates a maintenance window for event management cases with a name, case filter query, and time range (start and end).

        :param body: Maintenance window payload.
        :type body: MaintenanceWindowCreateRequest
        :rtype: MaintenanceWindowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def create_project(
        self,
        body: ProjectCreateRequest,
    ) -> ProjectResponse:
        """Create a project.

        Create a project.

        :param body: Project payload.
        :type body: ProjectCreateRequest
        :rtype: ProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_project_endpoint.call_with_http_info(**kwargs)

    def create_project_notification_rule(
        self,
        project_id: str,
        body: CaseNotificationRuleCreateRequest,
    ) -> CaseNotificationRuleResponse:
        """Create a notification rule.

        Create a notification rule for a project.

        :param project_id: Project UUID
        :type project_id: str
        :param body: Notification rule payload
        :type body: CaseNotificationRuleCreateRequest
        :rtype: CaseNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._create_project_notification_rule_endpoint.call_with_http_info(**kwargs)

    def delete_case_automation_rule(
        self,
        project_id: str,
        rule_id: str,
    ) -> None:
        """Delete an automation rule.

        Permanently deletes an automation rule from a project.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param rule_id: The UUID of the automation rule.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["rule_id"] = rule_id

        return self._delete_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def delete_case_comment(
        self,
        case_id: str,
        cell_id: str,
    ) -> None:
        """Delete case comment.

        Delete case comment

        :param case_id: Case's UUID or key
        :type case_id: str
        :param cell_id: The UUID of the timeline cell (comment) to update.
        :type cell_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["cell_id"] = cell_id

        return self._delete_case_comment_endpoint.call_with_http_info(**kwargs)

    def delete_case_custom_attribute(
        self,
        case_id: str,
        custom_attribute_key: str,
    ) -> CaseResponse:
        """Delete custom attribute from case.

        Delete custom attribute from case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param custom_attribute_key: Case Custom attribute's key
        :type custom_attribute_key: str
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["custom_attribute_key"] = custom_attribute_key

        return self._delete_case_custom_attribute_endpoint.call_with_http_info(**kwargs)

    def delete_case_link(
        self,
        link_id: str,
    ) -> None:
        """Delete a case link.

        Deletes an existing link between cases by link ID.

        :param link_id: The UUID of the case link.
        :type link_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["link_id"] = link_id

        return self._delete_case_link_endpoint.call_with_http_info(**kwargs)

    def delete_case_view(
        self,
        view_id: str,
    ) -> None:
        """Delete a case view.

        Permanently deletes a saved case view.

        :param view_id: The UUID of the case view.
        :type view_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["view_id"] = view_id

        return self._delete_case_view_endpoint.call_with_http_info(**kwargs)

    def delete_maintenance_window(
        self,
        maintenance_window_id: str,
    ) -> None:
        """Delete a maintenance window.

        Permanently deletes a maintenance window.

        :param maintenance_window_id: The UUID of the maintenance window.
        :type maintenance_window_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["maintenance_window_id"] = maintenance_window_id

        return self._delete_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def delete_project(
        self,
        project_id: str,
    ) -> None:
        """Remove a project.

        Remove a project using the project's ``id``.

        :param project_id: Project UUID.
        :type project_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._delete_project_endpoint.call_with_http_info(**kwargs)

    def delete_project_notification_rule(
        self,
        project_id: str,
        notification_rule_id: str,
    ) -> None:
        """Delete a notification rule.

        Delete a notification rule using the notification rule's ``id``.

        :param project_id: Project UUID
        :type project_id: str
        :param notification_rule_id: Notification Rule UUID
        :type notification_rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["notification_rule_id"] = notification_rule_id

        return self._delete_project_notification_rule_endpoint.call_with_http_info(**kwargs)

    def disable_case_automation_rule(
        self,
        project_id: str,
        rule_id: str,
    ) -> AutomationRuleResponse:
        """Disable an automation rule.

        Disables an automation rule so it no longer triggers on case events. The rule configuration is preserved.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param rule_id: The UUID of the automation rule.
        :type rule_id: str
        :rtype: AutomationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["rule_id"] = rule_id

        return self._disable_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def enable_case_automation_rule(
        self,
        project_id: str,
        rule_id: str,
    ) -> AutomationRuleResponse:
        """Enable an automation rule.

        Enables a previously disabled automation rule so it triggers on matching case events.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param rule_id: The UUID of the automation rule.
        :type rule_id: str
        :rtype: AutomationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["rule_id"] = rule_id

        return self._enable_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def favorite_case_project(
        self,
        project_id: str,
    ) -> None:
        """Favorite a project.

        Marks a case project as a favorite for the current authenticated user.

        :param project_id: Project UUID.
        :type project_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._favorite_case_project_endpoint.call_with_http_info(**kwargs)

    def get_case(
        self,
        case_id: str,
    ) -> CaseResponse:
        """Get the details of a case.

        Get the details of case by ``case_id``

        :param case_id: Case's UUID or key
        :type case_id: str
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        return self._get_case_endpoint.call_with_http_info(**kwargs)

    def get_case_automation_rule(
        self,
        project_id: str,
        rule_id: str,
    ) -> AutomationRuleResponse:
        """Get an automation rule.

        Returns a single automation rule identified by its UUID, including its trigger, action, and current state (enabled/disabled).

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param rule_id: The UUID of the automation rule.
        :type rule_id: str
        :rtype: AutomationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["rule_id"] = rule_id

        return self._get_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def get_case_view(
        self,
        view_id: str,
    ) -> CaseViewResponse:
        """Get a case view.

        Returns a single saved case view identified by its UUID, including its query, associated project, and timestamps.

        :param view_id: The UUID of the case view.
        :type view_id: str
        :rtype: CaseViewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["view_id"] = view_id

        return self._get_case_view_endpoint.call_with_http_info(**kwargs)

    def get_project(
        self,
        project_id: str,
    ) -> ProjectResponse:
        """Get the details of a project.

        Get the details of a project by ``project_id``.

        :param project_id: Project UUID.
        :type project_id: str
        :rtype: ProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._get_project_endpoint.call_with_http_info(**kwargs)

    def get_project_notification_rules(
        self,
        project_id: str,
    ) -> CaseNotificationRulesResponse:
        """Get notification rules.

        Get all notification rules for a project.

        :param project_id: Project UUID
        :type project_id: str
        :rtype: CaseNotificationRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._get_project_notification_rules_endpoint.call_with_http_info(**kwargs)

    def get_projects(
        self,
    ) -> ProjectsResponse:
        """Get all projects.

        Get all projects.

        :rtype: ProjectsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_projects_endpoint.call_with_http_info(**kwargs)

    def link_incident(
        self,
        case_id: str,
        body: RelationshipToIncidentRequest,
    ) -> CaseResponse:
        """Link incident to case.

        Link an incident to a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Incident link request
        :type body: RelationshipToIncidentRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._link_incident_endpoint.call_with_http_info(**kwargs)

    def link_jira_issue_to_case(
        self,
        case_id: str,
        body: JiraIssueLinkRequest,
    ) -> None:
        """Link existing Jira issue to case.

        Link an existing Jira issue to a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Jira issue link request
        :type body: JiraIssueLinkRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._link_jira_issue_to_case_endpoint.call_with_http_info(**kwargs)

    def list_case_automation_rules(
        self,
        project_id: str,
    ) -> AutomationRulesResponse:
        """List automation rules.

        Returns all automation rules configured for a project. Automation rules allow automatic actions to be triggered by case events like creation, status transitions, or attribute changes.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :rtype: AutomationRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._list_case_automation_rules_endpoint.call_with_http_info(**kwargs)

    def list_case_links(
        self,
        entity_type: str,
        entity_id: str,
        *,
        relationship: Union[str, UnsetType] = unset,
    ) -> CaseLinksResponse:
        """List case links.

        Returns all links associated with a case. Links define relationships (for example, BLOCKS) between cases. Requires entity_type and entity_id query parameters.

        :param entity_type: The entity type to look up links for. Use ``CASE`` to find links for a specific case.
        :type entity_type: str
        :param entity_id: The UUID of the entity to look up links for.
        :type entity_id: str
        :param relationship: Optional filter to only return links of a specific relationship type (for example, ``BLOCKS`` or ``CAUSES`` ).
        :type relationship: str, optional
        :rtype: CaseLinksResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["entity_type"] = entity_type

        kwargs["entity_id"] = entity_id

        if relationship is not unset:
            kwargs["relationship"] = relationship

        return self._list_case_links_endpoint.call_with_http_info(**kwargs)

    def list_case_timeline(
        self,
        case_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort_ascending: Union[bool, UnsetType] = unset,
    ) -> TimelineResponse:
        """Get case timeline.

        Returns the timeline of events for a case, including comments, status changes, and other activity. Supports pagination and sort order.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param page_size: Number of timeline cells to return per page.
        :type page_size: int, optional
        :param page_number: Zero-based page number for pagination.
        :type page_number: int, optional
        :param sort_ascending: If ``true`` , returns timeline cells in chronological order (oldest first). Defaults to ``false`` (newest first).
        :type sort_ascending: bool, optional
        :rtype: TimelineResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort_ascending is not unset:
            kwargs["sort_ascending"] = sort_ascending

        return self._list_case_timeline_endpoint.call_with_http_info(**kwargs)

    def list_case_views(
        self,
        project_id: str,
    ) -> CaseViewsResponse:
        """List case views.

        Returns all saved case views for a given project. Views are saved search queries that allow quick access to filtered lists of cases.

        :param project_id: Filter views by project identifier.
        :type project_id: str
        :rtype: CaseViewsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._list_case_views_endpoint.call_with_http_info(**kwargs)

    def list_case_watchers(
        self,
        case_id: str,
    ) -> CaseWatchersResponse:
        """List case watchers.

        Returns the list of users who are watching a case. Watchers receive notifications about updates to the case.

        :param case_id: Case's UUID or key
        :type case_id: str
        :rtype: CaseWatchersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        return self._list_case_watchers_endpoint.call_with_http_info(**kwargs)

    def list_maintenance_windows(
        self,
    ) -> MaintenanceWindowsResponse:
        """List maintenance windows.

        Returns all configured maintenance windows for event management cases. Maintenance windows define time periods during which case notifications and automation rules are suppressed for cases matching a given query.

        :rtype: MaintenanceWindowsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_maintenance_windows_endpoint.call_with_http_info(**kwargs)

    def list_user_case_project_favorites(
        self,
    ) -> ProjectFavoritesResponse:
        """List project favorites.

        Returns the list of case projects that the current authenticated user has marked as favorites.

        :rtype: ProjectFavoritesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_user_case_project_favorites_endpoint.call_with_http_info(**kwargs)

    def move_case_to_project(
        self,
        case_id: str,
        body: ProjectRelationship,
    ) -> CaseResponse:
        """Update case project.

        Update the project associated with a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Project update request
        :type body: ProjectRelationship
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._move_case_to_project_endpoint.call_with_http_info(**kwargs)

    def remove_case_insights(
        self,
        case_id: str,
        body: CaseInsightsRequest,
    ) -> CaseResponse:
        """Remove insights from a case.

        Removes one or more previously added insights from a case by specifying their type and resource identifier in the request body.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case insights request.
        :type body: CaseInsightsRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._remove_case_insights_endpoint.call_with_http_info(**kwargs)

    def search_cases(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort_field: Union[CaseSortableField, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        sort_asc: Union[bool, UnsetType] = unset,
    ) -> CasesResponse:
        """Search cases.

        Search cases.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort_field: Specify which field to sort
        :type sort_field: CaseSortableField, optional
        :param filter: Search query
        :type filter: str, optional
        :param sort_asc: Specify if order is ascending or not
        :type sort_asc: bool, optional
        :rtype: CasesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort_field is not unset:
            kwargs["sort_field"] = sort_field

        if filter is not unset:
            kwargs["filter"] = filter

        if sort_asc is not unset:
            kwargs["sort_asc"] = sort_asc

        return self._search_cases_endpoint.call_with_http_info(**kwargs)

    def search_cases_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort_field: Union[CaseSortableField, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        sort_asc: Union[bool, UnsetType] = unset,
    ) -> collections.abc.Iterable[Case]:
        """Search cases.

        Provide a paginated version of :meth:`search_cases`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort_field: Specify which field to sort
        :type sort_field: CaseSortableField, optional
        :param filter: Search query
        :type filter: str, optional
        :param sort_asc: Specify if order is ascending or not
        :type sort_asc: bool, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Case]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort_field is not unset:
            kwargs["sort_field"] = sort_field

        if filter is not unset:
            kwargs["filter"] = filter

        if sort_asc is not unset:
            kwargs["sort_asc"] = sort_asc

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._search_cases_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "page_start": 1,
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def unarchive_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Unarchive case.

        Unarchive case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Unarchive case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._unarchive_case_endpoint.call_with_http_info(**kwargs)

    def unassign_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Unassign case.

        Unassign case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Unassign case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._unassign_case_endpoint.call_with_http_info(**kwargs)

    def unfavorite_case_project(
        self,
        project_id: str,
    ) -> None:
        """Unfavorite a project.

        Removes a case project from the current user's favorites list.

        :param project_id: Project UUID.
        :type project_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._unfavorite_case_project_endpoint.call_with_http_info(**kwargs)

    def unlink_jira_issue(
        self,
        case_id: str,
    ) -> None:
        """Remove Jira issue link from case.

        Remove the link between a Jira issue and a case

        :param case_id: Case's UUID or key
        :type case_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        return self._unlink_jira_issue_endpoint.call_with_http_info(**kwargs)

    def unwatch_case(
        self,
        case_id: str,
        user_uuid: str,
    ) -> None:
        """Unwatch a case.

        Removes a user from the watchers list of a case. The user no longer receives notifications about updates to the case.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param user_uuid: The UUID of the user to add or remove as a watcher.
        :type user_uuid: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["user_uuid"] = user_uuid

        return self._unwatch_case_endpoint.call_with_http_info(**kwargs)

    def update_attributes(
        self,
        case_id: str,
        body: CaseUpdateAttributesRequest,
    ) -> CaseResponse:
        """Update case attributes.

        Update case attributes

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case attributes update payload
        :type body: CaseUpdateAttributesRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_attributes_endpoint.call_with_http_info(**kwargs)

    def update_case_automation_rule(
        self,
        project_id: str,
        rule_id: str,
        body: AutomationRuleUpdateRequest,
    ) -> AutomationRuleResponse:
        """Update an automation rule.

        Updates the trigger, action, name, or state of an existing automation rule.

        :param project_id: The UUID of the project that owns the automation rules.
        :type project_id: str
        :param rule_id: The UUID of the automation rule.
        :type rule_id: str
        :param body: Automation rule payload.
        :type body: AutomationRuleUpdateRequest
        :rtype: AutomationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_case_automation_rule_endpoint.call_with_http_info(**kwargs)

    def update_case_comment(
        self,
        case_id: str,
        cell_id: str,
        body: CaseUpdateCommentRequest,
    ) -> None:
        """Update case comment.

        Updates the text content of an existing comment on a case timeline. The comment is identified by its cell ID.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param cell_id: The UUID of the timeline cell (comment) to update.
        :type cell_id: str
        :param body: Case update comment payload.
        :type body: CaseUpdateCommentRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["cell_id"] = cell_id

        kwargs["body"] = body

        return self._update_case_comment_endpoint.call_with_http_info(**kwargs)

    def update_case_custom_attribute(
        self,
        case_id: str,
        custom_attribute_key: str,
        body: CaseUpdateCustomAttributeRequest,
    ) -> CaseResponse:
        """Update case custom attribute.

        Update case custom attribute

        :param case_id: Case's UUID or key
        :type case_id: str
        :param custom_attribute_key: Case Custom attribute's key
        :type custom_attribute_key: str
        :param body: Update case custom attribute payload
        :type body: CaseUpdateCustomAttributeRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["custom_attribute_key"] = custom_attribute_key

        kwargs["body"] = body

        return self._update_case_custom_attribute_endpoint.call_with_http_info(**kwargs)

    def update_case_description(
        self,
        case_id: str,
        body: CaseUpdateDescriptionRequest,
    ) -> CaseResponse:
        """Update case description.

        Update case description

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case description update payload
        :type body: CaseUpdateDescriptionRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_description_endpoint.call_with_http_info(**kwargs)

    def update_case_due_date(
        self,
        case_id: str,
        body: CaseUpdateDueDateRequest,
    ) -> CaseResponse:
        """Update case due date.

        Sets or updates the due date for a case. The due date is a calendar date (without a time component) indicating when the case should be resolved.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case due date update payload.
        :type body: CaseUpdateDueDateRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_due_date_endpoint.call_with_http_info(**kwargs)

    def update_case_resolved_reason(
        self,
        case_id: str,
        body: CaseUpdateResolvedReasonRequest,
    ) -> CaseResponse:
        """Update case resolved reason.

        Sets the resolved reason for a security case (for example, FALSE_POSITIVE, TRUE_POSITIVE). Applicable to security-type cases.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case resolved reason update payload.
        :type body: CaseUpdateResolvedReasonRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_resolved_reason_endpoint.call_with_http_info(**kwargs)

    def update_case_title(
        self,
        case_id: str,
        body: CaseUpdateTitleRequest,
    ) -> CaseResponse:
        """Update case title.

        Update case title

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case title update payload
        :type body: CaseUpdateTitleRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_title_endpoint.call_with_http_info(**kwargs)

    def update_case_view(
        self,
        view_id: str,
        body: CaseViewUpdateRequest,
    ) -> CaseViewResponse:
        """Update a case view.

        Updates the name, query, or notification rule of an existing case view.

        :param view_id: The UUID of the case view.
        :type view_id: str
        :param body: Case view payload.
        :type body: CaseViewUpdateRequest
        :rtype: CaseViewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["view_id"] = view_id

        kwargs["body"] = body

        return self._update_case_view_endpoint.call_with_http_info(**kwargs)

    def update_maintenance_window(
        self,
        maintenance_window_id: str,
        body: MaintenanceWindowUpdateRequest,
    ) -> MaintenanceWindowResponse:
        """Update a maintenance window.

        Updates the name, query, start time, or end time of an existing maintenance window.

        :param maintenance_window_id: The UUID of the maintenance window.
        :type maintenance_window_id: str
        :param body: Maintenance window payload.
        :type body: MaintenanceWindowUpdateRequest
        :rtype: MaintenanceWindowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["maintenance_window_id"] = maintenance_window_id

        kwargs["body"] = body

        return self._update_maintenance_window_endpoint.call_with_http_info(**kwargs)

    def update_priority(
        self,
        case_id: str,
        body: CaseUpdatePriorityRequest,
    ) -> CaseResponse:
        """Update case priority.

        Update case priority

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case priority update payload
        :type body: CaseUpdatePriorityRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_priority_endpoint.call_with_http_info(**kwargs)

    def update_project(
        self,
        project_id: str,
        body: ProjectUpdateRequest,
    ) -> ProjectResponse:
        """Update a project.

        Update a project.

        :param project_id: Project UUID.
        :type project_id: str
        :param body: Project payload.
        :type body: ProjectUpdateRequest
        :rtype: ProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["body"] = body

        return self._update_project_endpoint.call_with_http_info(**kwargs)

    def update_project_notification_rule(
        self,
        project_id: str,
        notification_rule_id: str,
        body: CaseNotificationRuleUpdateRequest,
    ) -> None:
        """Update a notification rule.

        Update a notification rule.

        :param project_id: Project UUID
        :type project_id: str
        :param notification_rule_id: Notification Rule UUID
        :type notification_rule_id: str
        :param body: Notification rule payload
        :type body: CaseNotificationRuleUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["notification_rule_id"] = notification_rule_id

        kwargs["body"] = body

        return self._update_project_notification_rule_endpoint.call_with_http_info(**kwargs)

    def update_status(
        self,
        case_id: str,
        body: CaseUpdateStatusRequest,
    ) -> CaseResponse:
        """Update case status.

        Update case status

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case status update payload
        :type body: CaseUpdateStatusRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_status_endpoint.call_with_http_info(**kwargs)

    def watch_case(
        self,
        case_id: str,
        user_uuid: str,
    ) -> None:
        """Watch a case.

        Adds a user (identified by their UUID) as a watcher of a case. The user receives notifications about subsequent updates to the case.

        :param case_id: Case's UUID or key
        :type case_id: str
        :param user_uuid: The UUID of the user to add or remove as a watcher.
        :type user_uuid: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["user_uuid"] = user_uuid

        return self._watch_case_endpoint.call_with_http_info(**kwargs)
