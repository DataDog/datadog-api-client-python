# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricCustomTimeAggregation(ModelSimple):
    """
    A time aggregation for use in query.

    :param value: Must be one of ["avg", "count", "max", "min", "sum"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "AVG": "avg",
            "COUNT": "count",
            "MAX": "max",
            "MIN": "min",
            "SUM": "sum",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
