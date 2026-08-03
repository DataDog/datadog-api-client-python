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
    from datadog_api_client.v2.model.fleet_agent_version_v2_attributes import FleetAgentVersionV2Attributes
    from datadog_api_client.v2.model.fleet_agent_version_v2_resource_type import FleetAgentVersionV2ResourceType


class FleetAgentVersionV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_version_v2_attributes import FleetAgentVersionV2Attributes
        from datadog_api_client.v2.model.fleet_agent_version_v2_resource_type import FleetAgentVersionV2ResourceType

        return {
            "attributes": (FleetAgentVersionV2Attributes,),
            "id": (str,),
            "type": (FleetAgentVersionV2ResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: FleetAgentVersionV2Attributes, id: str, type: FleetAgentVersionV2ResourceType, **kwargs
    ):
        """
        An available Datadog Agent version resource.

        :param attributes: Attributes of an available Datadog Agent version.
        :type attributes: FleetAgentVersionV2Attributes

        :param id: The agent version string used as the unique identifier.
        :type id: str

        :param type: The type of the agent version resource.
        :type type: FleetAgentVersionV2ResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
