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
    from datadog_api_client.v2.model.llm_obs_prompt_include import LLMObsPromptInclude


class LLMObsPromptIncludeItem(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_include import LLMObsPromptInclude

        return {
            "include": (LLMObsPromptInclude,),
        }

    attribute_map = {
        "include": "include",
    }

    def __init__(self_, include: LLMObsPromptInclude, **kwargs):
        """
        An explicitly versioned whole-chat or selective-message include.

        :param include: An explicitly versioned prompt included as chat items. Omitting ``items`` includes every child message in its original order. When ``items`` is present, its zero-based indexes are inserted in the order provided; duplicate indexes are preserved.
        :type include: LLMObsPromptInclude
        """
        super().__init__(kwargs)

        self_.include = include
