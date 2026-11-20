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
    from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
    from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition
    from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import TimeseriesWidgetExpressionAlias
    from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle


class TimeseriesWidgetEventRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
        from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import (
            TimeseriesWidgetExpressionAlias,
        )
        from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle

        return {
            "display_type": (WidgetDisplayType,),
            "event_query": (LogQueryDefinition,),
            "metadata": ([TimeseriesWidgetExpressionAlias],),
            "on_right_yaxis": (bool,),
            "style": (TimeseriesRequestStyle,),
        }

    attribute_map = {
        "display_type": "display_type",
        "event_query": "event_query",
        "metadata": "metadata",
        "on_right_yaxis": "on_right_yaxis",
        "style": "style",
    }

    def __init__(
        self_,
        event_query: LogQueryDefinition,
        display_type: Union[WidgetDisplayType, UnsetType] = unset,
        metadata: Union[List[TimeseriesWidgetExpressionAlias], UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        style: Union[TimeseriesRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: WidgetDisplayType, optional

        :param event_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type event_query: LogQueryDefinition

        :param metadata: Test-only generated schema for the dashboard versioning proof of concept.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TimeseriesRequestStyle, optional
        """
        if display_type is not unset:
            kwargs["display_type"] = display_type
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if on_right_yaxis is not unset:
            kwargs["on_right_yaxis"] = on_right_yaxis
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.event_query = event_query
