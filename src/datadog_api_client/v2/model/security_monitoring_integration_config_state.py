# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationConfigState(ModelSimple):
    """
    The state of the credentials configured on the entity context sync.

    :param value: Must be one of ["valid", "invalid", "initializing"].
    :type value: str
    """

    allowed_values = {
        "valid",
        "invalid",
        "initializing",
    }
    VALID: ClassVar["SecurityMonitoringIntegrationConfigState"]
    INVALID: ClassVar["SecurityMonitoringIntegrationConfigState"]
    INITIALIZING: ClassVar["SecurityMonitoringIntegrationConfigState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationConfigState.VALID = SecurityMonitoringIntegrationConfigState("valid")
SecurityMonitoringIntegrationConfigState.INVALID = SecurityMonitoringIntegrationConfigState("invalid")
SecurityMonitoringIntegrationConfigState.INITIALIZING = SecurityMonitoringIntegrationConfigState("initializing")
