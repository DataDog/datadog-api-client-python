# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRecoveryDiscoveryStatus(ModelSimple):
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
    QUEUED: ClassVar["RumRecoveryDiscoveryStatus"]
    PENDING: ClassVar["RumRecoveryDiscoveryStatus"]
    SLICING: ClassVar["RumRecoveryDiscoveryStatus"]
    DISCOVERED: ClassVar["RumRecoveryDiscoveryStatus"]
    PROCESSING: ClassVar["RumRecoveryDiscoveryStatus"]
    COMPLETED: ClassVar["RumRecoveryDiscoveryStatus"]
    FAILED: ClassVar["RumRecoveryDiscoveryStatus"]
    CANCELLED: ClassVar["RumRecoveryDiscoveryStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRecoveryDiscoveryStatus.QUEUED = RumRecoveryDiscoveryStatus("QUEUED")
RumRecoveryDiscoveryStatus.PENDING = RumRecoveryDiscoveryStatus("PENDING")
RumRecoveryDiscoveryStatus.SLICING = RumRecoveryDiscoveryStatus("SLICING")
RumRecoveryDiscoveryStatus.DISCOVERED = RumRecoveryDiscoveryStatus("DISCOVERED")
RumRecoveryDiscoveryStatus.PROCESSING = RumRecoveryDiscoveryStatus("PROCESSING")
RumRecoveryDiscoveryStatus.COMPLETED = RumRecoveryDiscoveryStatus("COMPLETED")
RumRecoveryDiscoveryStatus.FAILED = RumRecoveryDiscoveryStatus("FAILED")
RumRecoveryDiscoveryStatus.CANCELLED = RumRecoveryDiscoveryStatus("CANCELLED")
