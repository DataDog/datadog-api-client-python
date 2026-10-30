# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TopologyMapInlineNodeColumn(ModelComposed):
    def __init__(self, **kwargs):
        """
        Column of the nodes table.

        :param id: ID of the node ID column.
        :type id: TopologyMapInlineNodeIdColumnId

        :param kind: Column of strings.
        :type kind: TopologyMapInlineColumnKindString

        :param values: Node IDs.
        :type values: [str]

        :param meta: Display options for a value column.
        :type meta: TopologyMapInlineNodeValueColumnMeta, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.topology_map_inline_node_id_column import TopologyMapInlineNodeIdColumn
        from datadog_api_client.v1.model.topology_map_inline_node_string_column import TopologyMapInlineNodeStringColumn
        from datadog_api_client.v1.model.topology_map_inline_node_value_column import TopologyMapInlineNodeValueColumn

        return {
            "oneOf": [
                TopologyMapInlineNodeIdColumn,
                TopologyMapInlineNodeStringColumn,
                TopologyMapInlineNodeValueColumn,
            ],
        }
