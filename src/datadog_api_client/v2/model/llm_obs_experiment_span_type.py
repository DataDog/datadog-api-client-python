# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsExperimentSpanType(ModelSimple):
    """
    Resource type for a span item in an experiment spans response.

    :param value: If omitted defaults to "experiments". Must be one of ["experiments"].
    :type value: str
    """

    allowed_values = {
        "experiments",
    }
    EXPERIMENTS_SPAN: ClassVar["LLMObsExperimentSpanType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsExperimentSpanType.EXPERIMENTS_SPAN = LLMObsExperimentSpanType("experiments")
