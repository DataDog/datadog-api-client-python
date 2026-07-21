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
    from datadog_api_client.v2.model.llm_obs_prompt_sdk_data_attributes import LLMObsPromptSDKDataAttributes
    from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType


class LLMObsPromptSDKData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_sdk_data_attributes import LLMObsPromptSDKDataAttributes
        from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType

        return {
            "attributes": (LLMObsPromptSDKDataAttributes,),
            "id": (str,),
            "type": (LLMObsPromptType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsPromptSDKDataAttributes, id: str, type: LLMObsPromptType, **kwargs):
        """
        Data object for a flattened LLM Observability prompt version returned for SDK consumption.

        :param attributes: Attributes of a flattened prompt version returned for SDK consumption. Exactly one of ``template`` and ``chat_template`` is returned.
        :type attributes: LLMObsPromptSDKDataAttributes

        :param id: Unique identifier of the prompt.
        :type id: str

        :param type: Resource type of an LLM Observability prompt.
        :type type: LLMObsPromptType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
