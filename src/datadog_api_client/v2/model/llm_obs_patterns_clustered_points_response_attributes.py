# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_patterns_clustered_point import LLMObsPatternsClusteredPoint


class LLMObsPatternsClusteredPointsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_clustered_point import LLMObsPatternsClusteredPoint

        return {
            "next_page_token": (str, none_type),
            "points": ([LLMObsPatternsClusteredPoint],),
            "topic_id": (str,),
        }

    attribute_map = {
        "next_page_token": "next_page_token",
        "points": "points",
        "topic_id": "topic_id",
    }

    def __init__(
        self_,
        next_page_token: Union[str, none_type],
        points: List[LLMObsPatternsClusteredPoint],
        topic_id: str,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability patterns clustered points response.

        :param next_page_token: Pagination token for the next page of points. Null if there are no more pages.
        :type next_page_token: str, none_type

        :param points: List of clustered points.
        :type points: [LLMObsPatternsClusteredPoint]

        :param topic_id: Identifier of the topic the points belong to.
        :type topic_id: str
        """
        super().__init__(kwargs)

        self_.next_page_token = next_page_token
        self_.points = points
        self_.topic_id = topic_id
