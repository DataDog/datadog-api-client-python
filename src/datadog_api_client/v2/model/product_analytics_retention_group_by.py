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
    from datadog_api_client.v2.model.product_analytics_retention_group_by_target import (
        ProductAnalyticsRetentionGroupByTarget,
    )


class ProductAnalyticsRetentionGroupBy(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_group_by_sort import ProductAnalyticsGroupBySort
        from datadog_api_client.v2.model.product_analytics_retention_group_by_target import (
            ProductAnalyticsRetentionGroupByTarget,
        )

        return {
            "facet": (str,),
            "limit": (int,),
            "should_exclude_missing": (bool,),
            "sort": (ProductAnalyticsGroupBySort,),
            "source": (str,),
            "target": (ProductAnalyticsRetentionGroupByTarget,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
        "source": "source",
        "target": "target",
    }

    def __init__(
        self_,
        facet: str,
        target: ProductAnalyticsRetentionGroupByTarget,
        limit: Union[int, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[ProductAnalyticsGroupBySort, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Splits retention results by the values of a facet.

        :param facet: The attribute path to group by.
        :type facet: str

        :param limit: Maximum number of groups to return. Omit it to let the service choose.
        :type limit: int, optional

        :param should_exclude_missing: Whether to drop entities that have no value for the facet.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for group-by results.
        :type sort: ProductAnalyticsGroupBySort, optional

        :param source: Audience source backing the group-by, when grouping by an audience rather than a facet.
        :type source: str, optional

        :param target: Which axis of the retention grid a group-by applies to.
        :type target: ProductAnalyticsRetentionGroupByTarget
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
        self_.target = target
