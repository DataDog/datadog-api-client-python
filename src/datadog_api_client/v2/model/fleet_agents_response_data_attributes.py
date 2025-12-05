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
    from datadog_api_client.v2.model.fleet_agent_attributes import FleetAgentAttributes


class FleetAgentsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_attributes import FleetAgentAttributes

        return {
            "agents": ([FleetAgentAttributes],),
        }

    attribute_map = {
        "agents": "agents",
    }

    def __init__(self_, agents: Union[List[FleetAgentAttributes], UnsetType] = unset, **kwargs):
        """


        :param agents: Array of agents matching the query criteria.
        :type agents: [FleetAgentAttributes], optional
        """
        if agents is not unset:
            kwargs["agents"] = agents
        super().__init__(kwargs)
