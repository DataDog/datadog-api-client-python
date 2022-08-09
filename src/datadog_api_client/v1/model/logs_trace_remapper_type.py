# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsTraceRemapperType(ModelSimple):
    """
    Type of logs trace remapper.

    :param value: If omitted defaults to "trace-id-remapper". Must be one of ["trace-id-remapper"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "TRACE_ID_REMAPPER": "trace-id-remapper",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
