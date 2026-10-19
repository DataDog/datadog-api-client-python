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


class AgentHealthApi:
    """
    View Agent Health issues reported for node Agents and Cluster Agents.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

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
