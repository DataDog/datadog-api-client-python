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
    from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
    from datadog_api_client.v1.model.sankey_rum_data_source import SankeyRumDataSource
    from datadog_api_client.v1.model.sankey_join_keys import SankeyJoinKeys
    from datadog_api_client.v1.model.sankey_rum_query_mode import SankeyRumQueryMode
    from datadog_api_client.v1.model.product_analytics_audience_occurrence_filter import (
        ProductAnalyticsAudienceOccurrenceFilter,
    )


class SankeyRumQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_audience_filters import ProductAnalyticsAudienceFilters
        from datadog_api_client.v1.model.sankey_rum_data_source import SankeyRumDataSource
        from datadog_api_client.v1.model.sankey_join_keys import SankeyJoinKeys
        from datadog_api_client.v1.model.sankey_rum_query_mode import SankeyRumQueryMode
        from datadog_api_client.v1.model.product_analytics_audience_occurrence_filter import (
            ProductAnalyticsAudienceOccurrenceFilter,
        )

        return {
            "audience_filters": (ProductAnalyticsAudienceFilters,),
            "data_source": (SankeyRumDataSource,),
            "entries_per_step": (int,),
            "join_keys": (SankeyJoinKeys,),
            "mode": (SankeyRumQueryMode,),
            "number_of_steps": (int,),
            "occurrences": (ProductAnalyticsAudienceOccurrenceFilter,),
            "query_string": (str,),
            "source": (str,),
            "subquery_id": (str,),
            "target": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "data_source": "data_source",
        "entries_per_step": "entries_per_step",
        "join_keys": "join_keys",
        "mode": "mode",
        "number_of_steps": "number_of_steps",
        "occurrences": "occurrences",
        "query_string": "query_string",
        "source": "source",
        "subquery_id": "subquery_id",
        "target": "target",
    }

    def __init__(
        self_,
        data_source: SankeyRumDataSource,
        mode: SankeyRumQueryMode,
        query_string: str,
        audience_filters: Union[ProductAnalyticsAudienceFilters, UnsetType] = unset,
        entries_per_step: Union[int, UnsetType] = unset,
        join_keys: Union[SankeyJoinKeys, UnsetType] = unset,
        number_of_steps: Union[int, UnsetType] = unset,
        occurrences: Union[ProductAnalyticsAudienceOccurrenceFilter, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        subquery_id: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sankey widget with RUM data source query.

        :param audience_filters: Product Analytics/RUM audience filters.
        :type audience_filters: ProductAnalyticsAudienceFilters, optional

        :param data_source: Sankey widget with RUM data source.
        :type data_source: SankeyRumDataSource

        :param entries_per_step: Entries per step.
        :type entries_per_step: int, optional

        :param join_keys: Join keys.
        :type join_keys: SankeyJoinKeys, optional

        :param mode: Sankey mode for RUM queries.
        :type mode: SankeyRumQueryMode

        :param number_of_steps: Number of steps.
        :type number_of_steps: int, optional

        :param occurrences:
        :type occurrences: ProductAnalyticsAudienceOccurrenceFilter, optional

        :param query_string: Query string.
        :type query_string: str

        :param source: Source.
        :type source: str, optional

        :param subquery_id: Subquery ID.
        :type subquery_id: str, optional

        :param target: Target.
        :type target: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if entries_per_step is not unset:
            kwargs["entries_per_step"] = entries_per_step
        if join_keys is not unset:
            kwargs["join_keys"] = join_keys
        if number_of_steps is not unset:
            kwargs["number_of_steps"] = number_of_steps
        if occurrences is not unset:
            kwargs["occurrences"] = occurrences
        if source is not unset:
            kwargs["source"] = source
        if subquery_id is not unset:
            kwargs["subquery_id"] = subquery_id
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.mode = mode
        self_.query_string = query_string
