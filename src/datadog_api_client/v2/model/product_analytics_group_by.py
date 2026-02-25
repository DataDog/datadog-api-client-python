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
    from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort


class ProductAnalyticsGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort

        return {
            "facet": (str,),
            "limit": (int,),
            "should_exclude_missing": (bool,),
            "sort": (ProductAnalyticsGroupBySort,),
            "source": (str,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
        "source": "source",
    }

    def __init__(
        self_,
        facet: str,
        limit: Union[int, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[ProductAnalyticsGroupBySort, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A group-by rule for segmenting results by facet values.

        :param facet: The facet to group by.
        :type facet: str

        :param limit: Maximum number of groups to return.
        :type limit: int, optional

        :param should_exclude_missing: Exclude results with missing facet values.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for group-by results.
        :type sort: ProductAnalyticsGroupBySort, optional

        :param source: The source for audience-filter-based group-by.
        :type source: str, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

        self_.facet = facet
