# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityModifierRuleShiftActionType(ModelSimple):
    """
    The type of a severity modifier rule action that shifts the severity by one rank.

    :param value: If omitted defaults to "shift". Must be one of ["shift"].
    :type value: str
    """

    allowed_values = {
        "shift",
    }
    SHIFT: ClassVar["SeverityModifierRuleShiftActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityModifierRuleShiftActionType.SHIFT = SeverityModifierRuleShiftActionType("shift")
