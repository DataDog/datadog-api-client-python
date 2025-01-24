# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RuleSeverity(ModelSimple):
    """
    Severity of a security rule.

    :param value: Must be one of ["critical", "high", "medium", "low", "unknown", "info"].
    :type value: str
    """

    allowed_values = {
        "critical",
        "high",
        "medium",
        "low",
        "unknown",
        "info",
    }
    CRITICAL: ClassVar["RuleSeverity"]
    HIGH: ClassVar["RuleSeverity"]
    MEDIUM: ClassVar["RuleSeverity"]
    LOW: ClassVar["RuleSeverity"]
    UNKNOWN: ClassVar["RuleSeverity"]
    INFO: ClassVar["RuleSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RuleSeverity.CRITICAL = RuleSeverity("critical")
RuleSeverity.HIGH = RuleSeverity("high")
RuleSeverity.MEDIUM = RuleSeverity("medium")
RuleSeverity.LOW = RuleSeverity("low")
RuleSeverity.UNKNOWN = RuleSeverity("unknown")
RuleSeverity.INFO = RuleSeverity("info")
