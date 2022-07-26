# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionEventAggregation(ModelSimple):
    """
    Aggregation methods for event platform queries.

    :param value: Must be one of ["count", "cardinality", "median", "pc75", "pc90", "pc95", "pc98", "pc99", "sum", "min", "max", "avg"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COUNT": "count",
            "CARDINALITY": "cardinality",
            "MEDIAN": "median",
            "PC75": "pc75",
            "PC90": "pc90",
            "PC95": "pc95",
            "PC98": "pc98",
            "PC99": "pc99",
            "SUM": "sum",
            "MIN": "min",
            "MAX": "max",
            "AVG": "avg",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
