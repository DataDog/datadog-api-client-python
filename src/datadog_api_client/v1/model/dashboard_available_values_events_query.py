# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dashboard_available_values_events_data_source import (
        DashboardAvailableValuesEventsDataSource,
    )
    from datadog_api_client.v1.model.dashboard_available_values_events_query_group_by_items import (
        DashboardAvailableValuesEventsQueryGroupByItems,
    )
    from datadog_api_client.v1.model.dashboard_available_values_events_query_search import (
        DashboardAvailableValuesEventsQuerySearch,
    )


class DashboardAvailableValuesEventsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_available_values_events_data_source import (
            DashboardAvailableValuesEventsDataSource,
        )
        from datadog_api_client.v1.model.dashboard_available_values_events_query_group_by_items import (
            DashboardAvailableValuesEventsQueryGroupByItems,
        )
        from datadog_api_client.v1.model.dashboard_available_values_events_query_search import (
            DashboardAvailableValuesEventsQuerySearch,
        )

        return {
            "data_source": (DashboardAvailableValuesEventsDataSource,),
            "group_by": ([DashboardAvailableValuesEventsQueryGroupByItems],),
            "search": (DashboardAvailableValuesEventsQuerySearch,),
        }

    attribute_map = {
        "data_source": "data_source",
        "group_by": "group_by",
        "search": "search",
    }

    def __init__(
        self_,
        data_source: DashboardAvailableValuesEventsDataSource,
        group_by: List[DashboardAvailableValuesEventsQueryGroupByItems],
        search: DashboardAvailableValuesEventsQuerySearch,
        **kwargs,
    ):
        """
        Query for available values using an events-based data source (spans, logs, or rum).

        :param data_source: The events-based data source for the query.
        :type data_source: DashboardAvailableValuesEventsDataSource

        :param group_by: The fields to group by in the query.
        :type group_by: [DashboardAvailableValuesEventsQueryGroupByItems]

        :param search: The search filter for the query.
        :type search: DashboardAvailableValuesEventsQuerySearch
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.group_by = group_by
        self_.search = search
