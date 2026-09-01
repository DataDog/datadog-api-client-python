# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem
    from datadog_api_client.v2.model.llm_obs_trace_annotated_interaction_item import LLMObsTraceAnnotatedInteractionItem
    from datadog_api_client.v2.model.llm_obs_display_block_annotated_interaction_item import (
        LLMObsDisplayBlockAnnotatedInteractionItem,
    )
    from datadog_api_client.v2.model.llm_obs_frontend_annotated_interaction_item import (
        LLMObsFrontendAnnotatedInteractionItem,
    )


class LLMObsAnnotatedInteractionDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem

        return {
            "annotated_interaction": (LLMObsAnnotatedInteractionItem,),
        }

    attribute_map = {
        "annotated_interaction": "annotated_interaction",
    }

    def __init__(
        self_,
        annotated_interaction: Union[
            LLMObsAnnotatedInteractionItem,
            LLMObsTraceAnnotatedInteractionItem,
            LLMObsDisplayBlockAnnotatedInteractionItem,
            LLMObsFrontendAnnotatedInteractionItem,
        ],
        **kwargs,
    ):
        """
        Attributes containing the annotated interaction.

        :param annotated_interaction: An interaction with its associated annotations.
        :type annotated_interaction: LLMObsAnnotatedInteractionItem
        """
        super().__init__(kwargs)

        self_.annotated_interaction = annotated_interaction
