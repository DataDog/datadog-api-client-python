# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.topology_map_inline_node_string_column_id import (
        TopologyMapInlineNodeStringColumnId,
    )
    from datadog_api_client.v1.model.topology_map_inline_column_kind_string import TopologyMapInlineColumnKindString


class TopologyMapInlineNodeStringColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_node_string_column_id import (
            TopologyMapInlineNodeStringColumnId,
        )
        from datadog_api_client.v1.model.topology_map_inline_column_kind_string import TopologyMapInlineColumnKindString

        return {
            "id": (TopologyMapInlineNodeStringColumnId,),
            "kind": (TopologyMapInlineColumnKindString,),
            "values": ([str, none_type],),
        }

    attribute_map = {
        "id": "id",
        "kind": "kind",
        "values": "values",
    }

    def __init__(
        self_,
        id: TopologyMapInlineNodeStringColumnId,
        kind: TopologyMapInlineColumnKindString,
        values: List[str],
        **kwargs,
    ):
        """
        Column of node text.

        :param id: Node field the column fills. ``title`` is bold text at the top of the node; ``subtitle`` is smaller text below it.
        :type id: TopologyMapInlineNodeStringColumnId

        :param kind: Column of strings.
        :type kind: TopologyMapInlineColumnKindString

        :param values: Text for each node. A null ``title`` shows the node's ID; a null ``subtitle`` shows no subtitle.
        :type values: [str, none_type]
        """
        super().__init__(kwargs)

        self_.id = id
        self_.kind = kind
        self_.values = values
