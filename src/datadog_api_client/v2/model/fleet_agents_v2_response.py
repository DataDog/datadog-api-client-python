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
    from datadog_api_client.v2.model.fleet_agent_v2 import FleetAgentV2
    from datadog_api_client.v2.model.fleet_agents_v2_response_meta import FleetAgentsV2ResponseMeta


class FleetAgentsV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_v2 import FleetAgentV2
        from datadog_api_client.v2.model.fleet_agents_v2_response_meta import FleetAgentsV2ResponseMeta

        return {
            "data": ([FleetAgentV2],),
            "meta": (FleetAgentsV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[FleetAgentV2], meta: Union[FleetAgentsV2ResponseMeta, UnsetType] = unset, **kwargs):
        """
        Response containing a paginated list of Datadog Agents.

        :param data: Array of agents matching the query criteria.
        :type data: [FleetAgentV2]

        :param meta: Metadata for the v2 list of agents, including pagination information.
        :type meta: FleetAgentsV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
