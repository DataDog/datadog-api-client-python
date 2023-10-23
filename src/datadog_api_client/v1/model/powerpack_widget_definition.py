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
    from datadog_api_client.v1.model.powerpack_template_variables import PowerpackTemplateVariables
    from datadog_api_client.v1.model.powerpack_widget_definition_type import PowerpackWidgetDefinitionType


class PowerpackWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.powerpack_template_variables import PowerpackTemplateVariables
        from datadog_api_client.v1.model.powerpack_widget_definition_type import PowerpackWidgetDefinitionType

        return {
            "background_color": (str,),
            "banner_img": (str,),
            "powerpack_id": (str,),
            "show_title": (bool,),
            "template_variables": (PowerpackTemplateVariables,),
            "title": (str,),
            "type": (PowerpackWidgetDefinitionType,),
        }

    attribute_map = {
        "background_color": "background_color",
        "banner_img": "banner_img",
        "powerpack_id": "powerpack_id",
        "show_title": "show_title",
        "template_variables": "template_variables",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        powerpack_id: str,
        type: PowerpackWidgetDefinitionType,
        background_color: Union[str, UnsetType] = unset,
        banner_img: Union[str, UnsetType] = unset,
        show_title: Union[bool, UnsetType] = unset,
        template_variables: Union[PowerpackTemplateVariables, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The powerpack widget allows you to keep similar graphs together on your timeboard. Each group has a custom header, can hold one to many graphs, and is collapsible.

        :param background_color: Background color of the powerpack title.
        :type background_color: str, optional

        :param banner_img: URL of image to display as a banner for the powerpack.
        :type banner_img: str, optional

        :param powerpack_id: UUID of the associated powerpack.
        :type powerpack_id: str

        :param show_title: Whether to show the title or not.
        :type show_title: bool, optional

        :param template_variables: Powerpack template variables.
        :type template_variables: PowerpackTemplateVariables, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param type: Type of the powerpack widget.
        :type type: PowerpackWidgetDefinitionType
        """
        if background_color is not unset:
            kwargs["background_color"] = background_color
        if banner_img is not unset:
            kwargs["banner_img"] = banner_img
        if show_title is not unset:
            kwargs["show_title"] = show_title
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.powerpack_id = powerpack_id
        self_.type = type
