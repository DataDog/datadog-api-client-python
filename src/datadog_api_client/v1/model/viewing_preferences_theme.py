# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ViewingPreferencesTheme(ModelSimple):
    """
    The theme of the shared dashboard view. "system" follows your system's default viewing theme.

    :param value: Must be one of ["system", "light", "dark"].
    :type value: str
    """

    allowed_values = {
        "system",
        "light",
        "dark",
    }
    SYSTEM: ClassVar["ViewingPreferencesTheme"]
    LIGHT: ClassVar["ViewingPreferencesTheme"]
    DARK: ClassVar["ViewingPreferencesTheme"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ViewingPreferencesTheme.SYSTEM = ViewingPreferencesTheme("system")
ViewingPreferencesTheme.LIGHT = ViewingPreferencesTheme("light")
ViewingPreferencesTheme.DARK = ViewingPreferencesTheme("dark")
