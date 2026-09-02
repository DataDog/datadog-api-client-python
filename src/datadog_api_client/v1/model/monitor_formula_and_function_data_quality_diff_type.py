# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionDataQualityDiffType(ModelSimple):
    """
    How the difference between the source and target measures is computed.
        `absolute` subtracts the two values, `diff_percent` expresses the difference
        as a percentage of the source value.

    :param value: Must be one of ["absolute", "diff_percent"].
    :type value: str
    """

    allowed_values = {
        "absolute",
        "diff_percent",
    }
    ABSOLUTE: ClassVar["MonitorFormulaAndFunctionDataQualityDiffType"]
    DIFF_PERCENT: ClassVar["MonitorFormulaAndFunctionDataQualityDiffType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionDataQualityDiffType.ABSOLUTE = MonitorFormulaAndFunctionDataQualityDiffType("absolute")
MonitorFormulaAndFunctionDataQualityDiffType.DIFF_PERCENT = MonitorFormulaAndFunctionDataQualityDiffType("diff_percent")
