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
from datadog_api_client.v2.model.agent_health_host_issues_response import AgentHealthHostIssuesResponse
from datadog_api_client.v2.model.agent_health_agent_type import AgentHealthAgentType
from datadog_api_client.v2.model.agent_health_issues_response import AgentHealthIssuesResponse
from datadog_api_client.v2.model.agent_health_issues_count_by import AgentHealthIssuesCountBy
from datadog_api_client.v2.model.agent_health_issue_response import AgentHealthIssueResponse


class AgentHealthApi:
    """
    List open Agent Health issues across your organization and get an issue with its available remediation. Issues are reported by node Agents, Cluster Agents, and OpenTelemetry collectors. The meaning of ``resource_id`` depends on ``resource_kind`` : hostname for ``host`` , DaemonSet UID for ``deployment`` (node Agent), cluster UUID for ``cluster`` , hostname of the host running the Cluster Agent for ``cluster_agent`` , or OpenTelemetry collector ID for ``otel``.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_agent_health_issue_endpoint = _Endpoint(
            settings={
                "response_type": (AgentHealthIssueResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/agenthealth/issues/{issue_id}",
                "operation_id": "get_agent_health_issue",
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

        self._list_agent_health_host_issues_endpoint = _Endpoint(
            settings={
                "response_type": (AgentHealthHostIssuesResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/agenthealth/hosts/{resource_id}/issues",
                "operation_id": "list_agent_health_host_issues",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "agent_type": {
                    "openapi_types": (AgentHealthAgentType,),
                    "attribute": "agent_type",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_agent_health_issues_endpoint = _Endpoint(
            settings={
                "response_type": (AgentHealthIssuesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/agenthealth/issues",
                "operation_id": "list_agent_health_issues",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "count_by": {
                    "openapi_types": (AgentHealthIssuesCountBy,),
                    "attribute": "count_by",
                    "location": "query",
                },
                "filter_severity": {
                    "validation": {
                        "max_length": 12850,
                    },
                    "openapi_types": (str,),
                    "attribute": "filter[severity]",
                    "location": "query",
                },
                "filter_category": {
                    "validation": {
                        "max_length": 12850,
                    },
                    "openapi_types": (str,),
                    "attribute": "filter[category]",
                    "location": "query",
                },
                "filter_issue_type": {
                    "validation": {
                        "max_length": 12850,
                    },
                    "openapi_types": (str,),
                    "attribute": "filter[issue_type]",
                    "location": "query",
                },
                "filter_resource_kind": {
                    "validation": {
                        "max_length": 12850,
                    },
                    "openapi_types": (str,),
                    "attribute": "filter[resource_kind]",
                    "location": "query",
                },
                "filter_resource_id": {
                    "validation": {
                        "max_length": 12850,
                    },
                    "openapi_types": (str,),
                    "attribute": "filter[resource_id]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_agent_health_issue(
        self,
        issue_id: str,
    ) -> AgentHealthIssueResponse:
        """Get an Agent Health issue.

        Get an Agent Health issue and its available remediation in your organization.
        Only open issues are returned. The ``remediation`` attribute is omitted when
        the issue has no remediation.

        Returns ``404`` if the issue does not exist, is not open, belongs to another
        organization, or you do not have access to its data. This response does not
        reveal whether the issue exists. Returns ``403`` if you lack the ``hosts_read`` permission.

        :param issue_id: The unique identifier of the issue. It can contain ``:`` and must be percent-encoded
            by clients when included in the path.
        :type issue_id: str
        :rtype: AgentHealthIssueResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["issue_id"] = issue_id

        return self._get_agent_health_issue_endpoint.call_with_http_info(**kwargs)

    def list_agent_health_host_issues(
        self,
        resource_id: str,
        *,
        agent_type: Union[AgentHealthAgentType, UnsetType] = unset,
    ) -> AgentHealthHostIssuesResponse:
        """List active Agent Health issues.

        Returns the active Agent Health issues for a node Agent or Cluster Agent resource.

        :param resource_id: Resource identifier whose active Agent Health issues should be returned: a DaemonSet UID for a node Agent or a cluster UUID for a Cluster Agent.
        :type resource_id: str
        :param agent_type: Agent type associated with the resource. Defaults to ``node`` when omitted.
        :type agent_type: AgentHealthAgentType, optional
        :rtype: AgentHealthHostIssuesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        if agent_type is not unset:
            kwargs["agent_type"] = agent_type

        return self._list_agent_health_host_issues_endpoint.call_with_http_info(**kwargs)

    def list_agent_health_issues(
        self,
        *,
        count_by: Union[AgentHealthIssuesCountBy, UnsetType] = unset,
        filter_severity: Union[str, UnsetType] = unset,
        filter_category: Union[str, UnsetType] = unset,
        filter_issue_type: Union[str, UnsetType] = unset,
        filter_resource_kind: Union[str, UnsetType] = unset,
        filter_resource_id: Union[str, UnsetType] = unset,
    ) -> AgentHealthIssuesResponse:
        """List Agent Health issues.

        List open Agent Health issues across your organization. Returns ``403`` if you
        lack the ``hosts_read`` permission.

        Each item in ``data`` is a JSON:API resource object whose ``attributes`` hold the issue
        fields, including its ``issue_type``. Issues use a stable order: severity rank
        ( ``high`` , ``medium`` , ``low`` , then other values), then ``first_seen_at`` descending with
        missing timestamps last, then issue ID ascending.

        Set ``count_by=issue_type`` to include ``meta.page`` , where ``total_count`` is the number of
        open issues matching the filters and ``counts_by_issue_type`` holds the per-type counts.
        ``meta`` is omitted when ``count_by`` is not requested.

        Each filter accepts up to 50 comma-separated exact values of at most 256 characters
        each, combined with OR within a filter and AND across filters. Blank entries are ignored; an all-blank filter
        is treated as absent.

        :param count_by: Set to ``issue_type`` to include ``meta.page`` with ``total_count`` and per-issue-type counts. If you don't set this parameter, the response omits ``meta``. Only ``issue_type`` is supported.
        :type count_by: AgentHealthIssuesCountBy, optional
        :param filter_severity: Filter by a comma-separated list of exact ``severity`` values, up to 50 values
            of at most 256 characters each. Values are combined with OR within this filter and AND across filters.
            Blank entries are ignored; an all-blank filter is treated as absent.
        :type filter_severity: str, optional
        :param filter_category: Filter by a comma-separated list of exact ``category`` values, up to 50 values
            of at most 256 characters each. Values are combined with OR within this filter and AND across filters.
            Blank entries are ignored; an all-blank filter is treated as absent.
        :type filter_category: str, optional
        :param filter_issue_type: Filter by a comma-separated list of exact ``issue_type`` values, up to 50 values
            of at most 256 characters each. Values are combined with OR within this filter and AND across filters.
            Blank entries are ignored; an all-blank filter is treated as absent.
        :type filter_issue_type: str, optional
        :param filter_resource_kind: Filter by a comma-separated list of exact ``resource_kind`` values, up to 50 values
            of at most 256 characters each. Values are combined with OR within this filter and AND across filters.
            Blank entries are ignored; an all-blank filter is treated as absent.
        :type filter_resource_kind: str, optional
        :param filter_resource_id: Filter by a comma-separated list of exact ``resource_id`` values, up to 50 values
            of at most 256 characters each. Values are combined with OR within this filter and AND across filters.
            Blank entries are ignored; an all-blank filter is treated as absent.
        :type filter_resource_id: str, optional
        :rtype: AgentHealthIssuesResponse
        """
        kwargs: Dict[str, Any] = {}
        if count_by is not unset:
            kwargs["count_by"] = count_by

        if filter_severity is not unset:
            kwargs["filter_severity"] = filter_severity

        if filter_category is not unset:
            kwargs["filter_category"] = filter_category

        if filter_issue_type is not unset:
            kwargs["filter_issue_type"] = filter_issue_type

        if filter_resource_kind is not unset:
            kwargs["filter_resource_kind"] = filter_resource_kind

        if filter_resource_id is not unset:
            kwargs["filter_resource_id"] = filter_resource_id

        return self._list_agent_health_issues_endpoint.call_with_http_info(**kwargs)
