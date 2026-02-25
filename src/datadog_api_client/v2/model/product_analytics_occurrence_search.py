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
    from datadog_api_client.v2.model.product_analytics_occurrence_filter import ProductAnalyticsOccurrenceFilter


class ProductAnalyticsOccurrenceSearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_occurrence_filter import ProductAnalyticsOccurrenceFilter

        return {
            "occurrences": (ProductAnalyticsOccurrenceFilter,),
            "query": (str,),
        }

    attribute_map = {
        "occurrences": "occurrences",
        "query": "query",
    }

    def __init__(
        self_,
        occurrences: Union[ProductAnalyticsOccurrenceFilter, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Search parameters for an occurrence query.

        :param occurrences: Filter for occurrence-based queries.
        :type occurrences: ProductAnalyticsOccurrenceFilter, optional

        :param query: The search query using Datadog search syntax.
        :type query: str, optional
        """
        if occurrences is not unset:
            kwargs["occurrences"] = occurrences
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
