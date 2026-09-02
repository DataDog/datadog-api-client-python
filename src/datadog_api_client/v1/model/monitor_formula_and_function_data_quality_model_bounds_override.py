# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionDataQualityModelBoundsOverride(ModelSimple):
    """
    Restricts which predicted bound the monitor alerts on. `UPPER_ONLY` alerts only when
        the measure rises above the upper bound, `LOWER_ONLY` only when it falls below the
        lower bound. When unset, the monitor alerts on both.

    :param value: Must be one of ["UPPER_ONLY", "LOWER_ONLY"].
    :type value: str
    """

    allowed_values = {
        "UPPER_ONLY",
        "LOWER_ONLY",
    }
    UPPER_ONLY: ClassVar["MonitorFormulaAndFunctionDataQualityModelBoundsOverride"]
    LOWER_ONLY: ClassVar["MonitorFormulaAndFunctionDataQualityModelBoundsOverride"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionDataQualityModelBoundsOverride.UPPER_ONLY = (
    MonitorFormulaAndFunctionDataQualityModelBoundsOverride("UPPER_ONLY")
)
MonitorFormulaAndFunctionDataQualityModelBoundsOverride.LOWER_ONLY = (
    MonitorFormulaAndFunctionDataQualityModelBoundsOverride("LOWER_ONLY")
)
