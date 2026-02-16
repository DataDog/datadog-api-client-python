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
    from datadog_api_client.v2.model.chat_history_item_role import ChatHistoryItemRole


class ChatHistoryItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_history_item_role import ChatHistoryItemRole

        return {
            "content": (str,),
            "role": (ChatHistoryItemRole,),
        }

    attribute_map = {
        "content": "content",
        "role": "role",
    }

    def __init__(self_, content: str, role: ChatHistoryItemRole, **kwargs):
        """


        :param content: The message content.
        :type content: str

        :param role: The role of the message sender.
        :type role: ChatHistoryItemRole
        """
        super().__init__(kwargs)

        self_.content = content
        self_.role = role
