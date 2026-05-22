# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_item import LLMObsAnnotationItem
    from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
    from datadog_api_client.v2.model.llm_obs_any_interaction_type import LLMObsAnyInteractionType


class LLMObsAnnotatedInteractionByTraceItem(ModelNormal):
    validations = {
        "display_block": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_item import LLMObsAnnotationItem
        from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
        from datadog_api_client.v2.model.llm_obs_any_interaction_type import LLMObsAnyInteractionType

        return {
            "annotations": ([LLMObsAnnotationItem],),
            "content_id": (str,),
            "created_at": (datetime,),
            "display_block": ([LLMObsContentBlock],),
            "id": (str,),
            "modified_at": (datetime,),
            "queue_id": (str,),
            "queue_name": (str,),
            "type": (LLMObsAnyInteractionType,),
        }

    attribute_map = {
        "annotations": "annotations",
        "content_id": "content_id",
        "created_at": "created_at",
        "display_block": "display_block",
        "id": "id",
        "modified_at": "modified_at",
        "queue_id": "queue_id",
        "queue_name": "queue_name",
        "type": "type",
    }

    def __init__(
        self_,
        annotations: List[LLMObsAnnotationItem],
        content_id: str,
        created_at: datetime,
        id: str,
        modified_at: datetime,
        queue_id: str,
        queue_name: str,
        type: LLMObsAnyInteractionType,
        display_block: Union[List[LLMObsContentBlock], UnsetType] = unset,
        **kwargs,
    ):
        """
        An annotated interaction returned by the cross-queue lookup, including the source queue metadata.

        :param annotations: List of annotations for this interaction.
        :type annotations: [LLMObsAnnotationItem]

        :param content_id: Upstream entity identifier (trace ID, session ID, or deterministic display_block ID).
        :type content_id: str

        :param created_at: Timestamp when the interaction was added to the queue.
        :type created_at: datetime

        :param display_block: List of content blocks that make up a ``display_block`` interaction.
            Must contain at least one block.
        :type display_block: [LLMObsContentBlock], optional

        :param id: Unique identifier of the interaction.
        :type id: str

        :param modified_at: Timestamp when the interaction was last updated.
        :type modified_at: datetime

        :param queue_id: Identifier of the annotation queue this interaction belongs to.
        :type queue_id: str

        :param queue_name: Name of the annotation queue this interaction belongs to.
        :type queue_name: str

        :param type: Type of an annotated interaction.
        :type type: LLMObsAnyInteractionType
        """
        if display_block is not unset:
            kwargs["display_block"] = display_block
        super().__init__(kwargs)

        self_.annotations = annotations
        self_.content_id = content_id
        self_.created_at = created_at
        self_.id = id
        self_.modified_at = modified_at
        self_.queue_id = queue_id
        self_.queue_name = queue_name
        self_.type = type
