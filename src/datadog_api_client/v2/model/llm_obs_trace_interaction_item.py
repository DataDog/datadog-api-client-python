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


class LLMObsTraceInteractionItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_trace_interaction_type import LLMObsTraceInteractionType

        return {
            "content_id": (str,),
            "type": (LLMObsTraceInteractionType,),
        }

    attribute_map = {
        "content_id": "content_id",
        "type": "type",
    }

    def __init__(self_, content_id: str, type: LLMObsTraceInteractionType, **kwargs):
        """
        An interaction that references an upstream trace, experiment trace, or session.

        :param content_id: Upstream entity identifier (trace, experiment trace, or session ID).
        :type content_id: str

        :param type: Type of an upstream-entity interaction.
        :type type: LLMObsTraceInteractionType
        """
        super().__init__(kwargs)

        self_.content_id = content_id
        self_.type = type
