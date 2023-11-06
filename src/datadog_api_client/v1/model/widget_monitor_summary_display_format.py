# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class WidgetMonitorSummaryDisplayFormat(StringEnum):
    """
    What to display on the widget.

    :param value: Must be one of ["counts", "countsAndList", "list"].
    :type value: str
    """

    allowed_values = {
        "counts",
        "countsAndList",
        "list",
    }
    COUNTS: ClassVar["WidgetMonitorSummaryDisplayFormat"]
    COUNTS_AND_LIST: ClassVar["WidgetMonitorSummaryDisplayFormat"]
    LIST: ClassVar["WidgetMonitorSummaryDisplayFormat"]


WidgetMonitorSummaryDisplayFormat.COUNTS = WidgetMonitorSummaryDisplayFormat("counts")
WidgetMonitorSummaryDisplayFormat.COUNTS_AND_LIST = WidgetMonitorSummaryDisplayFormat("countsAndList")
WidgetMonitorSummaryDisplayFormat.LIST = WidgetMonitorSummaryDisplayFormat("list")
