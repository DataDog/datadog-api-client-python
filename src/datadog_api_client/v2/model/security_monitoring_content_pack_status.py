# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackStatus(ModelSimple):
    """
    The current status of a content pack

    :param value: Must be one of ["install", "activate", "initializing", "active", "warning", "broken"].
    :type value: str
    """

    allowed_values = {
        "install",
        "activate",
        "initializing",
        "active",
        "warning",
        "broken",
    }
    INSTALL: ClassVar["SecurityMonitoringContentPackStatus"]
    ACTIVATE: ClassVar["SecurityMonitoringContentPackStatus"]
    INITIALIZING: ClassVar["SecurityMonitoringContentPackStatus"]
    ACTIVE: ClassVar["SecurityMonitoringContentPackStatus"]
    WARNING: ClassVar["SecurityMonitoringContentPackStatus"]
    BROKEN: ClassVar["SecurityMonitoringContentPackStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackStatus.INSTALL = SecurityMonitoringContentPackStatus("install")
SecurityMonitoringContentPackStatus.ACTIVATE = SecurityMonitoringContentPackStatus("activate")
SecurityMonitoringContentPackStatus.INITIALIZING = SecurityMonitoringContentPackStatus("initializing")
SecurityMonitoringContentPackStatus.ACTIVE = SecurityMonitoringContentPackStatus("active")
SecurityMonitoringContentPackStatus.WARNING = SecurityMonitoringContentPackStatus("warning")
SecurityMonitoringContentPackStatus.BROKEN = SecurityMonitoringContentPackStatus("broken")
