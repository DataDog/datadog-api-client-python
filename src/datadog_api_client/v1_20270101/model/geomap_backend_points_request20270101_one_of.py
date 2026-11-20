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
    from datadog_api_client.v1_20270101.model.geomap_backend_points_request_any_of_any_of_item_columns_items import (
        GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems,
    )
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.logs_stream_query import LogsStreamQuery
    from datadog_api_client.v1_20270101.model.geomap_backend_points_request_any_of_any_of_item_response_format import (
        GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat,
    )
    from datadog_api_client.v1_20270101.model.geomap_request_style import GeomapRequestStyle
    from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule


class GeomapBackendPointsRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request_any_of_any_of_item_columns_items import (
            GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.logs_stream_query import LogsStreamQuery
        from datadog_api_client.v1_20270101.model.geomap_backend_points_request_any_of_any_of_item_response_format import (
            GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat,
        )
        from datadog_api_client.v1_20270101.model.geomap_request_style import GeomapRequestStyle
        from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule

        return {
            "columns": ([GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems],),
            "conditional_formats": ([ThresholdFormattingRule],),
            "query": (LogsStreamQuery,),
            "response_format": (GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat,),
            "style": (GeomapRequestStyle,),
            "text_formats": ([TextFormattingRule],),
        }

    attribute_map = {
        "columns": "columns",
        "conditional_formats": "conditional_formats",
        "query": "query",
        "response_format": "response_format",
        "style": "style",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        columns: List[GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems],
        query: LogsStreamQuery,
        response_format: GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        style: Union[GeomapRequestStyle, UnsetType] = unset,
        text_formats: Union[List[TextFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [GeomapBackendPointsRequestAnyOfAnyOfItemColumnsItems]

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: LogsStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: GeomapBackendPointsRequestAnyOfAnyOfItemResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule], optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if style is not unset:
            kwargs["style"] = style
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.response_format = response_format
