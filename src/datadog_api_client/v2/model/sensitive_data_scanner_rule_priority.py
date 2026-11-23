# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SensitiveDataScannerRulePriority(ModelSimple):
    """
    Severity of the issues found by the rule.

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
    CRITICAL: ClassVar["SensitiveDataScannerRulePriority"]
    HIGH: ClassVar["SensitiveDataScannerRulePriority"]
    MEDIUM: ClassVar["SensitiveDataScannerRulePriority"]
    LOW: ClassVar["SensitiveDataScannerRulePriority"]
    INFO: ClassVar["SensitiveDataScannerRulePriority"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SensitiveDataScannerRulePriority.CRITICAL = SensitiveDataScannerRulePriority("critical")
SensitiveDataScannerRulePriority.HIGH = SensitiveDataScannerRulePriority("high")
SensitiveDataScannerRulePriority.MEDIUM = SensitiveDataScannerRulePriority("medium")
SensitiveDataScannerRulePriority.LOW = SensitiveDataScannerRulePriority("low")
SensitiveDataScannerRulePriority.INFO = SensitiveDataScannerRulePriority("info")
