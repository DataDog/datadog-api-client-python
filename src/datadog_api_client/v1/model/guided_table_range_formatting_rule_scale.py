# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableRangeFormattingRuleScale(ModelSimple):
    """
    Scale function for mapping values to colors.

    :param value: Must be one of ["linear", "log", "pow", "sqrt"].
    :type value: str
    """

    allowed_values = {
        "linear",
        "log",
        "pow",
        "sqrt",
    }
    LINEAR: ClassVar["GuidedTableRangeFormattingRuleScale"]
    LOG: ClassVar["GuidedTableRangeFormattingRuleScale"]
    POW: ClassVar["GuidedTableRangeFormattingRuleScale"]
    SQRT: ClassVar["GuidedTableRangeFormattingRuleScale"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableRangeFormattingRuleScale.LINEAR = GuidedTableRangeFormattingRuleScale("linear")
GuidedTableRangeFormattingRuleScale.LOG = GuidedTableRangeFormattingRuleScale("log")
GuidedTableRangeFormattingRuleScale.POW = GuidedTableRangeFormattingRuleScale("pow")
GuidedTableRangeFormattingRuleScale.SQRT = GuidedTableRangeFormattingRuleScale("sqrt")
