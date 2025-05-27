# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.send_teams_message_action_type import SendTeamsMessageActionType


class SendTeamsMessageAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.send_teams_message_action_type import SendTeamsMessageActionType

        return {
            "channel": (str,),
            "team": (str,),
            "tenant": (str,),
            "type": (SendTeamsMessageActionType,),
        }

    attribute_map = {
        "channel": "channel",
        "team": "team",
        "tenant": "tenant",
        "type": "type",
    }

    def __init__(self_, channel: str, team: str, tenant: str, type: SendTeamsMessageActionType, **kwargs):
        """
        Sends a message to a Microsoft Teams channel.

        :param channel: The channel ID.
        :type channel: str

        :param team: The team ID.
        :type team: str

        :param tenant: The tenant ID.
        :type tenant: str

        :param type: Indicates that the action is a send Microsoft Teams message action.
        :type type: SendTeamsMessageActionType
        """
        super().__init__(kwargs)

        self_.channel = channel
        self_.team = team
        self_.tenant = tenant
        self_.type = type
