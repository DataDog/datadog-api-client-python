# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionDataQualityDiffFunction(ModelSimple):
    """
    Function applied to the measure before it is compared against the predicted bounds.

    :param value: Must be one of ["DIFF", "DIFF_PERCENT"].
    :type value: str
    """

    allowed_values = {
        "DIFF",
        "DIFF_PERCENT",
    }
    DIFF: ClassVar["MonitorFormulaAndFunctionDataQualityDiffFunction"]
    DIFF_PERCENT: ClassVar["MonitorFormulaAndFunctionDataQualityDiffFunction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionDataQualityDiffFunction.DIFF = MonitorFormulaAndFunctionDataQualityDiffFunction("DIFF")
MonitorFormulaAndFunctionDataQualityDiffFunction.DIFF_PERCENT = MonitorFormulaAndFunctionDataQualityDiffFunction(
    "DIFF_PERCENT"
)
