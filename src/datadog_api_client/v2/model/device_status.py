# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeviceStatus(ModelSimple):
    """
    Health status of the device, computed from its issues and recent telemetry.
        `inactive` means the device stopped reporting. `unknown` means no telemetry is available yet.

    :param value: Must be one of ["healthy", "degraded", "critical", "inactive", "unknown"].
    :type value: str
    """

    allowed_values = {
        "healthy",
        "degraded",
        "critical",
        "inactive",
        "unknown",
    }
    HEALTHY: ClassVar["DeviceStatus"]
    DEGRADED: ClassVar["DeviceStatus"]
    CRITICAL: ClassVar["DeviceStatus"]
    INACTIVE: ClassVar["DeviceStatus"]
    UNKNOWN: ClassVar["DeviceStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeviceStatus.HEALTHY = DeviceStatus("healthy")
DeviceStatus.DEGRADED = DeviceStatus("degraded")
DeviceStatus.CRITICAL = DeviceStatus("critical")
DeviceStatus.INACTIVE = DeviceStatus("inactive")
DeviceStatus.UNKNOWN = DeviceStatus("unknown")
