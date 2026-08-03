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
    from datadog_api_client.v2.model.fleet_agent_detail_v2 import FleetAgentDetailV2


class FleetAgentDetailV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_detail_v2 import FleetAgentDetailV2

        return {
            "data": (FleetAgentDetailV2,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetAgentDetailV2, **kwargs):
        """
        Response containing detailed information about a specific Datadog Agent.

        :param data: Detailed information about a specific Datadog Agent.
        :type data: FleetAgentDetailV2
        """
        super().__init__(kwargs)

        self_.data = data
