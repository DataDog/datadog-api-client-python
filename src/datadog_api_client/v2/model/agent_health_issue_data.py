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
    from datadog_api_client.v2.model.agent_health_issue_attributes import AgentHealthIssueAttributes
    from datadog_api_client.v2.model.agent_health_issue_resource_type import AgentHealthIssueResourceType


class AgentHealthIssueData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_issue_attributes import AgentHealthIssueAttributes
        from datadog_api_client.v2.model.agent_health_issue_resource_type import AgentHealthIssueResourceType

        return {
            "attributes": (AgentHealthIssueAttributes,),
            "id": (str,),
            "type": (AgentHealthIssueResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AgentHealthIssueAttributes, id: str, type: AgentHealthIssueResourceType, **kwargs):
        """
        An open Agent Health issue.

        :param attributes: Attributes of an open Agent Health issue.
        :type attributes: AgentHealthIssueAttributes

        :param id: The unique identifier of the issue.
        :type id: str

        :param type: The Agent Health issue resource type.
        :type type: AgentHealthIssueResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
