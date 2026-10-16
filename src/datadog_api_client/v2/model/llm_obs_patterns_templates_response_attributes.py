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
    from datadog_api_client.v2.model.llm_obs_patterns_template_item import LLMObsPatternsTemplateItem


class LLMObsPatternsTemplatesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_template_item import LLMObsPatternsTemplateItem

        return {
            "templates": ([LLMObsPatternsTemplateItem],),
        }

    attribute_map = {
        "templates": "templates",
    }

    def __init__(self_, templates: List[LLMObsPatternsTemplateItem], **kwargs):
        """
        Attributes of a list of Agent Observability patterns templates.

        :param templates: List of patterns templates.
        :type templates: [LLMObsPatternsTemplateItem]
        """
        super().__init__(kwargs)

        self_.templates = templates
