# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.topology_map_inline_edges_data import TopologyMapInlineEdgesData
    from datadog_api_client.v1.model.topology_map_inline_nodes_data import TopologyMapInlineNodesData


class TopologyMapInlineData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_edges_data import TopologyMapInlineEdgesData
        from datadog_api_client.v1.model.topology_map_inline_nodes_data import TopologyMapInlineNodesData

        return {
            "edges": (TopologyMapInlineEdgesData,),
            "nodes": (TopologyMapInlineNodesData,),
        }

    attribute_map = {
        "edges": "edges",
        "nodes": "nodes",
    }

    def __init__(
        self_,
        edges: Union[TopologyMapInlineEdgesData, UnsetType] = unset,
        nodes: Union[TopologyMapInlineNodesData, UnsetType] = unset,
        **kwargs,
    ):
        """
        Static nodes and edges, stored in columns. Within a table, every column must have the same number of values and a unique ``id``.

        :param edges: Table of edges, one row per edge.
        :type edges: TopologyMapInlineEdgesData, optional

        :param nodes: Table of nodes, one row per node.
        :type nodes: TopologyMapInlineNodesData, optional
        """
        if edges is not unset:
            kwargs["edges"] = edges
        if nodes is not unset:
            kwargs["nodes"] = nodes
        super().__init__(kwargs)
