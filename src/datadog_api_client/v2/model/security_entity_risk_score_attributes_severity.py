# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityEntityRiskScoreAttributesSeverity(ModelSimple):
    """
    Severity level based on risk score

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
    CRITICAL: ClassVar["SecurityEntityRiskScoreAttributesSeverity"]
    HIGH: ClassVar["SecurityEntityRiskScoreAttributesSeverity"]
    MEDIUM: ClassVar["SecurityEntityRiskScoreAttributesSeverity"]
    LOW: ClassVar["SecurityEntityRiskScoreAttributesSeverity"]
    INFO: ClassVar["SecurityEntityRiskScoreAttributesSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityEntityRiskScoreAttributesSeverity.CRITICAL = SecurityEntityRiskScoreAttributesSeverity("critical")
SecurityEntityRiskScoreAttributesSeverity.HIGH = SecurityEntityRiskScoreAttributesSeverity("high")
SecurityEntityRiskScoreAttributesSeverity.MEDIUM = SecurityEntityRiskScoreAttributesSeverity("medium")
SecurityEntityRiskScoreAttributesSeverity.LOW = SecurityEntityRiskScoreAttributesSeverity("low")
SecurityEntityRiskScoreAttributesSeverity.INFO = SecurityEntityRiskScoreAttributesSeverity("info")
