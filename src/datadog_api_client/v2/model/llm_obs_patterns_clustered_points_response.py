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
    from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_response_data import (
        LLMObsPatternsClusteredPointsResponseData,
    )


class LLMObsPatternsClusteredPointsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_response_data import (
            LLMObsPatternsClusteredPointsResponseData,
        )

        return {
            "data": (LLMObsPatternsClusteredPointsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsPatternsClusteredPointsResponseData, **kwargs):
        """
        Response containing the clustered points of an LLM Observability topic.

        :param data: Data object of an LLM Observability patterns clustered points response.
        :type data: LLMObsPatternsClusteredPointsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
