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
    from datadog_api_client.v2.model.llm_obs_annotation_item import LLMObsAnnotationItem
    from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
    from datadog_api_client.v2.model.llm_obs_display_block_interaction_type import LLMObsDisplayBlockInteractionType


class LLMObsDisplayBlockAnnotatedInteractionItem(ModelNormal):
    validations = {
        "display_block": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_item import LLMObsAnnotationItem
        from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
        from datadog_api_client.v2.model.llm_obs_display_block_interaction_type import LLMObsDisplayBlockInteractionType

        return {
            "annotations": ([LLMObsAnnotationItem],),
            "content_id": (str,),
            "display_block": ([LLMObsContentBlock],),
            "id": (str,),
            "type": (LLMObsDisplayBlockInteractionType,),
        }

    attribute_map = {
        "annotations": "annotations",
        "content_id": "content_id",
        "display_block": "display_block",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        annotations: List[LLMObsAnnotationItem],
        content_id: str,
        display_block: List[LLMObsContentBlock],
        id: str,
        type: LLMObsDisplayBlockInteractionType,
        **kwargs,
    ):
        """
        A display_block interaction with its associated annotations.

        :param annotations: List of annotations for this interaction.
        :type annotations: [LLMObsAnnotationItem]

        :param content_id: Server-generated deterministic identifier derived from the block list.
        :type content_id: str

        :param display_block: List of content blocks that make up a ``display_block`` interaction.
            Must contain at least one block.
        :type display_block: [LLMObsContentBlock]

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type discriminator for a ``display_block`` interaction.
        :type type: LLMObsDisplayBlockInteractionType
        """
        super().__init__(kwargs)

        self_.annotations = annotations
        self_.content_id = content_id
        self_.display_block = display_block
        self_.id = id
        self_.type = type
