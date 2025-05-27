# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SendTeamsMessageActionType(ModelSimple):
    """
    Indicates that the action is a send Microsoft Teams message action.

    :param value: If omitted defaults to "send_teams_message". Must be one of ["send_teams_message"].
    :type value: str
    """

    allowed_values = {
        "send_teams_message",
    }
    SEND_TEAMS_MESSAGE: ClassVar["SendTeamsMessageActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SendTeamsMessageActionType.SEND_TEAMS_MESSAGE = SendTeamsMessageActionType("send_teams_message")
