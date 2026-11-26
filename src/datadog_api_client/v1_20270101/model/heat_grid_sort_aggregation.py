# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatGridSortAggregation(ModelSimple):
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
    SUM: ClassVar["HeatGridSortAggregation"]
    MIN: ClassVar["HeatGridSortAggregation"]
    MAX: ClassVar["HeatGridSortAggregation"]
    AVG: ClassVar["HeatGridSortAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatGridSortAggregation.SUM = HeatGridSortAggregation("sum")
HeatGridSortAggregation.MIN = HeatGridSortAggregation("min")
HeatGridSortAggregation.MAX = HeatGridSortAggregation("max")
HeatGridSortAggregation.AVG = HeatGridSortAggregation("avg")
