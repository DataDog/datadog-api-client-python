# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AllocationType(ModelSimple):
    """
    The type of targeting rule (called allocation in the API model).

    :param value: Must be one of ["FEATURE_GATE", "CANARY"].
    :type value: str
    """

    allowed_values = {
        "FEATURE_GATE",
        "CANARY",
    }
    FEATURE_GATE: ClassVar["AllocationType"]
    CANARY: ClassVar["AllocationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AllocationType.FEATURE_GATE = AllocationType("FEATURE_GATE")
AllocationType.CANARY = AllocationType("CANARY")
