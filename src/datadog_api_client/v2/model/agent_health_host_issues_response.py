# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.agent_health_host_issues_data import AgentHealthHostIssuesData


class AgentHealthHostIssuesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_host_issues_data import AgentHealthHostIssuesData

        return {
            "data": (AgentHealthHostIssuesData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AgentHealthHostIssuesData, **kwargs):
        """
        Response containing the active Agent Health issues for a resource.

        :param data: Agent Health issue data for a resource.
        :type data: AgentHealthHostIssuesData
        """
        super().__init__(kwargs)

        self_.data = data
