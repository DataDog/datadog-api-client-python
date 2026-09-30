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
    from datadog_api_client.v2.model.llm_obs_prompt_message_placeholder_type import LLMObsPromptMessagePlaceholderType


class LLMObsPromptMessagePlaceholder(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_message_placeholder_type import (
            LLMObsPromptMessagePlaceholderType,
        )

        return {
            "name": (str,),
            "type": (LLMObsPromptMessagePlaceholderType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: LLMObsPromptMessagePlaceholderType, **kwargs):
        """
        A named placeholder that inserts a list of messages when a compatible SDK formats the prompt.
        **Preview:** Message placeholders are available in Preview. To request access, contact `Datadog Support <https://www.datadoghq.com/support/>`_ or your Customer Success Manager.

        :param name: Name used to supply the message list when formatting the prompt.
        :type name: str

        :param type: Type of chat-template item.
        :type type: LLMObsPromptMessagePlaceholderType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
