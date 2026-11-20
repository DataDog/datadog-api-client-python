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
    from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import TimeseriesWidgetExpressionAlias
    from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request_request_type import (
        TimeseriesWidgetDdsqlRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request_response_format import (
        TimeseriesWidgetDdsqlRequestResponseFormat,
    )
    from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle


class TimeseriesWidgetDdsqlRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
        from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import (
            TimeseriesWidgetExpressionAlias,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request_request_type import (
            TimeseriesWidgetDdsqlRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_ddsql_request_response_format import (
            TimeseriesWidgetDdsqlRequestResponseFormat,
        )
        from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle

        return {
            "ddsql_query": (str,),
            "display_type": (WidgetDisplayType,),
            "metadata": ([TimeseriesWidgetExpressionAlias],),
            "on_right_yaxis": (bool,),
            "request_type": (TimeseriesWidgetDdsqlRequestRequestType,),
            "response_format": (TimeseriesWidgetDdsqlRequestResponseFormat,),
            "style": (TimeseriesRequestStyle,),
        }

    attribute_map = {
        "ddsql_query": "ddsql_query",
        "display_type": "display_type",
        "metadata": "metadata",
        "on_right_yaxis": "on_right_yaxis",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: TimeseriesWidgetDdsqlRequestRequestType,
        response_format: TimeseriesWidgetDdsqlRequestResponseFormat,
        display_type: Union[WidgetDisplayType, UnsetType] = unset,
        metadata: Union[List[TimeseriesWidgetExpressionAlias], UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        style: Union[TimeseriesRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: WidgetDisplayType, optional

        :param metadata: Test-only generated schema for the dashboard versioning proof of concept.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TimeseriesWidgetDdsqlRequestRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TimeseriesWidgetDdsqlRequestResponseFormat

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

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format
