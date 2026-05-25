# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiMemoryViolationType(ModelSimple):
    """
    The type of AI memory violation result indicating whether it is a true positive or false positive.

    :param value: Must be one of ["TP", "FP"].
    :type value: str
    """

    allowed_values = {
        "TP",
        "FP",
    }
    TP: ClassVar["AiMemoryViolationType"]
    FP: ClassVar["AiMemoryViolationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiMemoryViolationType.TP = AiMemoryViolationType("TP")
AiMemoryViolationType.FP = AiMemoryViolationType("FP")
