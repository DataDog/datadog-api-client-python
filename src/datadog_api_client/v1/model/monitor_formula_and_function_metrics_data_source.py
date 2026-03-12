# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionMetricsDataSource(ModelSimple):
    """
    Data source for metrics queries.

    :param value: Must be one of ["metrics", "cloud_cost", "datadog_usage"].
    :type value: str
    """

    allowed_values = {
        "metrics",
        "cloud_cost",
        "datadog_usage",
    }
    METRICS: ClassVar["MonitorFormulaAndFunctionMetricsDataSource"]
    CLOUD_COST: ClassVar["MonitorFormulaAndFunctionMetricsDataSource"]
    DATADOG_USAGE: ClassVar["MonitorFormulaAndFunctionMetricsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionMetricsDataSource.METRICS = MonitorFormulaAndFunctionMetricsDataSource("metrics")
MonitorFormulaAndFunctionMetricsDataSource.CLOUD_COST = MonitorFormulaAndFunctionMetricsDataSource("cloud_cost")
MonitorFormulaAndFunctionMetricsDataSource.DATADOG_USAGE = MonitorFormulaAndFunctionMetricsDataSource("datadog_usage")
