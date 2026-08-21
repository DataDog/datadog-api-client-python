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
    from datadog_api_client.v2.model.product_analytics_retention_scope import ProductAnalyticsRetentionScope
    from datadog_api_client.v2.model.product_analytics_retention_compute import ProductAnalyticsRetentionCompute
    from datadog_api_client.v2.model.product_analytics_retention_group_by import ProductAnalyticsRetentionGroupBy
    from datadog_api_client.v2.model.product_analytics_retention_search import ProductAnalyticsRetentionSearch
    from datadog_api_client.v2.model.product_analytics_retention_cohort_scope import (
        ProductAnalyticsRetentionCohortScope,
    )
    from datadog_api_client.v2.model.product_analytics_retention_return_period_scope import (
        ProductAnalyticsRetentionReturnPeriodScope,
    )
    from datadog_api_client.v2.model.product_analytics_retention_cell_scope import ProductAnalyticsRetentionCellScope


class ProductAnalyticsRetentionGridQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_scope import ProductAnalyticsRetentionScope
        from datadog_api_client.v2.model.product_analytics_retention_compute import ProductAnalyticsRetentionCompute
        from datadog_api_client.v2.model.product_analytics_retention_group_by import ProductAnalyticsRetentionGroupBy
        from datadog_api_client.v2.model.product_analytics_retention_search import ProductAnalyticsRetentionSearch

        return {
            "computation_scope": (ProductAnalyticsRetentionScope,),
            "compute": (ProductAnalyticsRetentionCompute,),
            "group_by": ([ProductAnalyticsRetentionGroupBy],),
            "search": (ProductAnalyticsRetentionSearch,),
        }

    attribute_map = {
        "computation_scope": "computation_scope",
        "compute": "compute",
        "group_by": "group_by",
        "search": "search",
    }

    def __init__(
        self_,
        compute: ProductAnalyticsRetentionCompute,
        search: ProductAnalyticsRetentionSearch,
        computation_scope: Union[
            ProductAnalyticsRetentionScope,
            ProductAnalyticsRetentionCohortScope,
            ProductAnalyticsRetentionReturnPeriodScope,
            ProductAnalyticsRetentionCellScope,
            UnsetType,
        ] = unset,
        group_by: Union[List[ProductAnalyticsRetentionGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for a retention grid or retention metadata request.

        :param computation_scope: Restricts a retention query to part of the grid, so that results can be examined in detail.
            Omit it to compute the whole grid.
        :type computation_scope: ProductAnalyticsRetentionScope, optional

        :param compute: The metric and aggregation applied to a retention query.
        :type compute: ProductAnalyticsRetentionCompute

        :param group_by: Splits the results by the values of one or more facets.
        :type group_by: [ProductAnalyticsRetentionGroupBy], optional

        :param search: Defines the cohort and return criteria that make up a retention query.
        :type search: ProductAnalyticsRetentionSearch
        """
        if computation_scope is not unset:
            kwargs["computation_scope"] = computation_scope
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.compute = compute
        self_.search = search
