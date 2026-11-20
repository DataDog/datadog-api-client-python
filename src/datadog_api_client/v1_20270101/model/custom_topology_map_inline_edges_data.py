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
    from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column import (
        CustomTopologyMapInlineEdgeColumn,
    )


class CustomTopologyMapInlineEdgesData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_inline_edge_column import (
            CustomTopologyMapInlineEdgeColumn,
        )

        return {
            "columns": ([CustomTopologyMapInlineEdgeColumn],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(self_, columns: List[CustomTopologyMapInlineEdgeColumn], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [CustomTopologyMapInlineEdgeColumn]
        """
        super().__init__(kwargs)

        self_.columns = columns
