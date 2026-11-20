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
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_column import (
        CustomTopologyMapInlineNodeColumn,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_id_column import (
        CustomTopologyMapInlineNodeIdColumn,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_string_column import (
        CustomTopologyMapInlineNodeStringColumn,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_value_column import (
        CustomTopologyMapInlineNodeValueColumn,
    )


class CustomTopologyMapInlineNodesData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_node_column import (
            CustomTopologyMapInlineNodeColumn,
        )

        return {
            "columns": ([CustomTopologyMapInlineNodeColumn],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(
        self_,
        columns: List[
            Union[
                CustomTopologyMapInlineNodeColumn,
                CustomTopologyMapInlineNodeIdColumn,
                CustomTopologyMapInlineNodeStringColumn,
                CustomTopologyMapInlineNodeValueColumn,
            ]
        ],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [CustomTopologyMapInlineNodeColumn]
        """
        super().__init__(kwargs)

        self_.columns = columns
