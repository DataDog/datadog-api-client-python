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
    from datadog_api_client.v2.model.llm_obs_interaction_type import LLMObsInteractionType


class LLMObsAnnotatedInteractionItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_item import LLMObsAnnotationItem
        from datadog_api_client.v2.model.llm_obs_interaction_type import LLMObsInteractionType

        return {
            "annotations": ([LLMObsAnnotationItem],),
            "content_id": (str,),
            "id": (str,),
            "type": (LLMObsInteractionType,),
        }

    attribute_map = {
        "annotations": "annotations",
        "content_id": "content_id",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, annotations: List[LLMObsAnnotationItem], content_id: str, id: str, type: LLMObsInteractionType, **kwargs
    ):
        """
        An interaction with its associated annotations.

        :param annotations: List of annotations for this interaction.
        :type annotations: [LLMObsAnnotationItem]

        :param content_id: Identifier of the content for this interaction.
        :type content_id: str

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type of interaction in an annotation queue.
        :type type: LLMObsInteractionType
        """
        super().__init__(kwargs)

        self_.annotations = annotations
        self_.content_id = content_id
        self_.id = id
        self_.type = type
