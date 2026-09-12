# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_prompt_authoring_item import LLMObsPromptAuthoringItem
    from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage
    from datadog_api_client.v2.model.llm_obs_prompt_include_item import LLMObsPromptIncludeItem


class LLMObsPromptAuthoringMessagesTemplate(ModelNormal):
    validations = {
        "messages": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_authoring_item import LLMObsPromptAuthoringItem

        return {
            "messages": ([LLMObsPromptAuthoringItem],),
        }

    attribute_map = {
        "messages": "messages",
    }

    def __init__(
        self_,
        messages: List[Union[LLMObsPromptAuthoringItem, LLMObsPromptChatMessage, LLMObsPromptIncludeItem]],
        **kwargs,
    ):
        """
        A chat prompt whose authored items are stored under ``messages``.

        :param messages: A chat prompt containing messages, pinned includes, or both.
        :type messages: [LLMObsPromptAuthoringItem]
        """
        super().__init__(kwargs)

        self_.messages = messages
