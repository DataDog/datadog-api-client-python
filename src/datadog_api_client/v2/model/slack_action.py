# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SlackAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "channel": (str,),
            "type": (str,),
            "workspace": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "type": "type",
        "workspace": "workspace",
    }

    def __init__(self_, channel: str, type: str, workspace: str, **kwargs):
        """
        Sends a message to a Slack channel.

        :param channel: The channel ID.
        :type channel: str

        :param type: Must be set to "send_slack_message".
        :type type: str

        :param workspace: The workspace ID.
        :type workspace: str
        """
        super().__init__(kwargs)

        self_.channel = channel
        self_.type = type
        self_.workspace = workspace
