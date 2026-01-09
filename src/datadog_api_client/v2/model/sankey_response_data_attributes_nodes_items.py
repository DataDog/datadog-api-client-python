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
    from datadog_api_client.v2.model.sankey_response_data_attributes_nodes_items_aggregated_nodes_items import (
        SankeyResponseDataAttributesNodesItemsAggregatedNodesItems,
    )


class SankeyResponseDataAttributesNodesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sankey_response_data_attributes_nodes_items_aggregated_nodes_items import (
            SankeyResponseDataAttributesNodesItemsAggregatedNodesItems,
        )

        return {
            "aggregated_nodes": ([SankeyResponseDataAttributesNodesItemsAggregatedNodesItems],),
            "column": (int,),
            "id": (str,),
            "incoming_value": (int,),
            "name": (str,),
            "outgoing_value": (int,),
            "type": (str,),
            "value": (int,),
        }

    attribute_map = {
        "aggregated_nodes": "aggregated_nodes",
        "column": "column",
        "id": "id",
        "incoming_value": "incoming_value",
        "name": "name",
        "outgoing_value": "outgoing_value",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        aggregated_nodes: Union[List[SankeyResponseDataAttributesNodesItemsAggregatedNodesItems], UnsetType] = unset,
        column: Union[int, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        incoming_value: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        outgoing_value: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        value: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param aggregated_nodes:
        :type aggregated_nodes: [SankeyResponseDataAttributesNodesItemsAggregatedNodesItems], optional

        :param column:
        :type column: int, optional

        :param id:
        :type id: str, optional

        :param incoming_value:
        :type incoming_value: int, optional

        :param name:
        :type name: str, optional

        :param outgoing_value:
        :type outgoing_value: int, optional

        :param type:
        :type type: str, optional

        :param value:
        :type value: int, optional
        """
        if aggregated_nodes is not unset:
            kwargs["aggregated_nodes"] = aggregated_nodes
        if column is not unset:
            kwargs["column"] = column
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
