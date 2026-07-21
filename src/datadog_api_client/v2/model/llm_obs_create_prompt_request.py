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
    from datadog_api_client.v2.model.llm_obs_create_prompt_data import LLMObsCreatePromptData


class LLMObsCreatePromptRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_create_prompt_data import LLMObsCreatePromptData

        return {
            "data": (LLMObsCreatePromptData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsCreatePromptData, **kwargs):
        """
        Request to create an LLM Observability prompt.

        :param data: Data object for creating an LLM Observability prompt.
        :type data: LLMObsCreatePromptData
        """
        super().__init__(kwargs)

        self_.data = data
