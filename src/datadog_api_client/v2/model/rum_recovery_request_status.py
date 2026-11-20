# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMRecoveryRequestStatus(ModelSimple):
    """
    Recovery request state.

    :param value: Must be one of ["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "EXPIRED"].
    :type value: str
    """

    allowed_values = {
        "PENDING",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "EXPIRED",
    }
    PENDING: ClassVar["RUMRecoveryRequestStatus"]
    PROCESSING: ClassVar["RUMRecoveryRequestStatus"]
    COMPLETED: ClassVar["RUMRecoveryRequestStatus"]
    FAILED: ClassVar["RUMRecoveryRequestStatus"]
    CANCELLED: ClassVar["RUMRecoveryRequestStatus"]
    EXPIRED: ClassVar["RUMRecoveryRequestStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMRecoveryRequestStatus.PENDING = RUMRecoveryRequestStatus("PENDING")
RUMRecoveryRequestStatus.PROCESSING = RUMRecoveryRequestStatus("PROCESSING")
RUMRecoveryRequestStatus.COMPLETED = RUMRecoveryRequestStatus("COMPLETED")
RUMRecoveryRequestStatus.FAILED = RUMRecoveryRequestStatus("FAILED")
RUMRecoveryRequestStatus.CANCELLED = RUMRecoveryRequestStatus("CANCELLED")
RUMRecoveryRequestStatus.EXPIRED = RUMRecoveryRequestStatus("EXPIRED")
