# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DueDateSeverity(ModelSimple):
    """
    A severity level used to configure due date thresholds.

    :param value: Must be one of ["critical", "high", "medium", "low", "info", "none", "unknown"].
    :type value: str
    """

    allowed_values = {
        "critical",
        "high",
        "medium",
        "low",
        "info",
        "none",
        "unknown",
    }
    CRITICAL: ClassVar["DueDateSeverity"]
    HIGH: ClassVar["DueDateSeverity"]
    MEDIUM: ClassVar["DueDateSeverity"]
    LOW: ClassVar["DueDateSeverity"]
    INFO: ClassVar["DueDateSeverity"]
    NONE: ClassVar["DueDateSeverity"]
    UNKNOWN: ClassVar["DueDateSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DueDateSeverity.CRITICAL = DueDateSeverity("critical")
DueDateSeverity.HIGH = DueDateSeverity("high")
DueDateSeverity.MEDIUM = DueDateSeverity("medium")
DueDateSeverity.LOW = DueDateSeverity("low")
DueDateSeverity.INFO = DueDateSeverity("info")
DueDateSeverity.NONE = DueDateSeverity("none")
DueDateSeverity.UNKNOWN = DueDateSeverity("unknown")
