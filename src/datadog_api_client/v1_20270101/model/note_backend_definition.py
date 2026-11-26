# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.note_backend_definition_text_align import NoteBackendDefinitionTextAlign
    from datadog_api_client.v1_20270101.model.note_backend_definition_tick_edge import NoteBackendDefinitionTickEdge
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.note_backend_definition_type import NoteBackendDefinitionType
    from datadog_api_client.v1_20270101.model.note_backend_definition_vertical_align import (
        NoteBackendDefinitionVerticalAlign,
    )


class NoteBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.note_backend_definition_text_align import (
            NoteBackendDefinitionTextAlign,
        )
        from datadog_api_client.v1_20270101.model.note_backend_definition_tick_edge import NoteBackendDefinitionTickEdge
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.note_backend_definition_type import NoteBackendDefinitionType
        from datadog_api_client.v1_20270101.model.note_backend_definition_vertical_align import (
            NoteBackendDefinitionVerticalAlign,
        )

        return {
            "background_color": (str,),
            "content": (str,),
            "description": (str,),
            "font_size": (str,),
            "has_padding": (bool,),
            "notes": (str,),
            "show_tick": (bool,),
            "text_align": (NoteBackendDefinitionTextAlign,),
            "tick_edge": (NoteBackendDefinitionTickEdge,),
            "tick_pos": (str,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (NoteBackendDefinitionType,),
            "vertical_align": (NoteBackendDefinitionVerticalAlign,),
        }

    attribute_map = {
        "background_color": "background_color",
        "content": "content",
        "description": "description",
        "font_size": "font_size",
        "has_padding": "has_padding",
        "notes": "notes",
        "show_tick": "show_tick",
        "text_align": "text_align",
        "tick_edge": "tick_edge",
        "tick_pos": "tick_pos",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "vertical_align": "vertical_align",
    }

    def __init__(
        self_,
        content: str,
        type: NoteBackendDefinitionType,
        background_color: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        font_size: Union[str, UnsetType] = unset,
        has_padding: Union[bool, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        show_tick: Union[bool, UnsetType] = unset,
        text_align: Union[NoteBackendDefinitionTextAlign, UnsetType] = unset,
        tick_edge: Union[NoteBackendDefinitionTickEdge, UnsetType] = unset,
        tick_pos: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        vertical_align: Union[NoteBackendDefinitionVerticalAlign, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param background_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type background_color: str, optional

        :param content: Test-only generated schema for the dashboard versioning proof of concept.
        :type content: str

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param font_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type font_size: str, optional

        :param has_padding: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_padding: bool, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param show_tick: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_tick: bool, optional

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: NoteBackendDefinitionTextAlign, optional

        :param tick_edge: Test-only generated schema for the dashboard versioning proof of concept.
        :type tick_edge: NoteBackendDefinitionTickEdge, optional

        :param tick_pos: Test-only generated schema for the dashboard versioning proof of concept.
        :type tick_pos: str, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: NoteBackendDefinitionType

        :param vertical_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type vertical_align: NoteBackendDefinitionVerticalAlign, optional
        """
        if background_color is not unset:
            kwargs["background_color"] = background_color
        if description is not unset:
            kwargs["description"] = description
        if font_size is not unset:
            kwargs["font_size"] = font_size
        if has_padding is not unset:
            kwargs["has_padding"] = has_padding
        if notes is not unset:
            kwargs["notes"] = notes
        if show_tick is not unset:
            kwargs["show_tick"] = show_tick
        if text_align is not unset:
            kwargs["text_align"] = text_align
        if tick_edge is not unset:
            kwargs["tick_edge"] = tick_edge
        if tick_pos is not unset:
            kwargs["tick_pos"] = tick_pos
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        if vertical_align is not unset:
            kwargs["vertical_align"] = vertical_align
        super().__init__(kwargs)

        self_.content = content
        self_.type = type
