# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GeomapBackendPointsRequest20270101OneOf4457230272(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "limit": (float,),
            "projection": (GeomapPointsProjection,),
            "query": (DataProjectionQuery,),
            "request_type": (GeomapBackendPointsRequestAnyOfAnyOfItemRequestType4447003616,),
            "style": (GeomapBackendPointsRequestAnyOfAnyOfItemStyle,),
            "text_formats": ([TextFormattingRule],),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "limit": "limit",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "style": "style",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        projection: GeomapPointsProjection,
        query: Union[
            DataProjectionQuery, AggregateAugmentedQuery, EventsPlatformDataProjectionQueryDefinition, DatasetListQuery
        ],
        request_type: GeomapBackendPointsRequestAnyOfAnyOfItemRequestType4447003616,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        style: Union[GeomapBackendPointsRequestAnyOfAnyOfItemStyle, UnsetType] = unset,
        text_formats: Union[List[TextFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: GeomapPointsProjection

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: DataProjectionQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: GeomapBackendPointsRequestAnyOfAnyOfItemRequestType4447003616

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapBackendPointsRequestAnyOfAnyOfItemStyle, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule], optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if limit is not unset:
            kwargs["limit"] = limit
        if style is not unset:
            kwargs["style"] = style
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.projection = projection
        self_.query = query
        self_.request_type = request_type
