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


class GeomapBackendPointsRequest20270101OneOf4457228992(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "query": (GeomapBackendPointsRequestAnyOfAnyOfItemQuery,),
            "request_type": (GeomapBackendPointsRequestAnyOfAnyOfItemRequestType,),
            "response_format": (GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat4447001376,),
            "style": (GeomapRequestStyle,),
            "text_formats": ([TextFormattingRule],),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        query: GeomapBackendPointsRequestAnyOfAnyOfItemQuery,
        request_type: GeomapBackendPointsRequestAnyOfAnyOfItemRequestType,
        response_format: GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat4447001376,
        style: Union[GeomapRequestStyle, UnsetType] = unset,
        text_formats: Union[List[TextFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: GeomapBackendPointsRequestAnyOfAnyOfItemQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: GeomapBackendPointsRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat4447001376

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule], optional
        """
        if style is not unset:
            kwargs["style"] = style
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
        self_.response_format = response_format
