# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class WidgetSizeFormat(StringEnum):
    """
    Size of the widget.

    :param value: Must be one of ["small", "medium", "large"].
    :type value: str
    """

    allowed_values = {
        "small",
        "medium",
        "large",
    }
    SMALL: ClassVar["WidgetSizeFormat"]
    MEDIUM: ClassVar["WidgetSizeFormat"]
    LARGE: ClassVar["WidgetSizeFormat"]


WidgetSizeFormat.SMALL = WidgetSizeFormat("small")
WidgetSizeFormat.MEDIUM = WidgetSizeFormat("medium")
WidgetSizeFormat.LARGE = WidgetSizeFormat("large")
