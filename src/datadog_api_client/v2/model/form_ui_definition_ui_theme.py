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
    from datadog_api_client.v2.model.form_ui_definition_ui_theme_primary_color import (
        FormUiDefinitionUiThemePrimaryColor,
    )


class FormUiDefinitionUiTheme(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_ui_definition_ui_theme_primary_color import (
            FormUiDefinitionUiThemePrimaryColor,
        )

        return {
            "primary_color": (FormUiDefinitionUiThemePrimaryColor,),
        }

    attribute_map = {
        "primary_color": "primaryColor",
    }

    def __init__(self_, primary_color: Union[FormUiDefinitionUiThemePrimaryColor, UnsetType] = unset, **kwargs):
        """
        The visual theme applied to the form.

        :param primary_color: The primary color of the form theme.
        :type primary_color: FormUiDefinitionUiThemePrimaryColor, optional
        """
        if primary_color is not unset:
            kwargs["primary_color"] = primary_color
        super().__init__(kwargs)
