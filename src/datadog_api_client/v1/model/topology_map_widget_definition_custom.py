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
    from datadog_api_client.v1.model.topology_map_inline_data import TopologyMapInlineData
    from datadog_api_client.v1.model.topology_map_layout import TopologyMapLayout
    from datadog_api_client.v1.model.topology_request_custom import TopologyRequestCustom
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class TopologyMapWidgetDefinitionCustom(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.topology_map_inline_data import TopologyMapInlineData
        from datadog_api_client.v1.model.topology_map_layout import TopologyMapLayout
        from datadog_api_client.v1.model.topology_request_custom import TopologyRequestCustom
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "data": (TopologyMapInlineData,),
            "description": (str,),
            "layout": (TopologyMapLayout,),
            "requests": ([TopologyRequestCustom],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TopologyMapWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "data": "data",
        "description": "description",
        "layout": "layout",
        "requests": "requests",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        layout: TopologyMapLayout,
        requests: List[TopologyRequestCustom],
        type: TopologyMapWidgetDefinitionType,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        data: Union[TopologyMapInlineData, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom topology map widget. Renders nodes and edges from inline ``data`` and from scalar ``requests``. There is one node for each node ID found in ``data.nodes`` , ``data.edges`` , and ``requests``. When ``data`` and several requests set the same field on the same node (such as ``title`` or ``values[0]`` ), the last non-null value wins.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param data: Static nodes and edges, stored in columns. Within a table, every column must have the same number of values and a unique ``id``.
        :type data: TopologyMapInlineData, optional

        :param description: The description of the widget.
        :type description: str, optional

        :param layout: Algorithm that positions nodes and edges. The ``hierarchical`` layout places nodes in ranks so edges flow in one direction.
        :type layout: TopologyMapLayout

        :param requests: List of scalar requests that supply node data. Can be empty.
        :type requests: [TopologyRequestCustom]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the topology map widget.
        :type type: TopologyMapWidgetDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if data is not unset:
            kwargs["data"] = data
        if description is not unset:
            kwargs["description"] = description
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.layout = layout
        self_.requests = requests
        self_.type = type
