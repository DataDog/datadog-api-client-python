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
    from datadog_api_client.v2.model.fleet_agent_detail_v2_attributes import FleetAgentDetailV2Attributes
    from datadog_api_client.v2.model.fleet_agent_v2_resource_type import FleetAgentV2ResourceType


class FleetAgentDetailV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_detail_v2_attributes import FleetAgentDetailV2Attributes
        from datadog_api_client.v2.model.fleet_agent_v2_resource_type import FleetAgentV2ResourceType

        return {
            "attributes": (FleetAgentDetailV2Attributes,),
            "id": (str,),
            "type": (FleetAgentV2ResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetAgentDetailV2Attributes, id: str, type: FleetAgentV2ResourceType, **kwargs):
        """
        Detailed information about a specific Datadog Agent.

        :param attributes: Attributes for the v2 agent detail response.
        :type attributes: FleetAgentDetailV2Attributes

        :param id: The unique agent key identifier.
        :type id: str

        :param type: The type of the agent resource.
        :type type: FleetAgentV2ResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
