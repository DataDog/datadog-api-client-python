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
    from datadog_api_client.v1.model.topology_map_inline_edge_column import TopologyMapInlineEdgeColumn


class TopologyMapInlineEdgesData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_edge_column import TopologyMapInlineEdgeColumn

        return {
            "columns": ([TopologyMapInlineEdgeColumn],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(self_, columns: List[TopologyMapInlineEdgeColumn], **kwargs):
        """
        Table of edges, one row per edge.

        :param columns: Columns of the edges table. Must include one ``source`` column and one ``target`` column.
        :type columns: [TopologyMapInlineEdgeColumn]
        """
        super().__init__(kwargs)

        self_.columns = columns
