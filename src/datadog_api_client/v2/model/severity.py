# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Severity(ModelSimple):
    """
    The vulnerability severity.

    :param value: Must be one of ["Unknown", "None", "Low", "Medium", "High", "Critical"].
    :type value: str
    """

    allowed_values = {
        "Unknown",
        "None",
        "Low",
        "Medium",
        "High",
        "Critical",
    }
    UNKNOWN: ClassVar["Severity"]
    NONE: ClassVar["Severity"]
    LOW: ClassVar["Severity"]
    MEDIUM: ClassVar["Severity"]
    HIGH: ClassVar["Severity"]
    CRITICAL: ClassVar["Severity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Severity.UNKNOWN = Severity("Unknown")
Severity.NONE = Severity("None")
Severity.LOW = Severity("Low")
Severity.MEDIUM = Severity("Medium")
Severity.HIGH = Severity("High")
Severity.CRITICAL = Severity("Critical")
