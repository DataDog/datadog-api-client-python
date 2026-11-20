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
    from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
    from datadog_api_client.v1_20270101.model.graph_query_search_filter import GraphQuerySearchFilter


class LegacyUserJourneySearchFilters(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.audience_filters import AudienceFilters
        from datadog_api_client.v1_20270101.model.graph_query_search_filter import GraphQuerySearchFilter

        return {
            "audience_filters": (AudienceFilters,),
            "graph_filters": ([GraphQuerySearchFilter],),
            "string_filter": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "graph_filters": "graph_filters",
        "string_filter": "string_filter",
    }

    def __init__(
        self_,
        audience_filters: Union[AudienceFilters, UnsetType] = unset,
        graph_filters: Union[List[GraphQuerySearchFilter], UnsetType] = unset,
        string_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param audience_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type audience_filters: AudienceFilters, optional

        :param graph_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type graph_filters: [GraphQuerySearchFilter], optional

        :param string_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type string_filter: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if graph_filters is not unset:
            kwargs["graph_filters"] = graph_filters
        if string_filter is not unset:
            kwargs["string_filter"] = string_filter
        super().__init__(kwargs)
