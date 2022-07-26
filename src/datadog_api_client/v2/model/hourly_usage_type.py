# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class HourlyUsageType(ModelSimple):
    """
    Usage type that is being measured.

    :param value: Must be one of ["app_sec_host_count", "observability_pipelines_bytes_processed", "lambda_traced_invocations_count"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "APP_SEC_HOST_COUNT": "app_sec_host_count",
            "OBSERVABILITY_PIPELINES_BYTES_PROCESSSED": "observability_pipelines_bytes_processed",
            "LAMBDA_TRACED_INVOCATIONS_COUNT": "lambda_traced_invocations_count",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
