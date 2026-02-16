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
    from datadog_api_client.v2.model.chat_message_role import ChatMessageRole


class ChatMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_message_role import ChatMessageRole

        return {
            "chat_id": (str,),
            "content": (str,),
            "id": (str,),
            "role": (ChatMessageRole,),
            "user_uuid": (str,),
        }

    attribute_map = {
        "chat_id": "chatId",
        "content": "content",
        "id": "id",
        "role": "role",
        "user_uuid": "userUuid",
    }

    def __init__(
        self_,
        chat_id: str,
        content: str,
        id: str,
        role: ChatMessageRole,
        user_uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param chat_id: The chat ID.
        :type chat_id: str

        :param content: The message content.
        :type content: str

        :param id: The message ID.
        :type id: str

        :param role: The role of the message sender.
        :type role: ChatMessageRole

        :param user_uuid: The UUID of the user who sent the message.
        :type user_uuid: str, optional
        """
        if user_uuid is not unset:
            kwargs["user_uuid"] = user_uuid
        super().__init__(kwargs)

        self_.chat_id = chat_id
        self_.content = content
        self_.id = id
        self_.role = role
