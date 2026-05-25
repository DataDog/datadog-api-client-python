# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiPromptDataType(ModelSimple):
    """
    AI prompt resource type.

    :param value: If omitted defaults to "ai_prompt". Must be one of ["ai_prompt"].
    :type value: str
    """

    allowed_values = {
        "ai_prompt",
    }
    AI_PROMPT: ClassVar["AiPromptDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiPromptDataType.AI_PROMPT = AiPromptDataType("ai_prompt")
