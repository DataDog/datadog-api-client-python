# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema49(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["custom_bg", "custom_text", "custom_image"].
    :type value: str
    """

    allowed_values = {
        "custom_bg",
        "custom_text",
        "custom_image",
    }
    CUSTOM_BG: ClassVar["DashboardInlineSchema49"]
    CUSTOM_TEXT: ClassVar["DashboardInlineSchema49"]
    CUSTOM_IMAGE: ClassVar["DashboardInlineSchema49"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema49.CUSTOM_BG = DashboardInlineSchema49("custom_bg")
DashboardInlineSchema49.CUSTOM_TEXT = DashboardInlineSchema49("custom_text")
DashboardInlineSchema49.CUSTOM_IMAGE = DashboardInlineSchema49("custom_image")
