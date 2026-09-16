# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeRunAsPrincipalType(ModelSimple):
    """
    The type of principal allowed to act on behalf of the downtime.

    :param value: Must be one of ["user", "role", "team"].
    :type value: str
    """

    allowed_values = {
        "user",
        "role",
        "team",
    }
    USER: ClassVar["DowntimeRunAsPrincipalType"]
    ROLE: ClassVar["DowntimeRunAsPrincipalType"]
    TEAM: ClassVar["DowntimeRunAsPrincipalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeRunAsPrincipalType.USER = DowntimeRunAsPrincipalType("user")
DowntimeRunAsPrincipalType.ROLE = DowntimeRunAsPrincipalType("role")
DowntimeRunAsPrincipalType.TEAM = DowntimeRunAsPrincipalType("team")
