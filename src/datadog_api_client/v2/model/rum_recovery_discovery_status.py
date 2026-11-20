# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMRecoveryDiscoveryStatus(ModelSimple):
    """
    Batch discovery state. QUEUED indicates that the request is waiting for processing capacity.

    :param value: Must be one of ["QUEUED", "PENDING", "SLICING", "DISCOVERED", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED"].
    :type value: str
    """

    allowed_values = {
        "QUEUED",
        "PENDING",
        "SLICING",
        "DISCOVERED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    }
    QUEUED: ClassVar["RUMRecoveryDiscoveryStatus"]
    PENDING: ClassVar["RUMRecoveryDiscoveryStatus"]
    SLICING: ClassVar["RUMRecoveryDiscoveryStatus"]
    DISCOVERED: ClassVar["RUMRecoveryDiscoveryStatus"]
    PROCESSING: ClassVar["RUMRecoveryDiscoveryStatus"]
    COMPLETED: ClassVar["RUMRecoveryDiscoveryStatus"]
    FAILED: ClassVar["RUMRecoveryDiscoveryStatus"]
    CANCELLED: ClassVar["RUMRecoveryDiscoveryStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMRecoveryDiscoveryStatus.QUEUED = RUMRecoveryDiscoveryStatus("QUEUED")
RUMRecoveryDiscoveryStatus.PENDING = RUMRecoveryDiscoveryStatus("PENDING")
RUMRecoveryDiscoveryStatus.SLICING = RUMRecoveryDiscoveryStatus("SLICING")
RUMRecoveryDiscoveryStatus.DISCOVERED = RUMRecoveryDiscoveryStatus("DISCOVERED")
RUMRecoveryDiscoveryStatus.PROCESSING = RUMRecoveryDiscoveryStatus("PROCESSING")
RUMRecoveryDiscoveryStatus.COMPLETED = RUMRecoveryDiscoveryStatus("COMPLETED")
RUMRecoveryDiscoveryStatus.FAILED = RUMRecoveryDiscoveryStatus("FAILED")
RUMRecoveryDiscoveryStatus.CANCELLED = RUMRecoveryDiscoveryStatus("CANCELLED")
