# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content import (
        LLMObsCustomEvalConfigPromptContent,
    )


class LLMObsCustomEvalConfigPromptMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content import (
            LLMObsCustomEvalConfigPromptContent,
        )

        return {
            "content": (str,),
            "contents": ([LLMObsCustomEvalConfigPromptContent],),
            "role": (str,),
        }

    attribute_map = {
        "content": "content",
        "contents": "contents",
        "role": "role",
    }

    def __init__(
        self_,
        role: str,
        content: Union[str, UnsetType] = unset,
        contents: Union[List[LLMObsCustomEvalConfigPromptContent], UnsetType] = unset,
        **kwargs,
    ):
        """
        A message in the prompt template for a custom LLM judge evaluator.

        :param content: Text content of the message.
        :type content: str, optional

        :param contents: Multi-part content blocks for the message.
        :type contents: [LLMObsCustomEvalConfigPromptContent], optional

        :param role: Role of the message author.
        :type role: str
        """
        if content is not unset:
            kwargs["content"] = content
        if contents is not unset:
            kwargs["contents"] = contents
        super().__init__(kwargs)

        self_.role = role
