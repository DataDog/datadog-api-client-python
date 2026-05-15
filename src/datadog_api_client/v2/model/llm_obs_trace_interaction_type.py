# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsTraceInteractionType(ModelSimple):
    """
    Type of an upstream-entity interaction.

    :param value: Must be one of ["trace", "experiment_trace", "session"].
    :type value: str
    """

    allowed_values = {
        "trace",
        "experiment_trace",
        "session",
    }
    TRACE: ClassVar["LLMObsTraceInteractionType"]
    EXPERIMENT_TRACE: ClassVar["LLMObsTraceInteractionType"]
    SESSION: ClassVar["LLMObsTraceInteractionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsTraceInteractionType.TRACE = LLMObsTraceInteractionType("trace")
LLMObsTraceInteractionType.EXPERIMENT_TRACE = LLMObsTraceInteractionType("experiment_trace")
LLMObsTraceInteractionType.SESSION = LLMObsTraceInteractionType("session")
