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
    from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_response_attributes import (
        LLMObsPatternsTopicsWithClusteredPointsResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_type import (
        LLMObsPatternsTopicsWithClusteredPointsType,
    )


class LLMObsPatternsTopicsWithClusteredPointsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_response_attributes import (
            LLMObsPatternsTopicsWithClusteredPointsResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_topics_with_clustered_points_type import (
            LLMObsPatternsTopicsWithClusteredPointsType,
        )

        return {
            "attributes": (LLMObsPatternsTopicsWithClusteredPointsResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsTopicsWithClusteredPointsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsPatternsTopicsWithClusteredPointsResponseAttributes,
        id: str,
        type: LLMObsPatternsTopicsWithClusteredPointsType,
        **kwargs,
    ):
        """
        Data object of an LLM Observability patterns topics-with-clustered-points response.

        :param attributes: Attributes of an LLM Observability patterns topics-with-clustered-points response.
        :type attributes: LLMObsPatternsTopicsWithClusteredPointsResponseAttributes

        :param id: Identifier of the run the topics belong to.
        :type id: str

        :param type: Resource type of an LLM Observability patterns topics-with-clustered-points response.
        :type type: LLMObsPatternsTopicsWithClusteredPointsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
