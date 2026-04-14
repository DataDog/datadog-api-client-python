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
    from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
    from datadog_api_client.v1.model.product_analytics_extended_compute import ProductAnalyticsExtendedCompute
    from datadog_api_client.v1.model.formula_and_function_product_analytics_extended_data_source import (
        FormulaAndFunctionProductAnalyticsExtendedDataSource,
    )
    from datadog_api_client.v1.model.product_analytics_extended_group_by import ProductAnalyticsExtendedGroupBy
    from datadog_api_client.v1.model.formula_and_function_product_analytics_extended_query_definition_indexes_items import (
        FormulaAndFunctionProductAnalyticsExtendedQueryDefinitionIndexesItems,
    )
    from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery


class FormulaAndFunctionProductAnalyticsExtendedQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v1.model.product_analytics_extended_compute import ProductAnalyticsExtendedCompute
        from datadog_api_client.v1.model.formula_and_function_product_analytics_extended_data_source import (
            FormulaAndFunctionProductAnalyticsExtendedDataSource,
        )
        from datadog_api_client.v1.model.product_analytics_extended_group_by import ProductAnalyticsExtendedGroupBy
        from datadog_api_client.v1.model.formula_and_function_product_analytics_extended_query_definition_indexes_items import (
            FormulaAndFunctionProductAnalyticsExtendedQueryDefinitionIndexesItems,
        )
        from datadog_api_client.v1.model.product_analytics_base_query import ProductAnalyticsBaseQuery

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "compute": (ProductAnalyticsExtendedCompute,),
            "data_source": (FormulaAndFunctionProductAnalyticsExtendedDataSource,),
            "group_by": ([ProductAnalyticsExtendedGroupBy],),
            "indexes": ([FormulaAndFunctionProductAnalyticsExtendedQueryDefinitionIndexesItems],),
            "name": (str,),
            "query": (ProductAnalyticsBaseQuery,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        compute: ProductAnalyticsExtendedCompute,
        data_source: FormulaAndFunctionProductAnalyticsExtendedDataSource,
        name: str,
        query: ProductAnalyticsBaseQuery,
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsExtendedGroupBy], UnsetType] = unset,
        indexes: Union[List[FormulaAndFunctionProductAnalyticsExtendedQueryDefinitionIndexesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions Product Analytics Extended query for advanced analytics features.

        :param audience_filters: Product Analytics/RUM audience filters.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param compute: Compute configuration for Product Analytics Extended queries.
        :type compute: ProductAnalyticsExtendedCompute

        :param data_source: Data source for Product Analytics Extended queries.
        :type data_source: FormulaAndFunctionProductAnalyticsExtendedDataSource

        :param group_by: Group by configuration.
        :type group_by: [ProductAnalyticsExtendedGroupBy], optional

        :param indexes: Event indexes to query.
        :type indexes: [FormulaAndFunctionProductAnalyticsExtendedQueryDefinitionIndexesItems], optional

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: Product Analytics event query.
        :type query: ProductAnalyticsBaseQuery
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.query = query
