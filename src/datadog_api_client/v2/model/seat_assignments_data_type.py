# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeatAssignmentsDataType(ModelSimple):
    """
    Seat assignments resource type.

    :param value: If omitted defaults to "seat-assignments". Must be one of ["seat-assignments"].
    :type value: str
    """

    allowed_values = {
        "seat-assignments",
    }
    SEAT_ASSIGNMENTS: ClassVar["SeatAssignmentsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeatAssignmentsDataType.SEAT_ASSIGNMENTS = SeatAssignmentsDataType("seat-assignments")
