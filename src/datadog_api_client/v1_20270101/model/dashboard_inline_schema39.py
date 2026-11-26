# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema39(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["sum", "min", "max", "avg", "count", "cardinality", "median", "delta", "latest", "earliest", "most_frequent", "any"].
    :type value: str
    """

    allowed_values = {
        "sum",
        "min",
        "max",
        "avg",
        "count",
        "cardinality",
        "median",
        "delta",
        "latest",
        "earliest",
        "most_frequent",
        "any",
    }
    SUM: ClassVar["DashboardInlineSchema39"]
    MIN: ClassVar["DashboardInlineSchema39"]
    MAX: ClassVar["DashboardInlineSchema39"]
    AVG: ClassVar["DashboardInlineSchema39"]
    COUNT: ClassVar["DashboardInlineSchema39"]
    CARDINALITY: ClassVar["DashboardInlineSchema39"]
    MEDIAN: ClassVar["DashboardInlineSchema39"]
    DELTA: ClassVar["DashboardInlineSchema39"]
    LATEST: ClassVar["DashboardInlineSchema39"]
    EARLIEST: ClassVar["DashboardInlineSchema39"]
    MOST_FREQUENT: ClassVar["DashboardInlineSchema39"]
    ANY: ClassVar["DashboardInlineSchema39"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema39.SUM = DashboardInlineSchema39("sum")
DashboardInlineSchema39.MIN = DashboardInlineSchema39("min")
DashboardInlineSchema39.MAX = DashboardInlineSchema39("max")
DashboardInlineSchema39.AVG = DashboardInlineSchema39("avg")
DashboardInlineSchema39.COUNT = DashboardInlineSchema39("count")
DashboardInlineSchema39.CARDINALITY = DashboardInlineSchema39("cardinality")
DashboardInlineSchema39.MEDIAN = DashboardInlineSchema39("median")
DashboardInlineSchema39.DELTA = DashboardInlineSchema39("delta")
DashboardInlineSchema39.LATEST = DashboardInlineSchema39("latest")
DashboardInlineSchema39.EARLIEST = DashboardInlineSchema39("earliest")
DashboardInlineSchema39.MOST_FREQUENT = DashboardInlineSchema39("most_frequent")
DashboardInlineSchema39.ANY = DashboardInlineSchema39("any")
