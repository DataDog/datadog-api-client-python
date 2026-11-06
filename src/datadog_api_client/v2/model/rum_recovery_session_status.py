# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRecoverySessionStatus(ModelSimple):
    """
    Session availability or recovery state. `RECOVERED` indicates that the session is ready to query.

    :param value: Must be one of ["AVAILABLE", "PENDING", "PROCESSING", "RECOVERED", "FAILED", "RETAINED", "EXPIRED", "CANCELLED"].
    :type value: str
    """

    allowed_values = {
        "AVAILABLE",
        "PENDING",
        "PROCESSING",
        "RECOVERED",
        "FAILED",
        "RETAINED",
        "EXPIRED",
        "CANCELLED",
    }
    AVAILABLE: ClassVar["RumRecoverySessionStatus"]
    PENDING: ClassVar["RumRecoverySessionStatus"]
    PROCESSING: ClassVar["RumRecoverySessionStatus"]
    RECOVERED: ClassVar["RumRecoverySessionStatus"]
    FAILED: ClassVar["RumRecoverySessionStatus"]
    RETAINED: ClassVar["RumRecoverySessionStatus"]
    EXPIRED: ClassVar["RumRecoverySessionStatus"]
    CANCELLED: ClassVar["RumRecoverySessionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRecoverySessionStatus.AVAILABLE = RumRecoverySessionStatus("AVAILABLE")
RumRecoverySessionStatus.PENDING = RumRecoverySessionStatus("PENDING")
RumRecoverySessionStatus.PROCESSING = RumRecoverySessionStatus("PROCESSING")
RumRecoverySessionStatus.RECOVERED = RumRecoverySessionStatus("RECOVERED")
RumRecoverySessionStatus.FAILED = RumRecoverySessionStatus("FAILED")
RumRecoverySessionStatus.RETAINED = RumRecoverySessionStatus("RETAINED")
RumRecoverySessionStatus.EXPIRED = RumRecoverySessionStatus("EXPIRED")
RumRecoverySessionStatus.CANCELLED = RumRecoverySessionStatus("CANCELLED")
