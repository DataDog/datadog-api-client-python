# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricDatasetMetricScalarAggregation(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["sum", "min", "max", "avg"].
    :type value: str
    """

    allowed_values = {
        "sum",
        "min",
        "max",
        "avg",
    }
    SUM: ClassVar["MetricDatasetMetricScalarAggregation"]
    MIN: ClassVar["MetricDatasetMetricScalarAggregation"]
    MAX: ClassVar["MetricDatasetMetricScalarAggregation"]
    AVG: ClassVar["MetricDatasetMetricScalarAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricDatasetMetricScalarAggregation.SUM = MetricDatasetMetricScalarAggregation("sum")
MetricDatasetMetricScalarAggregation.MIN = MetricDatasetMetricScalarAggregation("min")
MetricDatasetMetricScalarAggregation.MAX = MetricDatasetMetricScalarAggregation("max")
MetricDatasetMetricScalarAggregation.AVG = MetricDatasetMetricScalarAggregation("avg")
