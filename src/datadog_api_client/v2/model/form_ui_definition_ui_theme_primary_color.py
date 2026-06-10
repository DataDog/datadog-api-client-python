# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormUiDefinitionUiThemePrimaryColor(ModelSimple):
    """
    The primary color of the form theme.

    :param value: Must be one of ["gray", "red", "orange", "yellow", "green", "light-blue", "dark-blue", "magenta", "indigo"].
    :type value: str
    """

    allowed_values = {
        "gray",
        "red",
        "orange",
        "yellow",
        "green",
        "light-blue",
        "dark-blue",
        "magenta",
        "indigo",
    }
    GRAY: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    RED: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    ORANGE: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    YELLOW: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    GREEN: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    LIGHT_BLUE: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    DARK_BLUE: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    MAGENTA: ClassVar["FormUiDefinitionUiThemePrimaryColor"]
    INDIGO: ClassVar["FormUiDefinitionUiThemePrimaryColor"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormUiDefinitionUiThemePrimaryColor.GRAY = FormUiDefinitionUiThemePrimaryColor("gray")
FormUiDefinitionUiThemePrimaryColor.RED = FormUiDefinitionUiThemePrimaryColor("red")
FormUiDefinitionUiThemePrimaryColor.ORANGE = FormUiDefinitionUiThemePrimaryColor("orange")
FormUiDefinitionUiThemePrimaryColor.YELLOW = FormUiDefinitionUiThemePrimaryColor("yellow")
FormUiDefinitionUiThemePrimaryColor.GREEN = FormUiDefinitionUiThemePrimaryColor("green")
FormUiDefinitionUiThemePrimaryColor.LIGHT_BLUE = FormUiDefinitionUiThemePrimaryColor("light-blue")
FormUiDefinitionUiThemePrimaryColor.DARK_BLUE = FormUiDefinitionUiThemePrimaryColor("dark-blue")
FormUiDefinitionUiThemePrimaryColor.MAGENTA = FormUiDefinitionUiThemePrimaryColor("magenta")
FormUiDefinitionUiThemePrimaryColor.INDIGO = FormUiDefinitionUiThemePrimaryColor("indigo")
