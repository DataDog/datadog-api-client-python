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
    from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit


class ProductAnalyticsSerie(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit

        return {
            "group_tags": ([str],),
            "query_index": (int,),
            "unit": ([ProductAnalyticsUnit],),
        }

    attribute_map = {
        "group_tags": "group_tags",
        "query_index": "query_index",
        "unit": "unit",
    }

    def __init__(
        self_,
        group_tags: Union[List[str], UnsetType] = unset,
        query_index: Union[int, UnsetType] = unset,
        unit: Union[List[ProductAnalyticsUnit], UnsetType] = unset,
        **kwargs,
    ):
        """
        A series in a timeseries response.

        :param group_tags:
        :type group_tags: [str], optional

        :param query_index:
        :type query_index: int, optional

        :param unit:
        :type unit: [ProductAnalyticsUnit], optional
        """
        if group_tags is not unset:
            kwargs["group_tags"] = group_tags
        if query_index is not unset:
            kwargs["query_index"] = query_index
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)
