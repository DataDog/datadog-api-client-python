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
    from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_data_response import (
        LLMObsAnnotatedInteractionsByTraceDataResponse,
    )


class LLMObsAnnotatedInteractionsByTraceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interactions_by_trace_data_response import (
            LLMObsAnnotatedInteractionsByTraceDataResponse,
        )

        return {
            "data": (LLMObsAnnotatedInteractionsByTraceDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsAnnotatedInteractionsByTraceDataResponse, **kwargs):
        """
        Response containing annotated interactions across all queues for the requested content IDs.

        :param data: Data object for the cross-queue annotated interactions response.
        :type data: LLMObsAnnotatedInteractionsByTraceDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
