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
    from datadog_api_client.v2.model.agent_health_host_issue import AgentHealthHostIssue


class AgentHealthHostIssuesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_host_issue import AgentHealthHostIssue

        return {
            "issues": ([AgentHealthHostIssue],),
        }

    attribute_map = {
        "issues": "issues",
    }

    def __init__(self_, issues: List[AgentHealthHostIssue], **kwargs):
        """
        Active Agent Health issues for a resource.

        :param issues: The active issues and their reconciliation metadata.
        :type issues: [AgentHealthHostIssue]
        """
        super().__init__(kwargs)

        self_.issues = issues
