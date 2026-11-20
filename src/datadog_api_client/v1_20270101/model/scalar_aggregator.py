# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScalarAggregator(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["sum", "min", "max", "avg", "last", "area", "l2norm", "percentile", "stddev", "count_unique"].
    :type value: str
    """

    allowed_values = {
        "sum",
        "min",
        "max",
        "avg",
        "last",
        "area",
        "l2norm",
        "percentile",
        "stddev",
        "count_unique",
    }
    SUM: ClassVar["ScalarAggregator"]
    MIN: ClassVar["ScalarAggregator"]
    MAX: ClassVar["ScalarAggregator"]
    AVG: ClassVar["ScalarAggregator"]
    LAST: ClassVar["ScalarAggregator"]
    AREA: ClassVar["ScalarAggregator"]
    L2NORM: ClassVar["ScalarAggregator"]
    PERCENTILE: ClassVar["ScalarAggregator"]
    STDDEV: ClassVar["ScalarAggregator"]
    COUNT_UNIQUE: ClassVar["ScalarAggregator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScalarAggregator.SUM = ScalarAggregator("sum")
ScalarAggregator.MIN = ScalarAggregator("min")
ScalarAggregator.MAX = ScalarAggregator("max")
ScalarAggregator.AVG = ScalarAggregator("avg")
ScalarAggregator.LAST = ScalarAggregator("last")
ScalarAggregator.AREA = ScalarAggregator("area")
ScalarAggregator.L2NORM = ScalarAggregator("l2norm")
ScalarAggregator.PERCENTILE = ScalarAggregator("percentile")
ScalarAggregator.STDDEV = ScalarAggregator("stddev")
ScalarAggregator.COUNT_UNIQUE = ScalarAggregator("count_unique")
