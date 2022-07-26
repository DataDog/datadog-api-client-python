# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricEstimateType(ModelSimple):
    """
    Estimate type based on the queried configuration. By default, `count_or_gauge` is returned. `distribution` is returned for distribution metrics without percentiles enabled. Lastly, `percentile` is returned if `filter[pct]=true` is queried with a distribution metric.

    :param value: If omitted defaults to "count_or_gauge". Must be one of ["count_or_gauge", "distribution", "percentile"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COUNT_OR_GAUGE": "count_or_gauge",
            "DISTRIBUTION": "distribution",
            "PERCENTILE": "percentile",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
