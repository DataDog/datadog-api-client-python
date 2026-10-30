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
    from datadog_api_client.v1.model.journey_map_conversion_type import JourneyMapConversionType
    from datadog_api_client.v1.model.journey_map_counting_method import JourneyMapCountingMethod
    from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
    from datadog_api_client.v1.model.journey_map_expanded_prefix import JourneyMapExpandedPrefix
    from datadog_api_client.v1.model.journey_map_group_by import JourneyMapGroupBy
    from datadog_api_client.v1.model.user_journey_search import UserJourneySearch
    from datadog_api_client.v1.model.journey_map_target import JourneyMapTarget


class JourneyMapQuery(ModelNormal):
    validations = {
        "entries_per_step": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.journey_map_conversion_type import JourneyMapConversionType
        from datadog_api_client.v1.model.journey_map_counting_method import JourneyMapCountingMethod
        from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
        from datadog_api_client.v1.model.journey_map_expanded_prefix import JourneyMapExpandedPrefix
        from datadog_api_client.v1.model.journey_map_group_by import JourneyMapGroupBy
        from datadog_api_client.v1.model.user_journey_search import UserJourneySearch
        from datadog_api_client.v1.model.journey_map_target import JourneyMapTarget

        return {
            "conversion_type": (JourneyMapConversionType,),
            "counting_method": (JourneyMapCountingMethod,),
            "data_source": (ProductAnalyticsFunnelDataSource,),
            "entries_per_step": (int,),
            "event_filter": (str,),
            "expanded_prefixes": ([JourneyMapExpandedPrefix],),
            "group_by": ([JourneyMapGroupBy],),
            "search": (UserJourneySearch,),
            "target": (JourneyMapTarget,),
        }

    attribute_map = {
        "conversion_type": "conversion_type",
        "counting_method": "counting_method",
        "data_source": "data_source",
        "entries_per_step": "entries_per_step",
        "event_filter": "event_filter",
        "expanded_prefixes": "expanded_prefixes",
        "group_by": "group_by",
        "search": "search",
        "target": "target",
    }

    def __init__(
        self_,
        data_source: ProductAnalyticsFunnelDataSource,
        search: UserJourneySearch,
        target: JourneyMapTarget,
        conversion_type: Union[JourneyMapConversionType, UnsetType] = unset,
        counting_method: Union[JourneyMapCountingMethod, UnsetType] = unset,
        entries_per_step: Union[int, UnsetType] = unset,
        event_filter: Union[str, UnsetType] = unset,
        expanded_prefixes: Union[List[JourneyMapExpandedPrefix], UnsetType] = unset,
        group_by: Union[List[JourneyMapGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        Journey Paths query definition.

        :param conversion_type: Whether to show the paths that convert to the end step or drop off before it.
        :type conversion_type: JourneyMapConversionType, optional

        :param counting_method: Whether to count unique journeys or all journeys.
        :type counting_method: JourneyMapCountingMethod, optional

        :param data_source: Data source for user journey funnel queries.
        :type data_source: ProductAnalyticsFunnelDataSource

        :param entries_per_step: Maximum number of paths shown per step.
        :type entries_per_step: int, optional

        :param event_filter: Filter applied to the events shown along the paths.
        :type event_filter: str, optional

        :param expanded_prefixes: Paths expanded to show the events that follow them.
        :type expanded_prefixes: [JourneyMapExpandedPrefix], optional

        :param group_by: Group by configuration.
        :type group_by: [JourneyMapGroupBy], optional

        :param search: User journey search configuration.
        :type search: UserJourneySearch

        :param target: The pair of journey steps the paths are visualized between.
        :type target: JourneyMapTarget
        """
        if conversion_type is not unset:
            kwargs["conversion_type"] = conversion_type
        if counting_method is not unset:
            kwargs["counting_method"] = counting_method
        if entries_per_step is not unset:
            kwargs["entries_per_step"] = entries_per_step
        if event_filter is not unset:
            kwargs["event_filter"] = event_filter
        if expanded_prefixes is not unset:
            kwargs["expanded_prefixes"] = expanded_prefixes
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.search = search
        self_.target = target
