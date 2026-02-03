# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSignalInvestigationStepOutputVerdict(ModelSimple):
    """
    The verdict from the investigation step.

    :param value: Must be one of ["unspecified", "benign", "suspicious", "inconclusive"].
    :type value: str
    """

    allowed_values = {
        "unspecified",
        "benign",
        "suspicious",
        "inconclusive",
    }
    UNSPECIFIED: ClassVar["SecurityMonitoringSignalInvestigationStepOutputVerdict"]
    BENIGN: ClassVar["SecurityMonitoringSignalInvestigationStepOutputVerdict"]
    SUSPICIOUS: ClassVar["SecurityMonitoringSignalInvestigationStepOutputVerdict"]
    INCONCLUSIVE: ClassVar["SecurityMonitoringSignalInvestigationStepOutputVerdict"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalInvestigationStepOutputVerdict.UNSPECIFIED = (
    SecurityMonitoringSignalInvestigationStepOutputVerdict("unspecified")
)
SecurityMonitoringSignalInvestigationStepOutputVerdict.BENIGN = SecurityMonitoringSignalInvestigationStepOutputVerdict(
    "benign"
)
SecurityMonitoringSignalInvestigationStepOutputVerdict.SUSPICIOUS = (
    SecurityMonitoringSignalInvestigationStepOutputVerdict("suspicious")
)
SecurityMonitoringSignalInvestigationStepOutputVerdict.INCONCLUSIVE = (
    SecurityMonitoringSignalInvestigationStepOutputVerdict("inconclusive")
)
