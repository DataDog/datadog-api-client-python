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
from datadog_api_client.v2.model.replay_analysis_issues_response import ReplayAnalysisIssuesResponse
from datadog_api_client.v2.model.replay_analysis_issue_response import ReplayAnalysisIssueResponse
from datadog_api_client.v2.model.replay_analysis_issue_sessions_response import ReplayAnalysisIssueSessionsResponse


class RumReplayAnalysisApi:
    """
    Analyze RUM replay sessions to identify and investigate user-facing issues. Retrieve issues detected by AI analysis, get details for individual issues, and explore the sessions associated with each issue.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_replay_analysis_issue_endpoint = _Endpoint(
            settings={
                "response_type": (ReplayAnalysisIssueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/analysis/issues/{issue_id}",
                "operation_id": "get_replay_analysis_issue",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "issue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "issue_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_replay_analysis_issues_endpoint = _Endpoint(
            settings={
                "response_type": (ReplayAnalysisIssuesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/analysis/issues",
                "operation_id": "list_replay_analysis_issues",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_application_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[application_id]",
                    "location": "query",
                },
                "filter_severity": {
                    "openapi_types": (str,),
                    "attribute": "filter[severity]",
                    "location": "query",
                },
                "filter_view_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[view_name]",
                    "location": "query",
                },
                "filter_issue_category": {
                    "openapi_types": (str,),
                    "attribute": "filter[issue_category]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_replay_analysis_issue_sessions_endpoint = _Endpoint(
            settings={
                "response_type": (ReplayAnalysisIssueSessionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/analysis/issues/{issue_id}/sessions",
                "operation_id": "list_replay_analysis_issue_sessions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "issue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "issue_id",
                    "location": "path",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_replay_analysis_issue(
        self,
        issue_id: str,
    ) -> ReplayAnalysisIssueResponse:
        """Get replay analysis issue.

        Retrieve details of a specific RUM replay analysis issue by its identifier.

        :param issue_id: Unique identifier of the issue.
        :type issue_id: str
        :rtype: ReplayAnalysisIssueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        return self._get_replay_analysis_issue_endpoint.call_with_http_info(**kwargs)

    def list_replay_analysis_issues(
        self,
        *,
        filter_application_id: Union[str, UnsetType] = unset,
        filter_severity: Union[str, UnsetType] = unset,
        filter_view_name: Union[str, UnsetType] = unset,
        filter_issue_category: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> ReplayAnalysisIssuesResponse:
        """List replay analysis issues.

        Retrieve a paginated list of RUM replay analysis issues, optionally filtered by application, severity, view name, or issue category.

        :param filter_application_id: Filter issues by application UUID.
        :type filter_application_id: str, optional
        :param filter_severity: Filter issues by comma-separated severity values. Valid values are ``high`` , ``medium`` , and ``low``.
        :type filter_severity: str, optional
        :param filter_view_name: Filter issues by comma-separated view names.
        :type filter_view_name: str, optional
        :param filter_issue_category: Filter issues by comma-separated issue categories.
        :type filter_issue_category: str, optional
        :param sort: Sort order for the results. Valid values are ``created_at`` , ``-created_at`` , ``severity`` , ``-severity`` , ``session_count`` , and ``-session_count``. Defaults to ``-created_at``.
        :type sort: str, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param page_size: Number of items per page. Must be between 1 and 100.
        :type page_size: int, optional
        :rtype: ReplayAnalysisIssuesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_application_id is not unset:
            kwargs["filter_application_id"] = filter_application_id

        if filter_severity is not unset:
            kwargs["filter_severity"] = filter_severity

        if filter_view_name is not unset:
            kwargs["filter_view_name"] = filter_view_name

        if filter_issue_category is not unset:
            kwargs["filter_issue_category"] = filter_issue_category

        if sort is not unset:
            kwargs["sort"] = sort

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_replay_analysis_issues_endpoint.call_with_http_info(**kwargs)

    def list_replay_analysis_issue_sessions(
        self,
        issue_id: str,
        *,
        sort: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> ReplayAnalysisIssueSessionsResponse:
        """List replay analysis issue sessions.

        Retrieve a paginated list of sessions related to a specific RUM replay analysis issue.

        :param issue_id: Unique identifier of the issue.
        :type issue_id: str
        :param sort: Sort order for the results. Valid values are ``last_seen_at`` , ``-last_seen_at`` , ``proximity`` , and ``-proximity``. Defaults to ``-last_seen_at``.
        :type sort: str, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param page_size: Number of items per page. Must be between 1 and 100.
        :type page_size: int, optional
        :rtype: ReplayAnalysisIssueSessionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        if sort is not unset:
            kwargs["sort"] = sort

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_replay_analysis_issue_sessions_endpoint.call_with_http_info(**kwargs)
