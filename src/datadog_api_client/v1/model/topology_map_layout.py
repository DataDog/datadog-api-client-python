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
    from datadog_api_client.v1.model.topology_map_layout_direction import TopologyMapLayoutDirection
    from datadog_api_client.v1.model.topology_map_layout_type import TopologyMapLayoutType


class TopologyMapLayout(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_layout_direction import TopologyMapLayoutDirection
        from datadog_api_client.v1.model.topology_map_layout_type import TopologyMapLayoutType

        return {
            "direction": (TopologyMapLayoutDirection,),
            "type": (TopologyMapLayoutType,),
        }

    attribute_map = {
        "direction": "direction",
        "type": "type",
    }

    def __init__(self_, direction: TopologyMapLayoutDirection, type: TopologyMapLayoutType, **kwargs):
        """
        Algorithm that positions nodes and edges. The ``hierarchical`` layout places nodes in ranks so edges flow in one direction.

        :param direction: Direction of ranks. For example, ``top-to-bottom`` places first-rank nodes at the top and last-rank nodes at the bottom.
        :type direction: TopologyMapLayoutDirection

        :param type: Type of layout algorithm.
        :type type: TopologyMapLayoutType
        """
        super().__init__(kwargs)

        self_.direction = direction
        self_.type = type
