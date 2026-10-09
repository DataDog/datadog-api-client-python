# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatgridSortAggregation(ModelSimple):
    """
    Aggregation used to order rows over the displayed time range.

    :param value: Must be one of ["avg", "min", "max", "sum"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "min",
        "max",
        "sum",
    }
    AVG: ClassVar["HeatgridSortAggregation"]
    MIN: ClassVar["HeatgridSortAggregation"]
    MAX: ClassVar["HeatgridSortAggregation"]
    SUM: ClassVar["HeatgridSortAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatgridSortAggregation.AVG = HeatgridSortAggregation("avg")
HeatgridSortAggregation.MIN = HeatgridSortAggregation("min")
HeatgridSortAggregation.MAX = HeatgridSortAggregation("max")
HeatgridSortAggregation.SUM = HeatgridSortAggregation("sum")
