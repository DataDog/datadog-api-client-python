# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_prompt_version_list_data import LLMObsPromptVersionListData


class LLMObsPromptVersionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_version_list_data import LLMObsPromptVersionListData

        return {
            "data": ([LLMObsPromptVersionListData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[LLMObsPromptVersionListData], **kwargs):
        """
        Response containing the versions of an LLM Observability prompt.

        :param data: Prompt versions ordered from newest to oldest.
        :type data: [LLMObsPromptVersionListData]
        """
        super().__init__(kwargs)

        self_.data = data
