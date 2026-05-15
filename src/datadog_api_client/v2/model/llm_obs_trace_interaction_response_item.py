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
    from datadog_api_client.v2.model.llm_obs_trace_interaction_type import LLMObsTraceInteractionType


class LLMObsTraceInteractionResponseItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_trace_interaction_type import LLMObsTraceInteractionType

        return {
            "already_existed": (bool,),
            "content_id": (str,),
            "id": (str,),
            "type": (LLMObsTraceInteractionType,),
        }

    attribute_map = {
        "already_existed": "already_existed",
        "content_id": "content_id",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, already_existed: bool, content_id: str, id: str, type: LLMObsTraceInteractionType, **kwargs):
        """
        A trace, experiment trace, or session interaction result.

        :param already_existed: Whether this interaction already existed in the queue.
        :type already_existed: bool

        :param content_id: Upstream entity identifier supplied by the caller.
        :type content_id: str

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type of an upstream-entity interaction.
        :type type: LLMObsTraceInteractionType
        """
        super().__init__(kwargs)

        self_.already_existed = already_existed
        self_.content_id = content_id
        self_.id = id
        self_.type = type
