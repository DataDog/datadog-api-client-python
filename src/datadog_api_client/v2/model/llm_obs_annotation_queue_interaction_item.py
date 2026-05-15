# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LLMObsAnnotationQueueInteractionItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A single interaction to add to an annotation queue.

        :param content_id: Upstream entity identifier (trace, experiment trace, or session ID).
        :type content_id: str

        :param type: Type of an upstream-entity interaction.
        :type type: LLMObsTraceInteractionType

        :param display_block: List of content blocks that make up a `display_block` interaction.
            Must contain at least one block.
        :type display_block: [LLMObsContentBlock]
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.llm_obs_trace_interaction_item import LLMObsTraceInteractionItem
        from datadog_api_client.v2.model.llm_obs_display_block_interaction_item import LLMObsDisplayBlockInteractionItem

        return {
            "oneOf": [
                LLMObsTraceInteractionItem,
                LLMObsDisplayBlockInteractionItem,
            ],
        }
