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
    from datadog_api_client.v2.model.form_ui_definition_ui_theme import FormUiDefinitionUiTheme


class FormUiDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_ui_definition_ui_theme import FormUiDefinitionUiTheme

        return {
            "ui_order": ([str],),
            "ui_theme": (FormUiDefinitionUiTheme,),
        }

    attribute_map = {
        "ui_order": "ui:order",
        "ui_theme": "ui:theme",
    }

    def __init__(
        self_,
        ui_order: Union[List[str], UnsetType] = unset,
        ui_theme: Union[FormUiDefinitionUiTheme, UnsetType] = unset,
        **kwargs,
    ):
        """
        UI configuration for rendering form fields, including widget overrides, field ordering, and themes.

        :param ui_order: The order in which form fields are displayed.
        :type ui_order: [str], optional

        :param ui_theme: The visual theme applied to the form.
        :type ui_theme: FormUiDefinitionUiTheme, optional
        """
        if ui_order is not unset:
            kwargs["ui_order"] = ui_order
        if ui_theme is not unset:
            kwargs["ui_theme"] = ui_theme
        super().__init__(kwargs)
