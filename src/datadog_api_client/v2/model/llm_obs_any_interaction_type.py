# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnyInteractionType(ModelSimple):
    """
    Type of an annotated interaction.

    :param value: Must be one of ["trace", "experiment_trace", "session", "display_block"].
    :type value: str
    """

    allowed_values = {
        "trace",
        "experiment_trace",
        "session",
        "display_block",
    }
    TRACE: ClassVar["LLMObsAnyInteractionType"]
    EXPERIMENT_TRACE: ClassVar["LLMObsAnyInteractionType"]
    SESSION: ClassVar["LLMObsAnyInteractionType"]
    DISPLAY_BLOCK: ClassVar["LLMObsAnyInteractionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnyInteractionType.TRACE = LLMObsAnyInteractionType("trace")
LLMObsAnyInteractionType.EXPERIMENT_TRACE = LLMObsAnyInteractionType("experiment_trace")
LLMObsAnyInteractionType.SESSION = LLMObsAnyInteractionType("session")
LLMObsAnyInteractionType.DISPLAY_BLOCK = LLMObsAnyInteractionType("display_block")
