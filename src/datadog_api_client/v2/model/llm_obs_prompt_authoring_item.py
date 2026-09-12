# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LLMObsPromptAuthoringItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A chat message or an explicitly versioned prompt include.

        :param content: Content of the message.
        :type content: str

        :param role: Role of the message (for example `system`, `user`, or `assistant`).
        :type role: str

        :param include: An explicitly versioned prompt included as chat items. Omitting `items` includes every child message in its original order. When `items` is present, its zero-based indexes are inserted in the order provided; duplicate indexes are preserved.
        :type include: LLMObsPromptInclude
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage
        from datadog_api_client.v2.model.llm_obs_prompt_include_item import LLMObsPromptIncludeItem

        return {
            "oneOf": [
                LLMObsPromptChatMessage,
                LLMObsPromptIncludeItem,
            ],
        }
