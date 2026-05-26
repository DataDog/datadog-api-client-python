# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryValueWidgetComparisonDirectionality(ModelSimple):
    """
    Color-coding direction: `increase_better` (green on rise), `decrease_better` (green on drop), or `neutral` (no color).

    :param value: If omitted defaults to "neutral". Must be one of ["increase_better", "decrease_better", "neutral"].
    :type value: str
    """

    allowed_values = {
        "increase_better",
        "decrease_better",
        "neutral",
    }
    INCREASE_BETTER: ClassVar["QueryValueWidgetComparisonDirectionality"]
    DECREASE_BETTER: ClassVar["QueryValueWidgetComparisonDirectionality"]
    NEUTRAL: ClassVar["QueryValueWidgetComparisonDirectionality"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryValueWidgetComparisonDirectionality.INCREASE_BETTER = QueryValueWidgetComparisonDirectionality("increase_better")
QueryValueWidgetComparisonDirectionality.DECREASE_BETTER = QueryValueWidgetComparisonDirectionality("decrease_better")
QueryValueWidgetComparisonDirectionality.NEUTRAL = QueryValueWidgetComparisonDirectionality("neutral")
