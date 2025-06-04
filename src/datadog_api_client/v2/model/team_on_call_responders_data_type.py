# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamOnCallRespondersDataType(ModelSimple):
    """
    Represents the resource type for a group of users assigned to handle on-call duties within a team.

    :param value: If omitted defaults to "team_oncall_responders". Must be one of ["team_oncall_responders"].
    :type value: str
    """

    allowed_values = {
        "team_oncall_responders",
    }
    TEAM_ONCALL_RESPONDERS: ClassVar["TeamOnCallRespondersDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamOnCallRespondersDataType.TEAM_ONCALL_RESPONDERS = TeamOnCallRespondersDataType("team_oncall_responders")
