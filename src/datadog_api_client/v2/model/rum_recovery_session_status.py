# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMRecoverySessionStatus(ModelSimple):
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
    AVAILABLE: ClassVar["RUMRecoverySessionStatus"]
    PENDING: ClassVar["RUMRecoverySessionStatus"]
    PROCESSING: ClassVar["RUMRecoverySessionStatus"]
    RECOVERED: ClassVar["RUMRecoverySessionStatus"]
    FAILED: ClassVar["RUMRecoverySessionStatus"]
    RETAINED: ClassVar["RUMRecoverySessionStatus"]
    EXPIRED: ClassVar["RUMRecoverySessionStatus"]
    CANCELLED: ClassVar["RUMRecoverySessionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMRecoverySessionStatus.AVAILABLE = RUMRecoverySessionStatus("AVAILABLE")
RUMRecoverySessionStatus.PENDING = RUMRecoverySessionStatus("PENDING")
RUMRecoverySessionStatus.PROCESSING = RUMRecoverySessionStatus("PROCESSING")
RUMRecoverySessionStatus.RECOVERED = RUMRecoverySessionStatus("RECOVERED")
RUMRecoverySessionStatus.FAILED = RUMRecoverySessionStatus("FAILED")
RUMRecoverySessionStatus.RETAINED = RUMRecoverySessionStatus("RETAINED")
RUMRecoverySessionStatus.EXPIRED = RUMRecoverySessionStatus("EXPIRED")
RUMRecoverySessionStatus.CANCELLED = RUMRecoverySessionStatus("CANCELLED")
