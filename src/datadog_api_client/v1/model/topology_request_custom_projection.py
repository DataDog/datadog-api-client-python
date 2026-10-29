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
    from datadog_api_client.v1.model.topology_request_custom_projection_dimension import (
        TopologyRequestCustomProjectionDimension,
    )
    from datadog_api_client.v1.model.topology_request_custom_projection_type import TopologyRequestCustomProjectionType


class TopologyRequestCustomProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_request_custom_projection_dimension import (
            TopologyRequestCustomProjectionDimension,
        )
        from datadog_api_client.v1.model.topology_request_custom_projection_type import (
            TopologyRequestCustomProjectionType,
        )

        return {
            "dimensions": ([TopologyRequestCustomProjectionDimension],),
            "type": (TopologyRequestCustomProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(
        self_,
        dimensions: List[TopologyRequestCustomProjectionDimension],
        type: TopologyRequestCustomProjectionType,
        **kwargs,
    ):
        """
        Mapping from result columns to node fields. Each result row feeds one node.

        :param dimensions: List of mappings from a result column to a node field. Each ``dimension`` must be unique.
        :type dimensions: [TopologyRequestCustomProjectionDimension]

        :param type: Projection type. Each result row is a node.
        :type type: TopologyRequestCustomProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
