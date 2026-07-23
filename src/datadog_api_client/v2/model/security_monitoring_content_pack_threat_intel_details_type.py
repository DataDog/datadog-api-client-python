# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackThreatIntelDetailsType(ModelSimple):
    """
    Type for threat intelligence content pack details.

    :param value: If omitted defaults to "threat_intel". Must be one of ["threat_intel"].
    :type value: str
    """

    allowed_values = {
        "threat_intel",
    }
    THREAT_INTEL: ClassVar["SecurityMonitoringContentPackThreatIntelDetailsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackThreatIntelDetailsType.THREAT_INTEL = SecurityMonitoringContentPackThreatIntelDetailsType(
    "threat_intel"
)
