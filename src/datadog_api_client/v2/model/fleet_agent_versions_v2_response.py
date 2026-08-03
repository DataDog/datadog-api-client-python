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
    from datadog_api_client.v2.model.fleet_agent_version_v2 import FleetAgentVersionV2
    from datadog_api_client.v2.model.fleet_agent_versions_v2_response_meta import FleetAgentVersionsV2ResponseMeta


class FleetAgentVersionsV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_version_v2 import FleetAgentVersionV2
        from datadog_api_client.v2.model.fleet_agent_versions_v2_response_meta import FleetAgentVersionsV2ResponseMeta

        return {
            "data": ([FleetAgentVersionV2],),
            "meta": (FleetAgentVersionsV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[FleetAgentVersionV2],
        meta: Union[FleetAgentVersionsV2ResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of available Datadog Agent versions.

        :param data: Array of available agent versions.
        :type data: [FleetAgentVersionV2]

        :param meta: Metadata for the v2 list of agent versions.
        :type meta: FleetAgentVersionsV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
