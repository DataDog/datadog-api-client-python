# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CellDisplayModeOption(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["number", "bar", "trend"].
    :type value: str
    """

    allowed_values = {
        "number",
        "bar",
        "trend",
    }
    NUMBER: ClassVar["CellDisplayModeOption"]
    BAR: ClassVar["CellDisplayModeOption"]
    TREND: ClassVar["CellDisplayModeOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CellDisplayModeOption.NUMBER = CellDisplayModeOption("number")
CellDisplayModeOption.BAR = CellDisplayModeOption("bar")
CellDisplayModeOption.TREND = CellDisplayModeOption("trend")
