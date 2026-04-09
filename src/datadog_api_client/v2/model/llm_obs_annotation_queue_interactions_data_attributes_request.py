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
    from datadog_api_client.v2.model.llm_obs_annotation_queue_interaction_item import (
        LLMObsAnnotationQueueInteractionItem,
    )


class LLMObsAnnotationQueueInteractionsDataAttributesRequest(ModelNormal):
    validations = {
        "interactions": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_queue_interaction_item import (
            LLMObsAnnotationQueueInteractionItem,
        )

        return {
            "interactions": ([LLMObsAnnotationQueueInteractionItem],),
        }

    attribute_map = {
        "interactions": "interactions",
    }

    def __init__(self_, interactions: List[LLMObsAnnotationQueueInteractionItem], **kwargs):
        """
        Attributes for adding interactions to an annotation queue.

        :param interactions: List of interactions to add to the queue. Must contain at least one item.
        :type interactions: [LLMObsAnnotationQueueInteractionItem]
        """
        super().__init__(kwargs)

        self_.interactions = interactions
