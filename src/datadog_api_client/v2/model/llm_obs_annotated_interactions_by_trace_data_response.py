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
    from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_data_attributes_response import (
        LLMObsAnnotatedInteractionsByTraceDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_type import (
        LLMObsAnnotatedInteractionsByTraceType,
    )


class LLMObsAnnotatedInteractionsByTraceDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_data_attributes_response import (
            LLMObsAnnotatedInteractionsByTraceDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_type import (
            LLMObsAnnotatedInteractionsByTraceType,
        )

        return {
            "attributes": (LLMObsAnnotatedInteractionsByTraceDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsAnnotatedInteractionsByTraceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsAnnotatedInteractionsByTraceDataAttributesResponse,
        id: str,
        type: LLMObsAnnotatedInteractionsByTraceType,
        **kwargs,
    ):
        """
        Data object for the cross-queue annotated interactions response.

        :param attributes: Attributes of the cross-queue annotated interactions response.
        :type attributes: LLMObsAnnotatedInteractionsByTraceDataAttributesResponse

        :param id: Opaque identifier for the response object.
        :type id: str

        :param type: Resource type for cross-queue annotated interactions lookup.
        :type type: LLMObsAnnotatedInteractionsByTraceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
