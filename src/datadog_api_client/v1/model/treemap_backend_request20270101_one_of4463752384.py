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
    from datadog_api_client.v1.model.treemap_backend_request20270101_one_of_query import (
        TreemapBackendRequest20270101OneOfQuery,
    )


class TreemapBackendRequest20270101OneOf4463752384(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.treemap_backend_request20270101_one_of_query import (
            TreemapBackendRequest20270101OneOfQuery,
        )

        return {
            "projection": (TabularProjection,),
            "query": (TreemapBackendRequest20270101OneOfQuery,),
            "request_type": (TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208,),
            "response_format": (TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453530528,),
            "style": (TreemapRequestStyle,),
        }

    attribute_map = {
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
    }

    def __init__(
        self_,
        query: Union[TreemapBackendRequest20270101OneOfQuery, StructuredAnalysisQuery, SampledAnalysisQuery],
        request_type: TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208,
        response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453530528,
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
        style: Union[TreemapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: TreemapBackendRequest20270101OneOfQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453530528

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TreemapRequestStyle, optional
        """
        if projection is not unset:
            kwargs["projection"] = projection
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
        self_.response_format = response_format
