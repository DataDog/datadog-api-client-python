# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityOverrideValue(ModelSimple):
    """
    Severity to apply to the findings.
        `info` sets the lowest severity the finding type allows.

    :param value: Must be one of ["critical", "high", "medium", "low", "info"].
    :type value: str
    """

    allowed_values = {
        "critical",
        "high",
        "medium",
        "low",
        "info",
    }
    CRITICAL: ClassVar["SeverityOverrideValue"]
    HIGH: ClassVar["SeverityOverrideValue"]
    MEDIUM: ClassVar["SeverityOverrideValue"]
    LOW: ClassVar["SeverityOverrideValue"]
    INFO: ClassVar["SeverityOverrideValue"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityOverrideValue.CRITICAL = SeverityOverrideValue("critical")
SeverityOverrideValue.HIGH = SeverityOverrideValue("high")
SeverityOverrideValue.MEDIUM = SeverityOverrideValue("medium")
SeverityOverrideValue.LOW = SeverityOverrideValue("low")
SeverityOverrideValue.INFO = SeverityOverrideValue("info")
