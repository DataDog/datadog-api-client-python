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
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.wildcard_widget_request import WildcardWidgetRequest
    from datadog_api_client.v1.model.wildcard_widget_specification import WildcardWidgetSpecification
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.wildcard_widget_definition_type import WildcardWidgetDefinitionType
    from datadog_api_client.v1.model.tree_map_widget_request import TreeMapWidgetRequest
    from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
    from datadog_api_client.v1.model.list_stream_widget_request import ListStreamWidgetRequest
    from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class WildcardWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.wildcard_widget_request import WildcardWidgetRequest
        from datadog_api_client.v1.model.wildcard_widget_specification import WildcardWidgetSpecification
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.wildcard_widget_definition_type import WildcardWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "requests": ([WildcardWidgetRequest],),
            "specification": (WildcardWidgetSpecification,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (WildcardWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "requests": "requests",
        "specification": "specification",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[
            Union[
                WildcardWidgetRequest,
                TreeMapWidgetRequest,
                TimeseriesWidgetRequest,
                ListStreamWidgetRequest,
                DistributionWidgetRequest,
            ]
        ],
        specification: WildcardWidgetSpecification,
        type: WildcardWidgetDefinitionType,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom visualization widget using Vega or Vega-Lite specifications. Combines standard Datadog data requests with a Vega or Vega-Lite JSON specification for flexible, custom visualizations.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: List of data requests for the wildcard widget.
        :type requests: [WildcardWidgetRequest]

        :param specification: Vega or Vega-Lite specification for custom visualization rendering. See https://vega.github.io/vega-lite/ for the full grammar reference.
        :type specification: WildcardWidgetSpecification

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the wildcard widget.
        :type type: WildcardWidgetDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
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
        self_.specification = specification
        self_.type = type
