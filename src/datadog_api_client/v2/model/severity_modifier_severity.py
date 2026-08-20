# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityModifierSeverity(ModelSimple):
    """
    The severity to assign to matched findings. `info_none` is not supported for the `iac_misconfiguration`, `runtime_code_vulnerability`, `secret`, or `static_code_vulnerability` finding types.

    :param value: Must be one of ["info_none", "low", "medium", "high", "critical"].
    :type value: str
    """

    allowed_values = {
        "info_none",
        "low",
        "medium",
        "high",
        "critical",
    }
    INFO_NONE: ClassVar["SeverityModifierSeverity"]
    LOW: ClassVar["SeverityModifierSeverity"]
    MEDIUM: ClassVar["SeverityModifierSeverity"]
    HIGH: ClassVar["SeverityModifierSeverity"]
    CRITICAL: ClassVar["SeverityModifierSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityModifierSeverity.INFO_NONE = SeverityModifierSeverity("info_none")
SeverityModifierSeverity.LOW = SeverityModifierSeverity("low")
SeverityModifierSeverity.MEDIUM = SeverityModifierSeverity("medium")
SeverityModifierSeverity.HIGH = SeverityModifierSeverity("high")
SeverityModifierSeverity.CRITICAL = SeverityModifierSeverity("critical")
