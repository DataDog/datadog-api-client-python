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
    from datadog_api_client.v2.model.llm_obs_prompt_data import LLMObsPromptData


class LLMObsPromptResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_data import LLMObsPromptData

        return {
            "data": (LLMObsPromptData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsPromptData, **kwargs):
        """
        Response containing a single LLM Observability prompt.

        :param data: Data object for an LLM Observability prompt.
        :type data: LLMObsPromptData
        """
        super().__init__(kwargs)

        self_.data = data
