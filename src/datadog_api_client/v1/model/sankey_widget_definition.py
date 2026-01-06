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
    from datadog_api_client.v1.model.sankey_widget_request import SankeyWidgetRequest
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.sankey_widget_definition_type import SankeyWidgetDefinitionType
    from datadog_api_client.v1.model.sankey_rum_request import SankeyRumRequest
    from datadog_api_client.v1.model.sankey_network_request import SankeyNetworkRequest
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class SankeyWidgetDefinition(ModelNormal):
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
        from datadog_api_client.v1.model.sankey_widget_request import SankeyWidgetRequest
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.sankey_widget_definition_type import SankeyWidgetDefinitionType

        return {
            "requests": ([SankeyWidgetRequest],),
            "show_other_links": (bool,),
            "sort_nodes": (bool,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SankeyWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "show_other_links": "show_other_links",
        "sort_nodes": "sort_nodes",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[Union[SankeyWidgetRequest, SankeyRumRequest, SankeyNetworkRequest]],
        type: SankeyWidgetDefinitionType,
        show_other_links: Union[bool, UnsetType] = unset,
        sort_nodes: Union[bool, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Sankey diagram visualizes the flow of data between categories, stages or sets of values.

        :param requests: List of Sankey widget requests.
        :type requests: [SankeyWidgetRequest]

        :param show_other_links: Whether to show links for "other" category.
        :type show_other_links: bool, optional

        :param sort_nodes: Whether to sort nodes in the Sankey diagram.
        :type sort_nodes: bool, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the Sankey widget.
        :type type: SankeyWidgetDefinitionType
        """
        if show_other_links is not unset:
            kwargs["show_other_links"] = show_other_links
        if sort_nodes is not unset:
            kwargs["sort_nodes"] = sort_nodes
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
