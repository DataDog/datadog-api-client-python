# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.agent_health_issue_data import AgentHealthIssueData
    from datadog_api_client.v2.model.agent_health_issues_response_meta import AgentHealthIssuesResponseMeta


class AgentHealthIssuesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_issue_data import AgentHealthIssueData
        from datadog_api_client.v2.model.agent_health_issues_response_meta import AgentHealthIssuesResponseMeta

        return {
            "data": ([AgentHealthIssueData],),
            "meta": (AgentHealthIssuesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[AgentHealthIssueData], meta: Union[AgentHealthIssuesResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        A response containing open Agent Health issues.

        :param data: The open Agent Health issues matching the request.
        :type data: [AgentHealthIssueData]

        :param meta: Aggregate counts for the matching Agent Health issues. Present only when ``count_by=issue_type`` is requested.
        :type meta: AgentHealthIssuesResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
