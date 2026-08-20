# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityModifierSeverityDelta(ModelSimple):
    """
    The direction in which to shift the severity of matched findings by one rank.

    :param value: Must be one of ["up_one", "down_one"].
    :type value: str
    """

    allowed_values = {
        "up_one",
        "down_one",
    }
    UP_ONE: ClassVar["SeverityModifierSeverityDelta"]
    DOWN_ONE: ClassVar["SeverityModifierSeverityDelta"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityModifierSeverityDelta.UP_ONE = SeverityModifierSeverityDelta("up_one")
SeverityModifierSeverityDelta.DOWN_ONE = SeverityModifierSeverityDelta("down_one")
