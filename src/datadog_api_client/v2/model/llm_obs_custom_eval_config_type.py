# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsCustomEvalConfigType(ModelSimple):
    """
    Type of the custom LLM Observability evaluator configuration resource.

    :param value: If omitted defaults to "evaluator_config". Must be one of ["evaluator_config"].
    :type value: str
    """

    allowed_values = {
        "evaluator_config",
    }
    EVALUATOR_CONFIG: ClassVar["LLMObsCustomEvalConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsCustomEvalConfigType.EVALUATOR_CONFIG = LLMObsCustomEvalConfigType("evaluator_config")
