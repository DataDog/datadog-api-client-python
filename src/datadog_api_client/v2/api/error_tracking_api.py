# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.issues_search_response import IssuesSearchResponse
from datadog_api_client.v2.model.search_issues_include_query_parameter_item import SearchIssuesIncludeQueryParameterItem
from datadog_api_client.v2.model.issues_search_request import IssuesSearchRequest
from datadog_api_client.v2.model.issue_response import IssueResponse
from datadog_api_client.v2.model.get_issue_include_query_parameter_item import GetIssueIncludeQueryParameterItem
from datadog_api_client.v2.model.issue_update_assignee_request import IssueUpdateAssigneeRequest
from datadog_api_client.v2.model.issue_update_state_request import IssueUpdateStateRequest


class ErrorTrackingApi:
    """
    View and manage issues within Error Tracking. See the `Error Tracking page <https://docs.datadoghq.com/error_tracking/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_issue_assignee_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/error-tracking/issues/{issue_id}/assignee",
                "operation_id": "delete_issue_assignee",
                "http_method": "DELETE",
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
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_issue_endpoint = _Endpoint(
            settings={
                "response_type": (IssueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/error-tracking/issues/{issue_id}",
                "operation_id": "get_issue",
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
                "include": {
                    "openapi_types": ([GetIssueIncludeQueryParameterItem],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_issues_endpoint = _Endpoint(
            settings={
                "response_type": (IssuesSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/error-tracking/issues/search",
                "operation_id": "search_issues",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([SearchIssuesIncludeQueryParameterItem],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IssuesSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_issue_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (IssueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/error-tracking/issues/{issue_id}/assignee",
                "operation_id": "update_issue_assignee",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "issue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "issue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IssueUpdateAssigneeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_issue_state_endpoint = _Endpoint(
            settings={
                "response_type": (IssueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/error-tracking/issues/{issue_id}/state",
                "operation_id": "update_issue_state",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "issue_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "issue_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IssueUpdateStateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_issue_assignee(
        self,
        issue_id: str,
    ) -> None:
        """Remove the assignee of an issue.

        Remove the assignee of an issue by ``issue_id``.

        :param issue_id: The identifier of the issue.
        :type issue_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        return self._delete_issue_assignee_endpoint.call_with_http_info(**kwargs)

    def get_issue(
        self,
        issue_id: str,
        *,
        include: Union[List[GetIssueIncludeQueryParameterItem], UnsetType] = unset,
    ) -> IssueResponse:
        """Get the details of an error tracking issue.

        Retrieve the full details for a specific error tracking issue, including attributes and relationships.

        :param issue_id: The identifier of the issue.
        :type issue_id: str
        :param include: Comma-separated list of relationship objects that should be included in the response. Possible values are ``assignee`` , ``case`` , and ``team_owners``.
        :type include: [GetIssueIncludeQueryParameterItem], optional
        :rtype: IssueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_issue_endpoint.call_with_http_info(**kwargs)

    def search_issues(
        self,
        body: IssuesSearchRequest,
        *,
        include: Union[List[SearchIssuesIncludeQueryParameterItem], UnsetType] = unset,
    ) -> IssuesSearchResponse:
        """Search error tracking issues.

        Search issues endpoint allows you to programmatically search for issues within your organization. This endpoint returns a list of issues that match a given search query, following the event search syntax. The search results are limited to a maximum of 100 issues per request.

        :param body: Search issues request payload.
        :type body: IssuesSearchRequest
        :param include: Comma-separated list of relationship objects that should be included in the response. Possible values are ``issue`` , ``issue.assignee`` , ``issue.case`` , and ``issue.team_owners``.
        :type include: [SearchIssuesIncludeQueryParameterItem], optional
        :rtype: IssuesSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._search_issues_endpoint.call_with_http_info(**kwargs)

    def update_issue_assignee(
        self,
        issue_id: str,
        body: IssueUpdateAssigneeRequest,
    ) -> IssueResponse:
        """Update the assignee of an issue.

        Update the assignee of an issue by ``issue_id``.

        :param issue_id: The identifier of the issue.
        :type issue_id: str
        :param body: Update issue assignee request payload.
        :type body: IssueUpdateAssigneeRequest
        :rtype: IssueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        kwargs["body"] = body

        return self._update_issue_assignee_endpoint.call_with_http_info(**kwargs)

    def update_issue_state(
        self,
        issue_id: str,
        body: IssueUpdateStateRequest,
    ) -> IssueResponse:
        """Update the state of an issue.

        Update the state of an issue by ``issue_id``. Use this endpoint to move an issue between states such as ``OPEN`` , ``RESOLVED`` , or ``IGNORED``.

        :param issue_id: The identifier of the issue.
        :type issue_id: str
        :param body: Update issue state request payload.
        :type body: IssueUpdateStateRequest
        :rtype: IssueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        kwargs["body"] = body

        return self._update_issue_state_endpoint.call_with_http_info(**kwargs)
