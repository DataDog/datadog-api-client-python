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
    from datadog_api_client.v2.model.product_analytics_retention_list_column import ProductAnalyticsRetentionListColumn
    from datadog_api_client.v2.model.product_analytics_retention_cell_scope import ProductAnalyticsRetentionCellScope
    from datadog_api_client.v2.model.product_analytics_retention_search import ProductAnalyticsRetentionSearch


class ProductAnalyticsRetentionListQuery(ModelNormal):
    validations = {
        "limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_column import (
            ProductAnalyticsRetentionListColumn,
        )
        from datadog_api_client.v2.model.product_analytics_retention_cell_scope import (
            ProductAnalyticsRetentionCellScope,
        )
        from datadog_api_client.v2.model.product_analytics_retention_search import ProductAnalyticsRetentionSearch

        return {
            "columns": ([ProductAnalyticsRetentionListColumn],),
            "computation_scope": (ProductAnalyticsRetentionCellScope,),
            "limit": (int,),
            "search": (ProductAnalyticsRetentionSearch,),
        }

    attribute_map = {
        "columns": "columns",
        "computation_scope": "computation_scope",
        "limit": "limit",
        "search": "search",
    }

    def __init__(
        self_,
        computation_scope: ProductAnalyticsRetentionCellScope,
        search: ProductAnalyticsRetentionSearch,
        columns: Union[List[ProductAnalyticsRetentionListColumn], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for a retention list request.

        :param columns: The attribute columns to include in each returned row.
        :type columns: [ProductAnalyticsRetentionListColumn], optional

        :param computation_scope: Narrows a retention query to a single cell, at the intersection of one cohort and one return period.
        :type computation_scope: ProductAnalyticsRetentionCellScope

        :param limit: Maximum number of rows to return. Use ``0`` for no limit.
        :type limit: int, optional

        :param search: Defines the cohort and return criteria that make up a retention query.
        :type search: ProductAnalyticsRetentionSearch
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)

        self_.computation_scope = computation_scope
        self_.search = search
