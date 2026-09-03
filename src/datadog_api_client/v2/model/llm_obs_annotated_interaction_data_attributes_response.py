# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem
    from datadog_api_client.v2.model.llm_obs_annotated_interaction_event import LLMObsAnnotatedInteractionEvent
    from datadog_api_client.v2.model.llm_obs_any_interaction_type import LLMObsAnyInteractionType
    from datadog_api_client.v2.model.llm_obs_trace_annotated_interaction_item import LLMObsTraceAnnotatedInteractionItem
    from datadog_api_client.v2.model.llm_obs_display_block_annotated_interaction_item import (
        LLMObsDisplayBlockAnnotatedInteractionItem,
    )


class LLMObsAnnotatedInteractionDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interaction_item import LLMObsAnnotatedInteractionItem
        from datadog_api_client.v2.model.llm_obs_annotated_interaction_event import LLMObsAnnotatedInteractionEvent
        from datadog_api_client.v2.model.llm_obs_any_interaction_type import LLMObsAnyInteractionType

        return {
            "annotated_interaction": (LLMObsAnnotatedInteractionItem,),
            "events": ([LLMObsAnnotatedInteractionEvent],),
            "interaction_type": (LLMObsAnyInteractionType,),
            "next_cursor": (str,),
        }

    attribute_map = {
        "annotated_interaction": "annotated_interaction",
        "events": "events",
        "interaction_type": "interaction_type",
        "next_cursor": "next_cursor",
    }

    def __init__(
        self_,
        annotated_interaction: Union[
            LLMObsAnnotatedInteractionItem,
            LLMObsTraceAnnotatedInteractionItem,
            LLMObsDisplayBlockAnnotatedInteractionItem,
        ],
        events: List[LLMObsAnnotatedInteractionEvent],
        interaction_type: LLMObsAnyInteractionType,
        next_cursor: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes containing an annotated interaction and its related events.

        :param annotated_interaction: An interaction with its associated annotations.
        :type annotated_interaction: LLMObsAnnotatedInteractionItem

        :param events: Page of events associated with the annotated interaction.
        :type events: [LLMObsAnnotatedInteractionEvent]

        :param interaction_type: Type of an annotated interaction.
        :type interaction_type: LLMObsAnyInteractionType

        :param next_cursor: Cursor to retrieve the next page of events. Absent when there are no more events.
        :type next_cursor: str, optional
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)

        self_.annotated_interaction = annotated_interaction
        self_.events = events
        self_.interaction_type = interaction_type
