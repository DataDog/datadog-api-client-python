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
    from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_response_attributes import (
        LLMObsPatternsClusteredPointsResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_type import LLMObsPatternsClusteredPointsType


class LLMObsPatternsClusteredPointsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_response_attributes import (
            LLMObsPatternsClusteredPointsResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_clustered_points_type import LLMObsPatternsClusteredPointsType

        return {
            "attributes": (LLMObsPatternsClusteredPointsResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsClusteredPointsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsPatternsClusteredPointsResponseAttributes,
        id: str,
        type: LLMObsPatternsClusteredPointsType,
        **kwargs,
    ):
        """
        Data object of an LLM Observability patterns clustered points response.

        :param attributes: Attributes of an LLM Observability patterns clustered points response.
        :type attributes: LLMObsPatternsClusteredPointsResponseAttributes

        :param id: Identifier of the topic the points belong to.
        :type id: str

        :param type: Resource type of an LLM Observability patterns clustered points response.
        :type type: LLMObsPatternsClusteredPointsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
