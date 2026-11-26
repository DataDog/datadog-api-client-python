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
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_value_column_kind import (
        CustomTopologyMapInlineNodeValueColumnKind,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_value_column_meta import (
        CustomTopologyMapInlineNodeValueColumnMeta,
    )


class CustomTopologyMapInlineNodeValueColumn(ModelNormal):
    validations = {
        "id": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_value_column_kind import (
            CustomTopologyMapInlineNodeValueColumnKind,
        )
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_value_column_meta import (
            CustomTopologyMapInlineNodeValueColumnMeta,
        )

        return {
            "id": (str,),
            "kind": (CustomTopologyMapInlineNodeValueColumnKind,),
            "meta": (CustomTopologyMapInlineNodeValueColumnMeta,),
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
        kind: CustomTopologyMapInlineNodeValueColumnKind,
        values: List[float],
        meta: Union[CustomTopologyMapInlineNodeValueColumnMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param id: Test-only generated schema for the dashboard versioning proof of concept.
        :type id: str

        :param kind: Test-only generated schema for the dashboard versioning proof of concept.
        :type kind: CustomTopologyMapInlineNodeValueColumnKind

        :param meta: Test-only generated schema for the dashboard versioning proof of concept.
        :type meta: CustomTopologyMapInlineNodeValueColumnMeta, optional

        :param values: Test-only generated schema for the dashboard versioning proof of concept.
        :type values: [float, none_type]
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.id = id
        self_.kind = kind
        self_.values = values
