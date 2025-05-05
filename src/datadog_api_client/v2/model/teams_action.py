# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TeamsAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "channel": (str,),
            "team": (str,),
            "tenant": (str,),
            "type": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "team": "team",
        "tenant": "tenant",
        "type": "type",
    }

    def __init__(self_, channel: str, team: str, tenant: str, type: str, **kwargs):
        """
        Sends a message to a Microsoft Teams channel.

        :param channel: The channel ID.
        :type channel: str

        :param team: The team ID.
        :type team: str

        :param tenant: The tenant ID.
        :type tenant: str

        :param type: Must be set to "send_teams_message".
        :type type: str
        """
        super().__init__(kwargs)

        self_.channel = channel
        self_.team = team
        self_.tenant = tenant
        self_.type = type
