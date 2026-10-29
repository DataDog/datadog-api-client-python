# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.topology_map_inline_column_kind_scalar import TopologyMapInlineColumnKindScalar
    from datadog_api_client.v1.model.topology_map_inline_node_value_column_meta import (
        TopologyMapInlineNodeValueColumnMeta,
    )


class TopologyMapInlineNodeValueColumn(ModelNormal):
    validations = {
        "id": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_map_inline_column_kind_scalar import TopologyMapInlineColumnKindScalar
        from datadog_api_client.v1.model.topology_map_inline_node_value_column_meta import (
            TopologyMapInlineNodeValueColumnMeta,
        )

        return {
            "id": (str,),
            "kind": (TopologyMapInlineColumnKindScalar,),
            "meta": (TopologyMapInlineNodeValueColumnMeta,),
            "values": ([float, none_type],),
        }

    attribute_map = {
        "id": "id",
        "kind": "kind",
        "meta": "meta",
        "values": "values",
    }

    def __init__(
        self_,
        id: str,
        kind: TopologyMapInlineColumnKindScalar,
        values: List[float],
        meta: Union[TopologyMapInlineNodeValueColumnMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Column of numeric node values. Nodes display non-null values in order of column ``id``.

        :param id: Position of the value in the node, as ``values[N]``. The smallest N appears first.
        :type id: str

        :param kind: Column of numbers.
        :type kind: TopologyMapInlineColumnKindScalar

        :param meta: Display options for a value column.
        :type meta: TopologyMapInlineNodeValueColumnMeta, optional

        :param values: Value for each node. Null values are not displayed.
        :type values: [float, none_type]
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.id = id
        self_.kind = kind
        self_.values = values
