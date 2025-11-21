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
    from datadog_api_client.v2.model.fleet_agent_info_attributes import FleetAgentInfoAttributes
    from datadog_api_client.v2.model.fleet_agent_info_resource_type import FleetAgentInfoResourceType


class FleetAgentInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_info_attributes import FleetAgentInfoAttributes
        from datadog_api_client.v2.model.fleet_agent_info_resource_type import FleetAgentInfoResourceType

        return {
            "attributes": (FleetAgentInfoAttributes,),
            "id": (str,),
            "type": (FleetAgentInfoResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetAgentInfoAttributes, id: str, type: FleetAgentInfoResourceType, **kwargs):
        """
        Represents detailed information about a specific Datadog Agent.

        :param attributes: Attributes for agent information.
        :type attributes: FleetAgentInfoAttributes

        :param id: The unique agent key identifier.
        :type id: str

        :param type: The type of Agent info resource.
        :type type: FleetAgentInfoResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
