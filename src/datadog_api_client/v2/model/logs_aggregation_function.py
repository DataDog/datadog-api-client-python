# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsAggregationFunction(ModelSimple):
    """
    An aggregation function

    :param value: Must be one of ["count", "cardinality", "pc75", "pc90", "pc95", "pc98", "pc99", "sum", "min", "max", "avg", "median"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COUNT": "count",
            "CARDINALITY": "cardinality",
            "PERCENTILE_75": "pc75",
            "PERCENTILE_90": "pc90",
            "PERCENTILE_95": "pc95",
            "PERCENTILE_98": "pc98",
            "PERCENTILE_99": "pc99",
            "SUM": "sum",
            "MIN": "min",
            "MAX": "max",
            "AVG": "avg",
            "MEDIAN": "median",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
