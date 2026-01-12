# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionDataQualityModelTypeOverride(ModelSimple):
    """
    Override for the model type used in anomaly detection.

    :param value: Must be one of ["freshness", "percentage", "any"].
    :type value: str
    """

    allowed_values = {
        "freshness",
        "percentage",
        "any",
    }
    FRESHNESS: ClassVar["MonitorFormulaAndFunctionDataQualityModelTypeOverride"]
    PERCENTAGE: ClassVar["MonitorFormulaAndFunctionDataQualityModelTypeOverride"]
    ANY: ClassVar["MonitorFormulaAndFunctionDataQualityModelTypeOverride"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionDataQualityModelTypeOverride.FRESHNESS = MonitorFormulaAndFunctionDataQualityModelTypeOverride(
    "freshness"
)
MonitorFormulaAndFunctionDataQualityModelTypeOverride.PERCENTAGE = (
    MonitorFormulaAndFunctionDataQualityModelTypeOverride("percentage")
)
MonitorFormulaAndFunctionDataQualityModelTypeOverride.ANY = MonitorFormulaAndFunctionDataQualityModelTypeOverride("any")
