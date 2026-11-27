# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.send_slack_message_action_customizable_content import (
        SendSlackMessageActionCustomizableContent,
    )
    from datadog_api_client.v2.model.send_slack_message_action_type import SendSlackMessageActionType


class SendSlackMessageAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.send_slack_message_action_customizable_content import (
            SendSlackMessageActionCustomizableContent,
        )
        from datadog_api_client.v2.model.send_slack_message_action_type import SendSlackMessageActionType

        return {
            "channel": (str,),
            "customizable_content": (SendSlackMessageActionCustomizableContent,),
            "type": (SendSlackMessageActionType,),
            "workspace": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "customizable_content": "customizable_content",
        "type": "type",
        "workspace": "workspace",
    }

    def __init__(
        self_,
        channel: str,
        type: SendSlackMessageActionType,
        workspace: str,
        customizable_content: Union[SendSlackMessageActionCustomizableContent, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sends a message to a Slack channel.

        :param channel: The channel ID.
        :type channel: str

        :param customizable_content: Options that customize the content of the Slack message sent for a Page.
        :type customizable_content: SendSlackMessageActionCustomizableContent, optional

        :param type: Indicates that the action is a send Slack message action.
        :type type: SendSlackMessageActionType

        :param workspace: The workspace ID.
        :type workspace: str
        """
        if customizable_content is not unset:
            kwargs["customizable_content"] = customizable_content
        super().__init__(kwargs)

        self_.channel = channel
        self_.type = type
        self_.workspace = workspace
