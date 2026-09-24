# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LLMObsPromptTemplate(ModelComposed):
    def __init__(self, **kwargs):
        """
        A text template, a list of chat messages, or an authored chat object. Text can include an exact prompt version with ``{{>prompt-id version=N}}`` ; other text, including ``{{>...}}`` sequences without a version, remains literal. Use an authored chat object when including prompts as chat messages.
        **Preview** : Prompt composition is available in Preview. To request access, contact `Datadog Support <https://docs.datadoghq.com/help/>`_ or your Customer Success Manager.
        Without access, inline references remain literal text and structured includes are unsupported. Previously compiled prompt versions remain available for execution.

        :param messages: A chat prompt containing messages, references to specific versions of other prompts, or both.
        :type messages: [LLMObsPromptAuthoringItem]
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
        from datadog_api_client.v2.model.llm_obs_prompt_authoring_messages_template import (
            LLMObsPromptAuthoringMessagesTemplate,
        )

        return {
            "oneOf": [
                str,
                [LLMObsPromptChatMessage],
                LLMObsPromptAuthoringMessagesTemplate,
            ],
        }
