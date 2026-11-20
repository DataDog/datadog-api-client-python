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
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column_id import (
        CustomTopologyMapInlineEdgeColumnId,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column_kind import (
        CustomTopologyMapInlineEdgeColumnKind,
    )


class CustomTopologyMapInlineEdgeColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column_id import (
            CustomTopologyMapInlineEdgeColumnId,
        )
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column_kind import (
            CustomTopologyMapInlineEdgeColumnKind,
        )

        return {
            "id": (CustomTopologyMapInlineEdgeColumnId,),
            "kind": (CustomTopologyMapInlineEdgeColumnKind,),
            "values": ([str],),
        }

    attribute_map = {
        "id": "id",
        "kind": "kind",
        "values": "values",
    }

    def __init__(
        self_,
        id: CustomTopologyMapInlineEdgeColumnId,
        kind: CustomTopologyMapInlineEdgeColumnKind,
        values: List[str],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param id: Test-only generated schema for the dashboard versioning proof of concept.
        :type id: CustomTopologyMapInlineEdgeColumnId

        :param kind: Test-only generated schema for the dashboard versioning proof of concept.
        :type kind: CustomTopologyMapInlineEdgeColumnKind

        :param values: Test-only generated schema for the dashboard versioning proof of concept.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.id = id
        self_.kind = kind
        self_.values = values
