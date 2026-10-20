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
    from datadog_api_client.v2.model.agent_health_host_issues_attributes import AgentHealthHostIssuesAttributes
    from datadog_api_client.v2.model.agent_health_host_issues_type import AgentHealthHostIssuesType


class AgentHealthHostIssuesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_host_issues_attributes import AgentHealthHostIssuesAttributes
        from datadog_api_client.v2.model.agent_health_host_issues_type import AgentHealthHostIssuesType

        return {
            "attributes": (AgentHealthHostIssuesAttributes,),
            "id": (str,),
            "type": (AgentHealthHostIssuesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AgentHealthHostIssuesAttributes, id: str, type: AgentHealthHostIssuesType, **kwargs
    ):
        """
        Agent Health issue data for a resource.

        :param attributes: Active Agent Health issues for a resource.
        :type attributes: AgentHealthHostIssuesAttributes

        :param id: The resource identifier.
        :type id: str

        :param type: The Agent Health issue resource type.
        :type type: AgentHealthHostIssuesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
