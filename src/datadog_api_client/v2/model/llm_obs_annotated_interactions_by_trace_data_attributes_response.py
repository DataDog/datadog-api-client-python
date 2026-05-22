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
    from datadog_api_client.v2.model.llm_obs_annotated_interaction_by_trace_item import (
        LLMObsAnnotatedInteractionByTraceItem,
    )


class LLMObsAnnotatedInteractionsByTraceDataAttributesResponse(ModelNormal):
    validations = {
        "total_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interaction_by_trace_item import (
            LLMObsAnnotatedInteractionByTraceItem,
        )

        return {
            "annotated_interactions": ([LLMObsAnnotatedInteractionByTraceItem],),
            "total_count": (int,),
        }

    attribute_map = {
        "annotated_interactions": "annotated_interactions",
        "total_count": "total_count",
    }

    def __init__(
        self_, annotated_interactions: List[LLMObsAnnotatedInteractionByTraceItem], total_count: int, **kwargs
    ):
        """
        Attributes of the cross-queue annotated interactions response.

        :param annotated_interactions: List of annotated interactions across all queues for the requested content IDs.
        :type annotated_interactions: [LLMObsAnnotatedInteractionByTraceItem]

        :param total_count: Total number of annotated interactions matching the query.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.annotated_interactions = annotated_interactions
        self_.total_count = total_count
