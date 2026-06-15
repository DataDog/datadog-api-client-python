# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsPatternsTopicsWithClusteredPointsType(ModelSimple):
    """
    Resource type of an LLM Observability patterns topics-with-clustered-points response.

    :param value: If omitted defaults to "get_topics_with_cluster_points_response". Must be one of ["get_topics_with_cluster_points_response"].
    :type value: str
    """

    allowed_values = {
        "get_topics_with_cluster_points_response",
    }
    GET_TOPICS_WITH_CLUSTER_POINTS_RESPONSE: ClassVar["LLMObsPatternsTopicsWithClusteredPointsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsPatternsTopicsWithClusteredPointsType.GET_TOPICS_WITH_CLUSTER_POINTS_RESPONSE = (
    LLMObsPatternsTopicsWithClusteredPointsType("get_topics_with_cluster_points_response")
)
