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
    from datadog_api_client.v2.model.fleet_agent_version import FleetAgentVersion


class FleetAgentVersionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_version import FleetAgentVersion

        return {
            "data": ([FleetAgentVersion],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[FleetAgentVersion], **kwargs):
        """
        Response containing a list of available Agent versions.

        :param data: Array of available Agent versions.
        :type data: [FleetAgentVersion]
        """
        super().__init__(kwargs)

        self_.data = data
