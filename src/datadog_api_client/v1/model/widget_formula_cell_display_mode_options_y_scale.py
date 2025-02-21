# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetFormulaCellDisplayModeOptionsYScale(ModelSimple):
    """
    Y scale for the cell display mode options.

    :param value: Must be one of ["shared", "independent"].
    :type value: str
    """

    allowed_values = {
        "shared",
        "independent",
    }
    SHARED: ClassVar["WidgetFormulaCellDisplayModeOptionsYScale"]
    INDEPENDENT: ClassVar["WidgetFormulaCellDisplayModeOptionsYScale"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetFormulaCellDisplayModeOptionsYScale.SHARED = WidgetFormulaCellDisplayModeOptionsYScale("shared")
WidgetFormulaCellDisplayModeOptionsYScale.INDEPENDENT = WidgetFormulaCellDisplayModeOptionsYScale("independent")
