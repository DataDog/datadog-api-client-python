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
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edges_data import (
        CustomTopologyMapInlineEdgesData,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_nodes_data import (
        CustomTopologyMapInlineNodesData,
    )


class CustomTopologyMapInlineData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edges_data import (
            CustomTopologyMapInlineEdgesData,
        )
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_nodes_data import (
            CustomTopologyMapInlineNodesData,
        )

        return {
            "edges": (CustomTopologyMapInlineEdgesData,),
            "nodes": (CustomTopologyMapInlineNodesData,),
        }

    attribute_map = {
        "edges": "edges",
        "nodes": "nodes",
    }

    def __init__(
        self_,
        edges: Union[CustomTopologyMapInlineEdgesData, UnsetType] = unset,
        nodes: Union[CustomTopologyMapInlineNodesData, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param edges: Test-only generated schema for the dashboard versioning proof of concept.
        :type edges: CustomTopologyMapInlineEdgesData, optional

        :param nodes: Test-only generated schema for the dashboard versioning proof of concept.
        :type nodes: CustomTopologyMapInlineNodesData, optional
        """
        if edges is not unset:
            kwargs["edges"] = edges
        if nodes is not unset:
            kwargs["nodes"] = nodes
        super().__init__(kwargs)
