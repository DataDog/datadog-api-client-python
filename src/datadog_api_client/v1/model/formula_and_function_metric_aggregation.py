# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionMetricAggregation(ModelSimple):
    """
    The aggregation methods available for metrics queries.

    :param value: Must be one of ["avg", "min", "max", "sum", "last", "area", "l2norm", "percentile"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "AVG": "avg",
            "MIN": "min",
            "MAX": "max",
            "SUM": "sum",
            "LAST": "last",
            "AREA": "area",
            "L2NORM": "l2norm",
            "PERCENTILE": "percentile",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
