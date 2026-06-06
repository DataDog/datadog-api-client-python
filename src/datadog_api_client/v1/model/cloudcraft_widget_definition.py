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
    from datadog_api_client.v1.model.cloudcraft_widget_definition_overlay import CloudcraftWidgetDefinitionOverlay
    from datadog_api_client.v1.model.cloudcraft_widget_definition_projection import CloudcraftWidgetDefinitionProjection
    from datadog_api_client.v1.model.cloudcraft_widget_definition_provider import CloudcraftWidgetDefinitionProvider
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.cloudcraft_widget_definition_type import CloudcraftWidgetDefinitionType


class CloudcraftWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.cloudcraft_widget_definition_overlay import CloudcraftWidgetDefinitionOverlay
        from datadog_api_client.v1.model.cloudcraft_widget_definition_projection import (
            CloudcraftWidgetDefinitionProjection,
        )
        from datadog_api_client.v1.model.cloudcraft_widget_definition_provider import CloudcraftWidgetDefinitionProvider
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.cloudcraft_widget_definition_type import CloudcraftWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "group_by": ([str],),
            "highlighted": (str,),
            "overlay": (CloudcraftWidgetDefinitionOverlay,),
            "overlay_filter": (str,),
            "projection": (CloudcraftWidgetDefinitionProjection,),
            "provider": (CloudcraftWidgetDefinitionProvider,),
            "query_string": (str,),
            "show_empty_groups": (bool,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (CloudcraftWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
        "group_by": "group_by",
        "highlighted": "highlighted",
        "overlay": "overlay",
        "overlay_filter": "overlay_filter",
        "projection": "projection",
        "provider": "provider",
        "query_string": "query_string",
        "show_empty_groups": "show_empty_groups",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        group_by: List[str],
        highlighted: str,
        overlay: CloudcraftWidgetDefinitionOverlay,
        overlay_filter: str,
        projection: CloudcraftWidgetDefinitionProjection,
        provider: CloudcraftWidgetDefinitionProvider,
        query_string: str,
        show_empty_groups: bool,
        type: CloudcraftWidgetDefinitionType,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        This widget displays a Cloudcraft topology of cloud resources for the selected provider.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param description: The description of the widget.
        :type description: str, optional

        :param group_by: List of tags or attributes used to group the cloud resources in the widget.
        :type group_by: [str]

        :param highlighted: Search query that visually highlights matching resources in the diagram.
        :type highlighted: str

        :param overlay: Overlay applied on top of the Cloudcraft topology.
        :type overlay: CloudcraftWidgetDefinitionOverlay

        :param overlay_filter: Filter applied to the selected overlay.
        :type overlay_filter: str

        :param projection: Projection used to render the Cloudcraft topology.
        :type projection: CloudcraftWidgetDefinitionProjection

        :param provider: Cloud provider for the Cloudcraft widget.
        :type provider: CloudcraftWidgetDefinitionProvider

        :param query_string: Query string used to filter the cloud resources displayed in the widget.
        :type query_string: str

        :param show_empty_groups: Whether to show empty outline groups in the diagram.
        :type show_empty_groups: bool

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of Cloudcraft widget.
        :type type: CloudcraftWidgetDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.group_by = group_by
        self_.highlighted = highlighted
        self_.overlay = overlay
        self_.overlay_filter = overlay_filter
        self_.projection = projection
        self_.provider = provider
        self_.query_string = query_string
        self_.show_empty_groups = show_empty_groups
        self_.type = type
