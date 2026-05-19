# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LLMObsAnnotatedInteractionItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        An interaction with its associated annotations.

        :param annotations: List of annotations for this interaction.
        :type annotations: [LLMObsAnnotationItem]

        :param content_id: Upstream entity identifier supplied by the caller.
        :type content_id: str

        :param created_at: Timestamp when the interaction was added to the queue.
        :type created_at: datetime

        :param id: Unique identifier of the interaction.
        :type id: str

        :param modified_at: Timestamp when the interaction was last updated.
        :type modified_at: datetime

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
        from datadog_api_client.v2.model.llm_obs_trace_annotated_interaction_item import (
            LLMObsTraceAnnotatedInteractionItem,
        )
        from datadog_api_client.v2.model.llm_obs_display_block_annotated_interaction_item import (
            LLMObsDisplayBlockAnnotatedInteractionItem,
        )

        return {
            "oneOf": [
                LLMObsTraceAnnotatedInteractionItem,
                LLMObsDisplayBlockAnnotatedInteractionItem,
            ],
        }
