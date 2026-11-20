# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
    from datadog_api_client.v1_20270101.model.product_analytics_compute import ProductAnalyticsCompute
    from datadog_api_client.v1_20270101.model.formula_product_analytics_extended_query_data_source import (
        FormulaProductAnalyticsExtendedQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.product_analytics_group_by import ProductAnalyticsGroupBy
    from datadog_api_client.v1.model.formula_product_analytics_extended_query20270101_indexes import (
        FormulaProductAnalyticsExtendedQuery20270101Indexes,
    )
    from datadog_api_client.v1_20270101.model.base_product_analytics_query import BaseProductAnalyticsQuery
    from datadog_api_client.v1_20270101.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v1_20270101.model.product_analytics_event_occurrence_query import (
        ProductAnalyticsEventOccurrenceQuery,
    )


class FormulaProductAnalyticsExtendedQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
        from datadog_api_client.v1_20270101.model.product_analytics_compute import ProductAnalyticsCompute
        from datadog_api_client.v1_20270101.model.formula_product_analytics_extended_query_data_source import (
            FormulaProductAnalyticsExtendedQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.product_analytics_group_by import ProductAnalyticsGroupBy
        from datadog_api_client.v1.model.formula_product_analytics_extended_query20270101_indexes import (
            FormulaProductAnalyticsExtendedQuery20270101Indexes,
        )
        from datadog_api_client.v1_20270101.model.base_product_analytics_query import BaseProductAnalyticsQuery

        return {
            "audience_filters": (AudienceFilters,),
            "compute": (ProductAnalyticsCompute,),
            "data_source": (FormulaProductAnalyticsExtendedQueryDataSource,),
            "group_by": ([ProductAnalyticsGroupBy],),
            "indexes": (FormulaProductAnalyticsExtendedQuery20270101Indexes,),
            "name": (str,),
            "query": (BaseProductAnalyticsQuery,),
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
        compute: ProductAnalyticsCompute,
        data_source: FormulaProductAnalyticsExtendedQueryDataSource,
        name: str,
        query: Union[BaseProductAnalyticsQuery, ProductAnalyticsEventQuery, ProductAnalyticsEventOccurrenceQuery],
        audience_filters: Union[AudienceFilters, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsGroupBy], UnsetType] = unset,
        indexes: Union[FormulaProductAnalyticsExtendedQuery20270101Indexes, List[Any], List[Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param audience_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type audience_filters: AudienceFilters, optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: ProductAnalyticsCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaProductAnalyticsExtendedQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [ProductAnalyticsGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: FormulaProductAnalyticsExtendedQuery20270101Indexes, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: BaseProductAnalyticsQuery
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
