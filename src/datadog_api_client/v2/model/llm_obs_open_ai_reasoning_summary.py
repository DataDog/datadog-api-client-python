# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsOpenAIReasoningSummary(ModelSimple):
    """
    The verbosity of the reasoning summary.

    :param value: Must be one of ["auto", "concise", "detailed"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "concise",
        "detailed",
    }
    AUTO: ClassVar["LLMObsOpenAIReasoningSummary"]
    CONCISE: ClassVar["LLMObsOpenAIReasoningSummary"]
    DETAILED: ClassVar["LLMObsOpenAIReasoningSummary"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsOpenAIReasoningSummary.AUTO = LLMObsOpenAIReasoningSummary("auto")
LLMObsOpenAIReasoningSummary.CONCISE = LLMObsOpenAIReasoningSummary("concise")
LLMObsOpenAIReasoningSummary.DETAILED = LLMObsOpenAIReasoningSummary("detailed")
