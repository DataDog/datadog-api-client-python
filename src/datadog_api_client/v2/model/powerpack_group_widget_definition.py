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
    from datadog_api_client.v2.model.powerpack_inner_widgets import PowerpackInnerWidgets


class PowerpackGroupWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_inner_widgets import PowerpackInnerWidgets

        return {
            "layout_type": (str,),
            "show_title": (bool,),
            "title": (str,),
            "type": (str,),
            "widgets": ([PowerpackInnerWidgets],),
        }

    attribute_map = {
        "layout_type": "layout_type",
        "show_title": "show_title",
        "title": "title",
        "type": "type",
        "widgets": "widgets",
    }

    def __init__(
        self_,
        layout_type: str,
        type: str,
        widgets: List[PowerpackInnerWidgets],
        show_title: Union[bool, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack group widget object.

        :param layout_type: Layout type of widgets.
        :type layout_type: str

        :param show_title: Boolean indicating whether powerpack group title should be visible or not.
        :type show_title: bool, optional

        :param title: Name for the group widget.
        :type title: str, optional

        :param type: Type of widget, must be group.
        :type type: str

        :param widgets: Widgets inside the powerpack.
        :type widgets: [PowerpackInnerWidgets]
        """
        if show_title is not unset:
            kwargs["show_title"] = show_title
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.layout_type = layout_type
        self_.type = type
        self_.widgets = widgets
