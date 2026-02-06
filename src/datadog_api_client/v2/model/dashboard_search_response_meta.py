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
    from datadog_api_client.v2.model.dashboard_search_aggregations import DashboardSearchAggregations


class DashboardSearchResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_search_aggregations import DashboardSearchAggregations

        return {
            "aggregations": (DashboardSearchAggregations,),
            "total": (int,),
        }

    attribute_map = {
        "aggregations": "aggregations",
        "total": "total",
    }

    def __init__(self_, total: int, aggregations: Union[DashboardSearchAggregations, UnsetType] = unset, **kwargs):
        """
        Metadata about the dashboard search results.

        :param aggregations: Aggregations of dashboard search results.
        :type aggregations: DashboardSearchAggregations, optional

        :param total: Total number of dashboards found.
        :type total: int
        """
        if aggregations is not unset:
            kwargs["aggregations"] = aggregations
        super().__init__(kwargs)

        self_.total = total
