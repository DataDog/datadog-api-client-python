# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecureEmbedViewingPreferencesTheme(ModelSimple):
    """
    The theme of the shared dashboard view. `system` follows the viewer's system default.

    :param value: Must be one of ["system", "light", "dark"].
    :type value: str
    """

    allowed_values = {
        "system",
        "light",
        "dark",
    }
    SYSTEM: ClassVar["SecureEmbedViewingPreferencesTheme"]
    LIGHT: ClassVar["SecureEmbedViewingPreferencesTheme"]
    DARK: ClassVar["SecureEmbedViewingPreferencesTheme"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecureEmbedViewingPreferencesTheme.SYSTEM = SecureEmbedViewingPreferencesTheme("system")
SecureEmbedViewingPreferencesTheme.LIGHT = SecureEmbedViewingPreferencesTheme("light")
SecureEmbedViewingPreferencesTheme.DARK = SecureEmbedViewingPreferencesTheme("dark")
