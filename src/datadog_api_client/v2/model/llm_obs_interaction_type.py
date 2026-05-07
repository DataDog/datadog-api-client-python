# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsInteractionType(ModelSimple):
    """
    Type of interaction in an annotation queue.

    :param value: Must be one of ["trace", "experiment_trace", "session"].
    :type value: str
    """

    allowed_values = {
        "trace",
        "experiment_trace",
        "session",
    }
    TRACE: ClassVar["LLMObsInteractionType"]
    EXPERIMENT_TRACE: ClassVar["LLMObsInteractionType"]
    SESSION: ClassVar["LLMObsInteractionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsInteractionType.TRACE = LLMObsInteractionType("trace")
LLMObsInteractionType.EXPERIMENT_TRACE = LLMObsInteractionType("experiment_trace")
LLMObsInteractionType.SESSION = LLMObsInteractionType("session")
