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
    from datadog_api_client.v1.model.embedded_app_widget_input import EmbeddedAppWidgetInput
    from datadog_api_client.v1.model.widget_time import WidgetTime
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.embedded_app_widget_definition_type import EmbeddedAppWidgetDefinitionType
    from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
    from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
    from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan


class EmbeddedAppWidgetDefinition(ModelNormal):
    validations = {
        "description": {
            "max_length": 5000,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.embedded_app_widget_input import EmbeddedAppWidgetInput
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.embedded_app_widget_definition_type import EmbeddedAppWidgetDefinitionType

        return {
            "app_id": (str,),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "inputs": ([EmbeddedAppWidgetInput],),
            "template_id": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (EmbeddedAppWidgetDefinitionType,),
        }

    attribute_map = {
        "app_id": "app_id",
        "custom_links": "custom_links",
        "description": "description",
        "inputs": "inputs",
        "template_id": "template_id",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        type: EmbeddedAppWidgetDefinitionType,
        app_id: Union[str, UnsetType] = unset,
        custom_links: Union[List[WidgetCustomLink], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        inputs: Union[List[EmbeddedAppWidgetInput], UnsetType] = unset,
        template_id: Union[str, UnsetType] = unset,
        time: Union[WidgetTime, WidgetLegacyLiveSpan, WidgetNewLiveSpan, WidgetNewFixedSpan, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The embedded app widget displays an App Builder app on a dashboard. Exactly one of ``app_id`` or ``template_id`` must be provided; they cannot be provided together.

        :param app_id: UUID of the App Builder app to embed.
        :type app_id: str, optional

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param description: The description of the widget.
        :type description: str, optional

        :param inputs: Inputs passed to the embedded app.
        :type inputs: [EmbeddedAppWidgetInput], optional

        :param template_id: ID of the built-in app template to embed.
        :type template_id: str, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the embedded app widget.
        :type type: EmbeddedAppWidgetDefinitionType
        """
        if app_id is not unset:
            kwargs["app_id"] = app_id
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if inputs is not unset:
            kwargs["inputs"] = inputs
        if template_id is not unset:
            kwargs["template_id"] = template_id
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.type = type
