# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeatUserDataType(ModelSimple):
    """
    Seat users resource type.

    :param value: If omitted defaults to "seat-users". Must be one of ["seat-users"].
    :type value: str
    """

    allowed_values = {
        "seat-users",
    }
    SEAT_USERS: ClassVar["SeatUserDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeatUserDataType.SEAT_USERS = SeatUserDataType("seat-users")
