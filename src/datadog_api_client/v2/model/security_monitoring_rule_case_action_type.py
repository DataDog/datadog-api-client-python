# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleCaseActionType(ModelSimple):
    """
    The action type.

    :param value: Must be one of ["block_ip", "block_user", "user_behavior"].
    :type value: str
    """

    allowed_values = {
        "block_ip",
        "block_user",
        "user_behavior",
    }
    BLOCK_IP: ClassVar["SecurityMonitoringRuleCaseActionType"]
    BLOCK_USER: ClassVar["SecurityMonitoringRuleCaseActionType"]
    USER_BEHAVIOR: ClassVar["SecurityMonitoringRuleCaseActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleCaseActionType.BLOCK_IP = SecurityMonitoringRuleCaseActionType("block_ip")
SecurityMonitoringRuleCaseActionType.BLOCK_USER = SecurityMonitoringRuleCaseActionType("block_user")
SecurityMonitoringRuleCaseActionType.USER_BEHAVIOR = SecurityMonitoringRuleCaseActionType("user_behavior")
