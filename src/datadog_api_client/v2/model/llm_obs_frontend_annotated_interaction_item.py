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
    from datadog_api_client.v2.model.llm_obs_annotation_item_response import LLMObsAnnotationItemResponse
    from datadog_api_client.v2.model.llm_obs_frontend_content import LLMObsFrontendContent
    from datadog_api_client.v2.model.llm_obs_frontend_interaction_type import LLMObsFrontendInteractionType


class LLMObsFrontendAnnotatedInteractionItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_item_response import LLMObsAnnotationItemResponse
        from datadog_api_client.v2.model.llm_obs_frontend_content import LLMObsFrontendContent
        from datadog_api_client.v2.model.llm_obs_frontend_interaction_type import LLMObsFrontendInteractionType

        return {
            "annotations": ([LLMObsAnnotationItemResponse],),
            "can_annotate": (bool,),
            "content_id": (str,),
            "frontend": (LLMObsFrontendContent,),
            "id": (str,),
            "type": (LLMObsFrontendInteractionType,),
        }

    attribute_map = {
        "annotations": "annotations",
        "can_annotate": "can_annotate",
        "content_id": "content_id",
        "frontend": "frontend",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        annotations: List[LLMObsAnnotationItemResponse],
        can_annotate: bool,
        content_id: str,
        frontend: LLMObsFrontendContent,
        id: str,
        type: LLMObsFrontendInteractionType,
        **kwargs,
    ):
        """
        A frontend interaction with its associated annotations.

        :param annotations: List of annotations for this interaction.
        :type annotations: [LLMObsAnnotationItemResponse]

        :param can_annotate: Whether the current caller can annotate this interaction.
        :type can_annotate: bool

        :param content_id: Server-generated deterministic identifier derived from the content.
        :type content_id: str

        :param frontend: Web content that makes up a ``frontend`` interaction.
        :type frontend: LLMObsFrontendContent

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type discriminator for a ``frontend`` interaction.
        :type type: LLMObsFrontendInteractionType
        """
        super().__init__(kwargs)

        self_.annotations = annotations
        self_.can_annotate = can_annotate
        self_.content_id = content_id
        self_.frontend = frontend
        self_.id = id
        self_.type = type
