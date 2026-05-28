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
    from datadog_api_client.v2.model.graph_item_data import GraphItemData


class GraphItemArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.graph_item_data import GraphItemData

        return {
            "data": ([GraphItemData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[GraphItemData], **kwargs):
        """
        Response body for the graph endpoint, returning per-grouping device counts.

        :param data: List of grouping entries with their associated device counts.
        :type data: [GraphItemData]
        """
        super().__init__(kwargs)

        self_.data = data
