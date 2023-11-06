# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class TableWidgetCellDisplayMode(StringEnum):
    """
    Define a display mode for the table cell.

    :param value: Must be one of ["number", "bar"].
    :type value: str
    """

    allowed_values = {
        "number",
        "bar",
    }
    NUMBER: ClassVar["TableWidgetCellDisplayMode"]
    BAR: ClassVar["TableWidgetCellDisplayMode"]


TableWidgetCellDisplayMode.NUMBER = TableWidgetCellDisplayMode("number")
TableWidgetCellDisplayMode.BAR = TableWidgetCellDisplayMode("bar")
