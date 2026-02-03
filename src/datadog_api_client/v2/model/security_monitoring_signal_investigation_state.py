# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSignalInvestigationState(ModelSimple):
    """
    The state of the investigation.

    :param value: Must be one of ["investigating", "completed"].
    :type value: str
    """

    allowed_values = {
        "investigating",
        "completed",
    }
    INVESTIGATING: ClassVar["SecurityMonitoringSignalInvestigationState"]
    COMPLETED: ClassVar["SecurityMonitoringSignalInvestigationState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalInvestigationState.INVESTIGATING = SecurityMonitoringSignalInvestigationState("investigating")
SecurityMonitoringSignalInvestigationState.COMPLETED = SecurityMonitoringSignalInvestigationState("completed")
