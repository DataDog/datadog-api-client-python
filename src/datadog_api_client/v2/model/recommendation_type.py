# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RecommendationType(ModelSimple):
    """
    JSON:API resource type for Spark Pod Autosizing recommendations. Identifies the Recommendation resource returned by SPA.

    :param value: If omitted defaults to "recommendation". Must be one of ["recommendation"].
    :type value: str
    """

    allowed_values = {
        "recommendation",
    }
    RECOMMENDATION: ClassVar["RecommendationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RecommendationType.RECOMMENDATION = RecommendationType("recommendation")
