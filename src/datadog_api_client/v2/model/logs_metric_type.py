# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsMetricType(ModelSimple):
    """
    The type of the resource. The value should always be logs_metrics.

    :param value: If omitted defaults to "logs_metrics". Must be one of ["logs_metrics"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "LOGS_METRICS": "logs_metrics",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
