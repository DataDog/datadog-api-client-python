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
    from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_response_data import (
        LLMObsPatternsTopicsWithClusteredPointsResponseData,
    )


class LLMObsPatternsTopicsWithClusteredPointsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_response_data import (
            LLMObsPatternsTopicsWithClusteredPointsResponseData,
        )

        return {
            "data": (LLMObsPatternsTopicsWithClusteredPointsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsPatternsTopicsWithClusteredPointsResponseData, **kwargs):
        """
        Response containing the topics, and the clustered points of their leaf topics,
        discovered by an LLM Observability patterns run.

        :param data: Data object of an LLM Observability patterns topics-with-clustered-points response.
        :type data: LLMObsPatternsTopicsWithClusteredPointsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
