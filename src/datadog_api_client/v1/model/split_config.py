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
    from datadog_api_client.v1.model.split_sort import SplitSort
    from datadog_api_client.v1.model.split_dimension import SplitDimension
    from datadog_api_client.v1.model.split_vector_entry_item import SplitVectorEntryItem


class SplitConfig(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 500,
            "inclusive_minimum": 1,
        },
        "split_dimensions": {
            "max_items": 1,
            "min_items": 1,
        },
        "static_splits": {
            "max_items": 500,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.split_sort import SplitSort
        from datadog_api_client.v1.model.split_dimension import SplitDimension
        from datadog_api_client.v1.model.split_vector_entry_item import SplitVectorEntryItem

        return {
            "limit": (int,),
            "sort": (SplitSort,),
            "split_dimensions": ([SplitDimension],),
            "static_splits": ([[SplitVectorEntryItem]],),
        }

    attribute_map = {
        "limit": "limit",
        "sort": "sort",
        "split_dimensions": "split_dimensions",
        "static_splits": "static_splits",
    }

    def __init__(
        self_,
        limit: int,
        sort: SplitSort,
        split_dimensions: List[SplitDimension],
        static_splits: Union[List[List[SplitVectorEntryItem]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Encapsulates all user choices about how to split a graph.

        :param limit: Maximum number of graphs to display in the widget.
        :type limit: int

        :param sort: Controls the order in which graphs appear in the split.
        :type sort: SplitSort

        :param split_dimensions: The dimension(s) on which to split the graph
        :type split_dimensions: [SplitDimension]

        :param static_splits: Manual selection of tags making split graph widget static
        :type static_splits: [[SplitVectorEntryItem]], optional
        """
        if static_splits is not unset:
            kwargs["static_splits"] = static_splits
        super().__init__(kwargs)

        self_.limit = limit
        self_.sort = sort
        self_.split_dimensions = split_dimensions
