# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.topology_map_inline_node_column import TopologyMapInlineNodeColumn
    from datadog_api_client.v1.model.topology_map_inline_node_id_column import TopologyMapInlineNodeIdColumn
    from datadog_api_client.v1.model.topology_map_inline_node_string_column import TopologyMapInlineNodeStringColumn
    from datadog_api_client.v1.model.topology_map_inline_node_value_column import TopologyMapInlineNodeValueColumn


class TopologyMapInlineNodesData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_node_column import TopologyMapInlineNodeColumn

        return {
            "columns": ([TopologyMapInlineNodeColumn],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(
        self_,
        columns: List[
            Union[
                TopologyMapInlineNodeColumn,
                TopologyMapInlineNodeIdColumn,
                TopologyMapInlineNodeStringColumn,
                TopologyMapInlineNodeValueColumn,
            ]
        ],
        **kwargs,
    ):
        """
        Table of nodes, one row per node.

        :param columns: Columns of the nodes table. Must include an ``id`` column, unless the list is empty (no nodes).
        :type columns: [TopologyMapInlineNodeColumn]
        """
        super().__init__(kwargs)

        self_.columns = columns
