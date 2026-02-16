# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CustomAgentConversationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "conversation_id": (str,),
            "output_schema": (dict,),
            "user_prompt": (str,),
        }

    attribute_map = {
        "conversation_id": "conversationId",
        "output_schema": "outputSchema",
        "user_prompt": "userPrompt",
    }

    def __init__(
        self_,
        user_prompt: str,
        conversation_id: Union[str, UnsetType] = unset,
        output_schema: Union[dict, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param conversation_id: The conversation ID to continue an existing conversation.
        :type conversation_id: str, optional

        :param output_schema: Optional JSON schema to structure the output.
        :type output_schema: dict, optional

        :param user_prompt: The user's prompt for the conversation.
        :type user_prompt: str
        """
        if conversation_id is not unset:
            kwargs["conversation_id"] = conversation_id
        if output_schema is not unset:
            kwargs["output_schema"] = output_schema
        super().__init__(kwargs)

        self_.user_prompt = user_prompt
