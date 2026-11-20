# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaMetricsDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["metrics", "cloud_cost", "datadog_usage"].
    :type value: str
    """

    allowed_values = {
        "metrics",
        "cloud_cost",
        "datadog_usage",
    }
    METRICS: ClassVar["FormulaMetricsDataSource"]
    CLOUD_COST: ClassVar["FormulaMetricsDataSource"]
    DATADOG_USAGE: ClassVar["FormulaMetricsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaMetricsDataSource.METRICS = FormulaMetricsDataSource("metrics")
FormulaMetricsDataSource.CLOUD_COST = FormulaMetricsDataSource("cloud_cost")
FormulaMetricsDataSource.DATADOG_USAGE = FormulaMetricsDataSource("datadog_usage")
