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
    from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem


class LLMObsAnnotatedInteractionsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem

        return {
            "annotated_interactions": ([LLMObsAnnotatedInteractionItem],),
        }

    attribute_map = {
        "annotated_interactions": "annotated_interactions",
    }

    def __init__(self_, annotated_interactions: List[LLMObsAnnotatedInteractionItem], **kwargs):
        """
        Attributes containing the list of annotated interactions.

        :param annotated_interactions: List of interactions with their annotations.
        :type annotated_interactions: [LLMObsAnnotatedInteractionItem]
        """
        super().__init__(kwargs)

        self_.annotated_interactions = annotated_interactions
