# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackActivation(ModelSimple):
    """
    The activation status of a content pack

    :param value: Must be one of ["never_activated", "activated", "deactivated"].
    :type value: str
    """

    allowed_values = {
        "never_activated",
        "activated",
        "deactivated",
    }
    NEVER_ACTIVATED: ClassVar["SecurityMonitoringContentPackActivation"]
    ACTIVATED: ClassVar["SecurityMonitoringContentPackActivation"]
    DEACTIVATED: ClassVar["SecurityMonitoringContentPackActivation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackActivation.NEVER_ACTIVATED = SecurityMonitoringContentPackActivation("never_activated")
SecurityMonitoringContentPackActivation.ACTIVATED = SecurityMonitoringContentPackActivation("activated")
SecurityMonitoringContentPackActivation.DEACTIVATED = SecurityMonitoringContentPackActivation("deactivated")
