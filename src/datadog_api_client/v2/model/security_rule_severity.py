# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityRuleSeverity(ModelSimple):
    """
    Severity of a security rule

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
    CRITICAL: ClassVar["SecurityRuleSeverity"]
    HIGH: ClassVar["SecurityRuleSeverity"]
    MEDIUM: ClassVar["SecurityRuleSeverity"]
    LOW: ClassVar["SecurityRuleSeverity"]
    UNKNOWN: ClassVar["SecurityRuleSeverity"]
    INFO: ClassVar["SecurityRuleSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityRuleSeverity.CRITICAL = SecurityRuleSeverity("critical")
SecurityRuleSeverity.HIGH = SecurityRuleSeverity("high")
SecurityRuleSeverity.MEDIUM = SecurityRuleSeverity("medium")
SecurityRuleSeverity.LOW = SecurityRuleSeverity("low")
SecurityRuleSeverity.UNKNOWN = SecurityRuleSeverity("unknown")
SecurityRuleSeverity.INFO = SecurityRuleSeverity("info")
