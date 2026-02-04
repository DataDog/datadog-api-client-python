# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.notebook_search_aggregations import NotebookSearchAggregations


class NotebookSearchResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notebook_search_aggregations import NotebookSearchAggregations

        return {
            "aggregations": (NotebookSearchAggregations,),
            "total": (int,),
        }

    attribute_map = {
        "aggregations": "aggregations",
        "total": "total",
    }

    def __init__(self_, total: int, aggregations: Union[NotebookSearchAggregations, UnsetType] = unset, **kwargs):
        """
        Metadata about the notebook search results.

        :param aggregations: Aggregations of notebook search results.
        :type aggregations: NotebookSearchAggregations, optional

        :param total: Total number of notebooks found.
        :type total: int
        """
        if aggregations is not unset:
            kwargs["aggregations"] = aggregations
        super().__init__(kwargs)

        self_.total = total
