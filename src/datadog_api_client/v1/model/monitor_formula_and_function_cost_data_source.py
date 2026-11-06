# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionCostDataSource(ModelSimple):
    """
    Data source for cost queries.

    :param value: Must be one of ["cloud_cost", "datadog_usage"].
    :type value: str
    """

    allowed_values = {
        "cloud_cost",
        "datadog_usage",
    }
    CLOUD_COST: ClassVar["MonitorFormulaAndFunctionCostDataSource"]
    DATADOG_USAGE: ClassVar["MonitorFormulaAndFunctionCostDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionCostDataSource.CLOUD_COST = MonitorFormulaAndFunctionCostDataSource("cloud_cost")
MonitorFormulaAndFunctionCostDataSource.DATADOG_USAGE = MonitorFormulaAndFunctionCostDataSource("datadog_usage")
