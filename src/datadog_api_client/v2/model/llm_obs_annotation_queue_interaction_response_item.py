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
    from datadog_api_client.v2.model.llm_obs_interaction_type import LLMObsInteractionType


class LLMObsAnnotationQueueInteractionResponseItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_interaction_type import LLMObsInteractionType

        return {
            "already_existed": (bool,),
            "content_id": (str,),
            "id": (str,),
            "type": (LLMObsInteractionType,),
        }

    attribute_map = {
        "already_existed": "already_existed",
        "content_id": "content_id",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, already_existed: bool, content_id: str, id: str, type: LLMObsInteractionType, **kwargs):
        """
        A single interaction result.

        :param already_existed: Whether this interaction already existed in the queue.
        :type already_existed: bool

        :param content_id: Identifier of the content (trace ID or session ID) for this interaction.
        :type content_id: str

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type of interaction in an annotation queue.
        :type type: LLMObsInteractionType
        """
        super().__init__(kwargs)

        self_.already_existed = already_existed
        self_.content_id = content_id
        self_.id = id
        self_.type = type
