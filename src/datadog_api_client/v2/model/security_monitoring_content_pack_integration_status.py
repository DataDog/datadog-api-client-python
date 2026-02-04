# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackIntegrationStatus(ModelSimple):
    """
    The installation status of the related integration

    :param value: Must be one of ["installed", "available", "partially_installed", "detected", "error"].
    :type value: str
    """

    allowed_values = {
        "installed",
        "available",
        "partially_installed",
        "detected",
        "error",
    }
    INSTALLED: ClassVar["SecurityMonitoringContentPackIntegrationStatus"]
    AVAILABLE: ClassVar["SecurityMonitoringContentPackIntegrationStatus"]
    PARTIALLY_INSTALLED: ClassVar["SecurityMonitoringContentPackIntegrationStatus"]
    DETECTED: ClassVar["SecurityMonitoringContentPackIntegrationStatus"]
    ERROR: ClassVar["SecurityMonitoringContentPackIntegrationStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackIntegrationStatus.INSTALLED = SecurityMonitoringContentPackIntegrationStatus("installed")
SecurityMonitoringContentPackIntegrationStatus.AVAILABLE = SecurityMonitoringContentPackIntegrationStatus("available")
SecurityMonitoringContentPackIntegrationStatus.PARTIALLY_INSTALLED = SecurityMonitoringContentPackIntegrationStatus(
    "partially_installed"
)
SecurityMonitoringContentPackIntegrationStatus.DETECTED = SecurityMonitoringContentPackIntegrationStatus("detected")
SecurityMonitoringContentPackIntegrationStatus.ERROR = SecurityMonitoringContentPackIntegrationStatus("error")
