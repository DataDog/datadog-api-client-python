# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsMeasureComparisonFilterInputOperation(ModelSimple):
    """
    Comparison applied by this filter.

    :param value: Must be one of ["=", "!=", ">", ">=", "<", "<="].
    :type value: str
    """

    allowed_values = {
        "=",
        "!=",
        ">",
        ">=",
        "<",
        "<=",
    }
    EQ: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]
    NEQ: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]
    GT: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]
    GT_EQ: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]
    LT: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]
    LT_EQ: ClassVar["ExperimentsMeasureComparisonFilterInputOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsMeasureComparisonFilterInputOperation.EQ = ExperimentsMeasureComparisonFilterInputOperation("=")
ExperimentsMeasureComparisonFilterInputOperation.NEQ = ExperimentsMeasureComparisonFilterInputOperation("!=")
ExperimentsMeasureComparisonFilterInputOperation.GT = ExperimentsMeasureComparisonFilterInputOperation(">")
ExperimentsMeasureComparisonFilterInputOperation.GT_EQ = ExperimentsMeasureComparisonFilterInputOperation(">=")
ExperimentsMeasureComparisonFilterInputOperation.LT = ExperimentsMeasureComparisonFilterInputOperation("<")
ExperimentsMeasureComparisonFilterInputOperation.LT_EQ = ExperimentsMeasureComparisonFilterInputOperation("<=")
