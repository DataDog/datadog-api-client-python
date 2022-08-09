# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleQueryAggregation(ModelSimple):
    """
    The aggregation type.

    :param value: Must be one of ["count", "cardinality", "sum", "max", "new_value", "geo_data"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COUNT": "count",
            "CARDINALITY": "cardinality",
            "SUM": "sum",
            "MAX": "max",
            "NEW_VALUE": "new_value",
            "GEO_DATA": "geo_data",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
