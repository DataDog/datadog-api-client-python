# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionDataQualityDetectionType(ModelSimple):
    """
    How a `data-jobs alert` job duration monitor detects a breach. Must match the
        `.detection()` call in the monitor query. Required for job duration monitors.

    :param value: Must be one of ["static", "anomaly"].
    :type value: str
    """

    allowed_values = {
        "static",
        "anomaly",
    }
    STATIC: ClassVar["MonitorFormulaAndFunctionDataQualityDetectionType"]
    ANOMALY: ClassVar["MonitorFormulaAndFunctionDataQualityDetectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionDataQualityDetectionType.STATIC = MonitorFormulaAndFunctionDataQualityDetectionType("static")
MonitorFormulaAndFunctionDataQualityDetectionType.ANOMALY = MonitorFormulaAndFunctionDataQualityDetectionType("anomaly")
