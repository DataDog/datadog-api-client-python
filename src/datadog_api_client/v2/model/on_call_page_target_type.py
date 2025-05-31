# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageTargetType(ModelSimple):
    """
    The kind of target, `team_id` | `team_handle` | `user_id`.

    :param value: Must be one of ["team_id", "team_handle", "user_id"].
    :type value: str
    """

    allowed_values = {
        "team_id",
        "team_handle",
        "user_id",
    }
    TEAM_ID: ClassVar["OnCallPageTargetType"]
    TEAM_HANDLE: ClassVar["OnCallPageTargetType"]
    USER_ID: ClassVar["OnCallPageTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageTargetType.TEAM_ID = OnCallPageTargetType("team_id")
OnCallPageTargetType.TEAM_HANDLE = OnCallPageTargetType("team_handle")
OnCallPageTargetType.USER_ID = OnCallPageTargetType("user_id")
