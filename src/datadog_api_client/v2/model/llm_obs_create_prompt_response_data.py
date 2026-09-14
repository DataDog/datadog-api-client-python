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
    from datadog_api_client.v2.model.llm_obs_create_prompt_response_data_attributes import (
        LLMObsCreatePromptResponseDataAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType


class LLMObsCreatePromptResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_create_prompt_response_data_attributes import (
            LLMObsCreatePromptResponseDataAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType

        return {
            "attributes": (LLMObsCreatePromptResponseDataAttributes,),
            "id": (str,),
            "type": (LLMObsPromptType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsCreatePromptResponseDataAttributes, id: str, type: LLMObsPromptType, **kwargs
    ):
        """
        Data object returned after creating an Agent Observability prompt.

        :param attributes: Attributes returned after creating an Agent Observability prompt and its first version.
        :type attributes: LLMObsCreatePromptResponseDataAttributes

        :param id: Unique identifier of the prompt.
        :type id: str

        :param type: Resource type of an Agent Observability prompt.
        :type type: LLMObsPromptType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
