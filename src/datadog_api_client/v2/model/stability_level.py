# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StabilityLevel(ModelSimple):
    """
    The stability level for action filtering.

    :param value: Must be one of ["UNSPECIFIED", "DEV", "BETA", "STABLE"].
    :type value: str
    """

    allowed_values = {
        "UNSPECIFIED",
        "DEV",
        "BETA",
        "STABLE",
    }
    UNSPECIFIED: ClassVar["StabilityLevel"]
    DEV: ClassVar["StabilityLevel"]
    BETA: ClassVar["StabilityLevel"]
    STABLE: ClassVar["StabilityLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StabilityLevel.UNSPECIFIED = StabilityLevel("UNSPECIFIED")
StabilityLevel.DEV = StabilityLevel("DEV")
StabilityLevel.BETA = StabilityLevel("BETA")
StabilityLevel.STABLE = StabilityLevel("STABLE")
