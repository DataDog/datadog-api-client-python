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
    from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
    from datadog_api_client.v2.model.llm_obs_display_block_interaction_type import LLMObsDisplayBlockInteractionType


class LLMObsDisplayBlockInteractionItem(ModelNormal):
    validations = {
        "display_block": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
        from datadog_api_client.v2.model.llm_obs_display_block_interaction_type import LLMObsDisplayBlockInteractionType

        return {
            "display_block": ([LLMObsContentBlock],),
            "type": (LLMObsDisplayBlockInteractionType,),
        }

    attribute_map = {
        "display_block": "display_block",
        "type": "type",
    }

    def __init__(self_, display_block: List[LLMObsContentBlock], type: LLMObsDisplayBlockInteractionType, **kwargs):
        """
        An interaction whose rendered content is supplied directly as a list
        of display blocks. The server generates ``content_id`` deterministically
        from the block list.

        :param display_block: List of content blocks that make up a ``display_block`` interaction.
            Must contain at least one block.
        :type display_block: [LLMObsContentBlock]

        :param type: Type discriminator for a ``display_block`` interaction.
        :type type: LLMObsDisplayBlockInteractionType
        """
        super().__init__(kwargs)

        self_.display_block = display_block
        self_.type = type
