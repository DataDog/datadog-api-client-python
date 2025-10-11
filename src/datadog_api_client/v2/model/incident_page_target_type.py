# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentPageTargetType(ModelSimple):
    """
    Type of page target for incident pages.

    :param value: Must be one of ["team_handle", "team_uuid", "user_uuid"].
    :type value: str
    """

    allowed_values = {
        "team_handle",
        "team_uuid",
        "user_uuid",
    }
    TEAM_HANDLE: ClassVar["IncidentPageTargetType"]
    TEAM_UUID: ClassVar["IncidentPageTargetType"]
    USER_UUID: ClassVar["IncidentPageTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentPageTargetType.TEAM_HANDLE = IncidentPageTargetType("team_handle")
IncidentPageTargetType.TEAM_UUID = IncidentPageTargetType("team_uuid")
IncidentPageTargetType.USER_UUID = IncidentPageTargetType("user_uuid")
