# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionMetricSemanticMode(ModelSimple):
    """
    Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed.

    :param value: Must be one of ["combined", "native"].
    :type value: str
    """

    allowed_values = {
        "combined",
        "native",
    }
    COMBINED: ClassVar["FormulaAndFunctionMetricSemanticMode"]
    NATIVE: ClassVar["FormulaAndFunctionMetricSemanticMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionMetricSemanticMode.COMBINED = FormulaAndFunctionMetricSemanticMode("combined")
FormulaAndFunctionMetricSemanticMode.NATIVE = FormulaAndFunctionMetricSemanticMode("native")
