# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricDatasetCloudCostScalarAggregation(ModelSimple):
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
    SUM: ClassVar["MetricDatasetCloudCostScalarAggregation"]
    MIN: ClassVar["MetricDatasetCloudCostScalarAggregation"]
    MAX: ClassVar["MetricDatasetCloudCostScalarAggregation"]
    AVG: ClassVar["MetricDatasetCloudCostScalarAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricDatasetCloudCostScalarAggregation.SUM = MetricDatasetCloudCostScalarAggregation("sum")
MetricDatasetCloudCostScalarAggregation.MIN = MetricDatasetCloudCostScalarAggregation("min")
MetricDatasetCloudCostScalarAggregation.MAX = MetricDatasetCloudCostScalarAggregation("max")
MetricDatasetCloudCostScalarAggregation.AVG = MetricDatasetCloudCostScalarAggregation("avg")
