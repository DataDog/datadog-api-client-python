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
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content_value import (
        LLMObsCustomEvalConfigPromptContentValue,
    )


class LLMObsCustomEvalConfigPromptContent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_content_value import (
            LLMObsCustomEvalConfigPromptContentValue,
        )

        return {
            "type": (str,),
            "value": (LLMObsCustomEvalConfigPromptContentValue,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: str, value: LLMObsCustomEvalConfigPromptContentValue, **kwargs):
        """
        A content block within a prompt message.

        :param type: Content block type.
        :type type: str

        :param value: Value of a prompt message content block.
        :type value: LLMObsCustomEvalConfigPromptContentValue
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
