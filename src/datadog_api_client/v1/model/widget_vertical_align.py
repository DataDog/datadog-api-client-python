# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class WidgetVerticalAlign(StringEnum):
    """
    Vertical alignment.

    :param value: Must be one of ["center", "top", "bottom"].
    :type value: str
    """

    allowed_values = {
        "center",
        "top",
        "bottom",
    }
    CENTER: ClassVar["WidgetVerticalAlign"]
    TOP: ClassVar["WidgetVerticalAlign"]
    BOTTOM: ClassVar["WidgetVerticalAlign"]


WidgetVerticalAlign.CENTER = WidgetVerticalAlign("center")
WidgetVerticalAlign.TOP = WidgetVerticalAlign("top")
WidgetVerticalAlign.BOTTOM = WidgetVerticalAlign("bottom")
