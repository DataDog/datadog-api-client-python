# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RecommendationsFilterRequestDataType(ModelSimple):
    """
    Legacy JSON:API resource type required by the cost recommendations search decoder.

    :param value: If omitted defaults to "recommendations_filter". Must be one of ["recommendations_filter"].
    :type value: str
    """

    allowed_values = {
        "recommendations_filter",
    }
    RECOMMENDATIONS_FILTER: ClassVar["RecommendationsFilterRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RecommendationsFilterRequestDataType.RECOMMENDATIONS_FILTER = RecommendationsFilterRequestDataType(
    "recommendations_filter"
)
