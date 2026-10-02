# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RecommendationV2RequestType(ModelSimple):
    """
    JSON:API resource type for the SPA v2 recommendation request.

    :param value: If omitted defaults to "recommendation_v2_request". Must be one of ["recommendation_v2_request"].
    :type value: str
    """

    allowed_values = {
        "recommendation_v2_request",
    }
    RECOMMENDATION_V2_REQUEST: ClassVar["RecommendationV2RequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RecommendationV2RequestType.RECOMMENDATION_V2_REQUEST = RecommendationV2RequestType("recommendation_v2_request")
