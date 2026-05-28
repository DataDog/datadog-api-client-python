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
    from datadog_api_client.v2.model.graph_item_data_attributes_counts_items import GraphItemDataAttributesCountsItems


class GraphItemDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.graph_item_data_attributes_counts_items import (
            GraphItemDataAttributesCountsItems,
        )

        return {
            "counts": ([GraphItemDataAttributesCountsItems],),
            "type": (str,),
        }

    attribute_map = {
        "counts": "counts",
        "type": "type",
    }

    def __init__(
        self_,
        counts: Union[List[GraphItemDataAttributesCountsItems], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a single grouping in the End User Device Monitoring graph response.

        :param counts: List of per-value counts for the grouping column.
        :type counts: [GraphItemDataAttributesCountsItems], optional

        :param type: Identifier of the grouping column (for example, ``os`` or ``type`` ).
        :type type: str, optional
        """
        if counts is not unset:
            kwargs["counts"] = counts
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
