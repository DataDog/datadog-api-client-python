# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipConfidenceLevel(ModelSimple):
    """
    The ownership confidence level.

    :param value: Must be one of ["high", "medium", "low"].
    :type value: str
    """

    allowed_values = {
        "high",
        "medium",
        "low",
    }
    HIGH: ClassVar["OwnershipConfidenceLevel"]
    MEDIUM: ClassVar["OwnershipConfidenceLevel"]
    LOW: ClassVar["OwnershipConfidenceLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipConfidenceLevel.HIGH = OwnershipConfidenceLevel("high")
OwnershipConfidenceLevel.MEDIUM = OwnershipConfidenceLevel("medium")
OwnershipConfidenceLevel.LOW = OwnershipConfidenceLevel("low")
