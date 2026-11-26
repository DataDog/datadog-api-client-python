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
    from datadog_api_client.v1.model.bar_chart_backend_request20270101_one_of_query import (
        BarChartBackendRequest20270101OneOfQuery,
    )


class BarChartBackendRequest20270101OneOf4454436672(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.bar_chart_backend_request20270101_one_of_query import (
            BarChartBackendRequest20270101OneOfQuery,
        )

        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "projection": (TabularProjection,),
            "query": (BarChartBackendRequest20270101OneOfQuery,),
            "request_type": (BarChartBackendRequestAnyOfAnyOfItemRequestType4443924544,),
            "response_format": (BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443924864,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        query: Union[BarChartBackendRequest20270101OneOfQuery, StructuredAnalysisQuery, SampledAnalysisQuery],
        request_type: BarChartBackendRequestAnyOfAnyOfItemRequestType4443924544,
        response_format: BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443924864,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        projection: Union[
            TabularProjection,
            ScatterplotProjection,
            TreeDataProjectionBarChart,
            TreeDataProjectionSunburst,
            TreeDataProjectionToplist,
            TreeDataProjectionTreemap,
            QueryValueProjection,
            QueryTableProjection,
            RunChartProjection,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: BarChartBackendRequest20270101OneOfQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: BarChartBackendRequestAnyOfAnyOfItemRequestType4443924544

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443924864
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if projection is not unset:
            kwargs["projection"] = projection
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
        self_.response_format = response_format
