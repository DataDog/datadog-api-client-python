# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSignalInvestigationType(ModelSimple):
    """
    The type of investigation signal.

    :param value: If omitted defaults to "investigation_signal". Must be one of ["investigation_signal"].
    :type value: str
    """

    allowed_values = {
        "investigation_signal",
    }
    INVESTIGATION_SIGNAL: ClassVar["SecurityMonitoringSignalInvestigationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalInvestigationType.INVESTIGATION_SIGNAL = SecurityMonitoringSignalInvestigationType(
    "investigation_signal"
)
