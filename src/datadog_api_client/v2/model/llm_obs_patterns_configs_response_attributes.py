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
    from datadog_api_client.v2.model.llm_obs_patterns_config_item import LLMObsPatternsConfigItem


class LLMObsPatternsConfigsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_config_item import LLMObsPatternsConfigItem

        return {
            "configs": ([LLMObsPatternsConfigItem],),
        }

    attribute_map = {
        "configs": "configs",
    }

    def __init__(self_, configs: List[LLMObsPatternsConfigItem], **kwargs):
        """
        Attributes of a list of LLM Observability patterns configurations.

        :param configs: List of patterns configurations.
        :type configs: [LLMObsPatternsConfigItem]
        """
        super().__init__(kwargs)

        self_.configs = configs
