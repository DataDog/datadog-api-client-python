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
    from datadog_api_client.v2.model.llm_obs_annotation_queue_interaction_response_item import (
        LLMObsAnnotationQueueInteractionResponseItem,
    )


class LLMObsAnnotationQueueInteractionsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_queue_interaction_response_item import (
            LLMObsAnnotationQueueInteractionResponseItem,
        )

        return {
            "interactions": ([LLMObsAnnotationQueueInteractionResponseItem],),
        }

    attribute_map = {
        "interactions": "interactions",
    }

    def __init__(self_, interactions: List[LLMObsAnnotationQueueInteractionResponseItem], **kwargs):
        """
        Attributes of the interaction addition response.

        :param interactions: List of interactions that were processed.
        :type interactions: [LLMObsAnnotationQueueInteractionResponseItem]
        """
        super().__init__(kwargs)

        self_.interactions = interactions
