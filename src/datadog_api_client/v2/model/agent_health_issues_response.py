# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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

    def __init__(self_, data: List[AgentHealthIssueData], meta: AgentHealthIssuesResponseMeta, **kwargs):
        """
        A paginated response containing open Agent Health issues.

        :param data: The open Agent Health issues on this page.
        :type data: [AgentHealthIssueData]

        :param meta: Pagination metadata for the matching Agent Health issues.
        :type meta: AgentHealthIssuesResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
