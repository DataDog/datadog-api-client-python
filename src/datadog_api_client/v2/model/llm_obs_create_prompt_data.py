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
    from datadog_api_client.v2.model.llm_obs_create_prompt_data_attributes import LLMObsCreatePromptDataAttributes
    from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType


class LLMObsCreatePromptData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_create_prompt_data_attributes import LLMObsCreatePromptDataAttributes
        from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType

        return {
            "attributes": (LLMObsCreatePromptDataAttributes,),
            "type": (LLMObsPromptType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsCreatePromptDataAttributes, type: LLMObsPromptType, **kwargs):
        """
        Data object for creating an LLM Observability prompt.

        :param attributes: Attributes for creating an LLM Observability prompt and its first version. ``prompt_id`` and ``template`` are required; all other attributes are optional.
        :type attributes: LLMObsCreatePromptDataAttributes

        :param type: Resource type of an LLM Observability prompt.
        :type type: LLMObsPromptType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
