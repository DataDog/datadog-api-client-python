# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeRequestRiskLevel(ModelSimple):
    """
    The risk level of the change request.

    :param value: Must be one of ["UNDEFINED", "LOW", "MEDIUM", "HIGH"].
    :type value: str
    """

    allowed_values = {
        "UNDEFINED",
        "LOW",
        "MEDIUM",
        "HIGH",
    }
    UNDEFINED: ClassVar["ChangeRequestRiskLevel"]
    LOW: ClassVar["ChangeRequestRiskLevel"]
    MEDIUM: ClassVar["ChangeRequestRiskLevel"]
    HIGH: ClassVar["ChangeRequestRiskLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeRequestRiskLevel.UNDEFINED = ChangeRequestRiskLevel("UNDEFINED")
ChangeRequestRiskLevel.LOW = ChangeRequestRiskLevel("LOW")
ChangeRequestRiskLevel.MEDIUM = ChangeRequestRiskLevel("MEDIUM")
ChangeRequestRiskLevel.HIGH = ChangeRequestRiskLevel("HIGH")
