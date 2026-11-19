# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SensitiveDataScannerGroupTargetType(ModelSimple):
    """
    Type of target whose scanning groups are served by the target-scoped group routes. `llm_observability` is Agent Observability.

    :param value: If omitted defaults to "llm_observability". Must be one of ["llm_observability"].
    :type value: str
    """

    allowed_values = {
        "llm_observability",
    }
    LLM_OBSERVABILITY: ClassVar["SensitiveDataScannerGroupTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SensitiveDataScannerGroupTargetType.LLM_OBSERVABILITY = SensitiveDataScannerGroupTargetType("llm_observability")
