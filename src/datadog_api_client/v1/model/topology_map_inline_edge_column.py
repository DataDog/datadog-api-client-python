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
    from datadog_api_client.v1.model.topology_map_inline_edge_column_id import TopologyMapInlineEdgeColumnId
    from datadog_api_client.v1.model.topology_map_inline_column_kind_string import TopologyMapInlineColumnKindString


class TopologyMapInlineEdgeColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_edge_column_id import TopologyMapInlineEdgeColumnId
        from datadog_api_client.v1.model.topology_map_inline_column_kind_string import TopologyMapInlineColumnKindString

        return {
            "id": (TopologyMapInlineEdgeColumnId,),
            "kind": (TopologyMapInlineColumnKindString,),
            "values": ([str],),
        }

    attribute_map = {
        "id": "id",
        "kind": "kind",
        "values": "values",
    }

    def __init__(
        self_, id: TopologyMapInlineEdgeColumnId, kind: TopologyMapInlineColumnKindString, values: List[str], **kwargs
    ):
        """
        Column of edge endpoint node IDs.

        :param id: Edge endpoint the column holds.
        :type id: TopologyMapInlineEdgeColumnId

        :param kind: Column of strings.
        :type kind: TopologyMapInlineColumnKindString

        :param values: Node IDs.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.id = id
        self_.kind = kind
        self_.values = values
