# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsCustomEvalConfigParsingType(ModelSimple):
    """
    Output parsing type for a custom LLM judge evaluator.

    :param value: Must be one of ["structured_output", "json"].
    :type value: str
    """

    allowed_values = {
        "structured_output",
        "json",
    }
    STRUCTURED_OUTPUT: ClassVar["LLMObsCustomEvalConfigParsingType"]
    JSON: ClassVar["LLMObsCustomEvalConfigParsingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsCustomEvalConfigParsingType.STRUCTURED_OUTPUT = LLMObsCustomEvalConfigParsingType("structured_output")
LLMObsCustomEvalConfigParsingType.JSON = LLMObsCustomEvalConfigParsingType("json")
