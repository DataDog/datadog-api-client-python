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
    from datadog_api_client.v2.model.csm_agentless_host_facet_data import CsmAgentlessHostFacetData


class CsmAgentlessHostFacetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agentless_host_facet_data import CsmAgentlessHostFacetData

        return {
            "data": ([CsmAgentlessHostFacetData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CsmAgentlessHostFacetData], **kwargs):
        """
        The response returned when listing facets for agentless hosts.

        :param data: The list of available facets for agentless hosts.
        :type data: [CsmAgentlessHostFacetData]
        """
        super().__init__(kwargs)

        self_.data = data
