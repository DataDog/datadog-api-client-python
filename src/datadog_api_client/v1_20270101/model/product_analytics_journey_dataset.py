# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
    from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
    from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_data_source import (
        ProductAnalyticsJourneyDatasetDataSource,
    )
    from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_entity import (
        ProductAnalyticsJourneyDatasetEntity,
    )
    from datadog_api_client.v1_20270101.model.product_analytics_event_query import ProductAnalyticsEventQuery
    from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_search import (
        ProductAnalyticsJourneyDatasetSearch,
    )
    from datadog_api_client.v1_20270101.model.time_window import TimeWindow


class ProductAnalyticsJourneyDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
        from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
        from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_data_source import (
            ProductAnalyticsJourneyDatasetDataSource,
        )
        from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_entity import (
            ProductAnalyticsJourneyDatasetEntity,
        )
        from datadog_api_client.v1_20270101.model.product_analytics_event_query import ProductAnalyticsEventQuery
        from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset_search import (
            ProductAnalyticsJourneyDatasetSearch,
        )
        from datadog_api_client.v1_20270101.model.time_window import TimeWindow

        return {
            "audience_filters": (AudienceFilters,),
            "columns": ([DatasetColumn],),
            "conversion_time_ms": (float, none_type),
            "data_source": (ProductAnalyticsJourneyDatasetDataSource,),
            "entity": (ProductAnalyticsJourneyDatasetEntity,),
            "expression": (str,),
            "name": (str,),
            "node_objects": ({str: (ProductAnalyticsEventQuery,)},),
            "search": (ProductAnalyticsJourneyDatasetSearch,),
            "time_window": (TimeWindow,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "columns": "columns",
        "conversion_time_ms": "conversion_time_ms",
        "data_source": "data_source",
        "entity": "entity",
        "expression": "expression",
        "name": "name",
        "node_objects": "node_objects",
        "search": "search",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        columns: List[DatasetColumn],
        data_source: ProductAnalyticsJourneyDatasetDataSource,
        entity: ProductAnalyticsJourneyDatasetEntity,
        expression: str,
        name: str,
        node_objects: Dict[str, ProductAnalyticsEventQuery],
        audience_filters: Union[AudienceFilters, UnsetType] = unset,
        conversion_time_ms: Union[float, none_type, UnsetType] = unset,
        search: Union[ProductAnalyticsJourneyDatasetSearch, UnsetType] = unset,
        time_window: Union[TimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param audience_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type audience_filters: AudienceFilters, optional

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetColumn]

        :param conversion_time_ms: Test-only generated schema for the dashboard versioning proof of concept.
        :type conversion_time_ms: float, none_type, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ProductAnalyticsJourneyDatasetDataSource

        :param entity: Test-only generated schema for the dashboard versioning proof of concept.
        :type entity: ProductAnalyticsJourneyDatasetEntity

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param node_objects: Test-only generated schema for the dashboard versioning proof of concept.
        :type node_objects: {str: (ProductAnalyticsEventQuery,)}

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: ProductAnalyticsJourneyDatasetSearch, optional

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if conversion_time_ms is not unset:
            kwargs["conversion_time_ms"] = conversion_time_ms
        if search is not unset:
            kwargs["search"] = search
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.columns = columns
        self_.data_source = data_source
        self_.entity = entity
        self_.expression = expression
        self_.name = name
        self_.node_objects = node_objects
