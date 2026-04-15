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
    from datadog_api_client.v1.model.funnel_grouped_display import FunnelGroupedDisplay
    from datadog_api_client.v1.model.product_analytics_funnel_request import ProductAnalyticsFunnelRequest
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class ProductAnalyticsFunnelWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.funnel_grouped_display import FunnelGroupedDisplay
        from datadog_api_client.v1.model.product_analytics_funnel_request import ProductAnalyticsFunnelRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.funnel_widget_definition_type import FunnelWidgetDefinitionType

        return {
            "description": (str,),
            "grouped_display": (FunnelGroupedDisplay,),
            "requests": ([ProductAnalyticsFunnelRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (FunnelWidgetDefinitionType,),
        }

    attribute_map = {
        "description": "description",
        "grouped_display": "grouped_display",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[ProductAnalyticsFunnelRequest],
        type: FunnelWidgetDefinitionType,
        description: Union[str, UnsetType] = unset,
        grouped_display: Union[FunnelGroupedDisplay, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The user journey funnel visualization displays conversion funnels based on user journey data from Product Analytics.

        :param description: The description of the widget.
        :type description: str, optional

        :param grouped_display: Display mode for grouped funnel results.
        :type grouped_display: FunnelGroupedDisplay, optional

        :param requests: Request payload used to query items.
        :type requests: [ProductAnalyticsFunnelRequest]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: The title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: The size of the title.
        :type title_size: str, optional

        :param type: Type of funnel widget.
        :type type: FunnelWidgetDefinitionType
        """
        if description is not unset:
            kwargs["description"] = description
        if grouped_display is not unset:
            kwargs["grouped_display"] = grouped_display
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
