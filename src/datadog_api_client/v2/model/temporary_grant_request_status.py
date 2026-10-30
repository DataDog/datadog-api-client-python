# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TemporaryGrantRequestStatus(ModelSimple):
    """
    The durable request decision, independent of whether its grant is still active.

    :param value: Must be one of ["pending", "approved", "denied", "cancelled"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "approved",
        "denied",
        "cancelled",
    }
    PENDING: ClassVar["TemporaryGrantRequestStatus"]
    APPROVED: ClassVar["TemporaryGrantRequestStatus"]
    DENIED: ClassVar["TemporaryGrantRequestStatus"]
    CANCELLED: ClassVar["TemporaryGrantRequestStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TemporaryGrantRequestStatus.PENDING = TemporaryGrantRequestStatus("pending")
TemporaryGrantRequestStatus.APPROVED = TemporaryGrantRequestStatus("approved")
TemporaryGrantRequestStatus.DENIED = TemporaryGrantRequestStatus("denied")
TemporaryGrantRequestStatus.CANCELLED = TemporaryGrantRequestStatus("cancelled")
