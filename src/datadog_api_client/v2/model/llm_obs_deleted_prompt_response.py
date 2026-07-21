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
    from datadog_api_client.v2.model.llm_obs_deleted_prompt_data import LLMObsDeletedPromptData


class LLMObsDeletedPromptResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_deleted_prompt_data import LLMObsDeletedPromptData

        return {
            "data": (LLMObsDeletedPromptData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDeletedPromptData, **kwargs):
        """
        Response confirming that an LLM Observability prompt was deleted.

        :param data: Data object confirming that an LLM Observability prompt was deleted.
        :type data: LLMObsDeletedPromptData
        """
        super().__init__(kwargs)

        self_.data = data
