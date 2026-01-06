# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventsAggregationValue(ModelSimple):
    """
    Standard aggregation types for events-based queries.

    :param value: Must be one of ["avg", "cardinality", "count", "delta", "earliest", "latest", "max", "median", "min", "most_frequent", "sum"].
    :type value: str
    """

    allowed_values = {
        "avg",
        "cardinality",
        "count",
        "delta",
        "earliest",
        "latest",
        "max",
        "median",
        "min",
        "most_frequent",
        "sum",
    }
    AVG: ClassVar["EventsAggregationValue"]
    CARDINALITY: ClassVar["EventsAggregationValue"]
    COUNT: ClassVar["EventsAggregationValue"]
    DELTA: ClassVar["EventsAggregationValue"]
    EARLIEST: ClassVar["EventsAggregationValue"]
    LATEST: ClassVar["EventsAggregationValue"]
    MAX: ClassVar["EventsAggregationValue"]
    MEDIAN: ClassVar["EventsAggregationValue"]
    MIN: ClassVar["EventsAggregationValue"]
    MOST_FREQUENT: ClassVar["EventsAggregationValue"]
    SUM: ClassVar["EventsAggregationValue"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventsAggregationValue.AVG = EventsAggregationValue("avg")
EventsAggregationValue.CARDINALITY = EventsAggregationValue("cardinality")
EventsAggregationValue.COUNT = EventsAggregationValue("count")
EventsAggregationValue.DELTA = EventsAggregationValue("delta")
EventsAggregationValue.EARLIEST = EventsAggregationValue("earliest")
EventsAggregationValue.LATEST = EventsAggregationValue("latest")
EventsAggregationValue.MAX = EventsAggregationValue("max")
EventsAggregationValue.MEDIAN = EventsAggregationValue("median")
EventsAggregationValue.MIN = EventsAggregationValue("min")
EventsAggregationValue.MOST_FREQUENT = EventsAggregationValue("most_frequent")
EventsAggregationValue.SUM = EventsAggregationValue("sum")
