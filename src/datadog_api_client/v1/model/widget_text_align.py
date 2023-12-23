# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class WidgetTextAlign(StringEnum):
    """
    How to align the text on the widget.

    :param value: Must be one of ["center", "left", "right"].
    :type value: str
    """

    allowed_values = {
        "center",
        "left",
        "right",
    }
    CENTER: ClassVar["WidgetTextAlign"]
    LEFT: ClassVar["WidgetTextAlign"]
    RIGHT: ClassVar["WidgetTextAlign"]


WidgetTextAlign.CENTER = WidgetTextAlign("center")
WidgetTextAlign.LEFT = WidgetTextAlign("left")
WidgetTextAlign.RIGHT = WidgetTextAlign("right")
