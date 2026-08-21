# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_sankey_aggregated_node import (
        ProductAnalyticsSankeyAggregatedNode,
    )
    from datadog_api_client.v2.model.product_analytics_sankey_node_type import ProductAnalyticsSankeyNodeType


class ProductAnalyticsSankeyNode(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_aggregated_node import (
            ProductAnalyticsSankeyAggregatedNode,
        )
        from datadog_api_client.v2.model.product_analytics_sankey_node_type import ProductAnalyticsSankeyNodeType

        return {
            "aggregated_nodes": ([ProductAnalyticsSankeyAggregatedNode],),
            "column": (int,),
            "dropoff_value": (int,),
            "id": (str,),
            "incoming_value": (int,),
            "name": (str,),
            "outgoing_value": (int,),
            "type": (ProductAnalyticsSankeyNodeType,),
            "value": (int,),
        }

    attribute_map = {
        "aggregated_nodes": "aggregated_nodes",
        "column": "column",
        "dropoff_value": "dropoff_value",
        "id": "id",
        "incoming_value": "incoming_value",
        "name": "name",
        "outgoing_value": "outgoing_value",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        aggregated_nodes: Union[List[ProductAnalyticsSankeyAggregatedNode], UnsetType] = unset,
        column: Union[int, UnsetType] = unset,
        dropoff_value: Union[int, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        incoming_value: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        outgoing_value: Union[int, UnsetType] = unset,
        type: Union[ProductAnalyticsSankeyNodeType, UnsetType] = unset,
        value: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A node of the Sankey diagram, representing one facet value in one column.

        :param aggregated_nodes: The nodes rolled up into this one, when the node is an aggregate.
        :type aggregated_nodes: [ProductAnalyticsSankeyAggregatedNode], optional

        :param column: Zero-based index of the column the node sits in.
        :type column: int, optional

        :param dropoff_value: Number of sessions that ended at the node.
        :type dropoff_value: int, optional

        :param id: Unique identifier for the node.
        :type id: str, optional

        :param incoming_value: Number of sessions entering the node.
        :type incoming_value: int, optional

        :param name: The facet value the node represents.
        :type name: str, optional

        :param outgoing_value: Number of sessions leaving the node.
        :type outgoing_value: int, optional

        :param type: The kind of node. ``regular`` is a single facet value, ``other`` rolls up the values that did not
            fit within ``entries_per_step`` , and ``dropoff`` collects the sessions that ended at this column.
        :type type: ProductAnalyticsSankeyNodeType, optional

        :param value: Number of sessions passing through the node.
        :type value: int, optional
        """
        if aggregated_nodes is not unset:
            kwargs["aggregated_nodes"] = aggregated_nodes
        if column is not unset:
            kwargs["column"] = column
        if dropoff_value is not unset:
            kwargs["dropoff_value"] = dropoff_value
        if id is not unset:
            kwargs["id"] = id
        if incoming_value is not unset:
            kwargs["incoming_value"] = incoming_value
        if name is not unset:
            kwargs["name"] = name
        if outgoing_value is not unset:
            kwargs["outgoing_value"] = outgoing_value
        if type is not unset:
            kwargs["type"] = type
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
