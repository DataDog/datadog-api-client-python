# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class HeatmapBackendRequest20270101OneOf4458140576(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "number_format": (WidgetNumberFormat,),
            "query": (HeatmapBackendRequestAnyOfAnyOfItemQuery,),
            "request_type": (HeatmapBackendRequestAnyOfAnyOfItemRequestType,),
            "style": (RequestStyle,),
        }

    attribute_map = {
        "number_format": "number_format",
        "query": "query",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        query: HeatmapBackendRequestAnyOfAnyOfItemQuery,
        request_type: HeatmapBackendRequestAnyOfAnyOfItemRequestType,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        style: Union[RequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: HeatmapBackendRequestAnyOfAnyOfItemQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: HeatmapBackendRequestAnyOfAnyOfItemRequestType

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional
        """
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
