# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsMetricScoreType(ModelSimple):
    """
    Type of metric recorded for an LLM Observability experiment.

    :param value: Must be one of ["score", "categorical", "boolean", "json"].
    :type value: str
    """

    allowed_values = {
        "score",
        "categorical",
        "boolean",
        "json",
    }
    SCORE: ClassVar["LLMObsMetricScoreType"]
    CATEGORICAL: ClassVar["LLMObsMetricScoreType"]
    BOOLEAN: ClassVar["LLMObsMetricScoreType"]
    JSON: ClassVar["LLMObsMetricScoreType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsMetricScoreType.SCORE = LLMObsMetricScoreType("score")
LLMObsMetricScoreType.CATEGORICAL = LLMObsMetricScoreType("categorical")
LLMObsMetricScoreType.BOOLEAN = LLMObsMetricScoreType("boolean")
LLMObsMetricScoreType.JSON = LLMObsMetricScoreType("json")
