# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleCaseActionOptionsFlaggedIPType(ModelSimple):
    """
    Used with the case action of type 'flag_ip'. The value specified in this field is applied as a flag to the IP addresses.

    :param value: Must be one of ["SUSPICIOUS", "FLAGGED"].
    :type value: str
    """

    allowed_values = {
        "SUSPICIOUS",
        "FLAGGED",
    }
    SUSPICIOUS: ClassVar["SecurityMonitoringRuleCaseActionOptionsFlaggedIPType"]
    FLAGGED: ClassVar["SecurityMonitoringRuleCaseActionOptionsFlaggedIPType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleCaseActionOptionsFlaggedIPType.SUSPICIOUS = SecurityMonitoringRuleCaseActionOptionsFlaggedIPType(
    "SUSPICIOUS"
)
SecurityMonitoringRuleCaseActionOptionsFlaggedIPType.FLAGGED = SecurityMonitoringRuleCaseActionOptionsFlaggedIPType(
    "FLAGGED"
)
