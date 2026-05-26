# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiMemoryViolationResultDataType(ModelSimple):
    """
    AI memory violation result resource type.

    :param value: If omitted defaults to "ai_memory_violation_result". Must be one of ["ai_memory_violation_result"].
    :type value: str
    """

    allowed_values = {
        "ai_memory_violation_result",
    }
    AI_MEMORY_VIOLATION_RESULT: ClassVar["AiMemoryViolationResultDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiMemoryViolationResultDataType.AI_MEMORY_VIOLATION_RESULT = AiMemoryViolationResultDataType(
    "ai_memory_violation_result"
)
