# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimestampType(ModelSimple):
    """
    The type of timestamp being overridden.

    :param value: Must be one of ["created", "detected", "resolved", "declared"].
    :type value: str
    """

    allowed_values = {
        "created",
        "detected",
        "resolved",
        "declared",
    }
    CREATED: ClassVar["TimestampType"]
    DETECTED: ClassVar["TimestampType"]
    RESOLVED: ClassVar["TimestampType"]
    DECLARED: ClassVar["TimestampType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimestampType.CREATED = TimestampType("created")
TimestampType.DETECTED = TimestampType("detected")
TimestampType.RESOLVED = TimestampType("resolved")
TimestampType.DECLARED = TimestampType("declared")
