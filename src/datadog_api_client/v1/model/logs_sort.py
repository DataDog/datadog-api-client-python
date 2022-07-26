# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsSort(ModelSimple):
    """
    Time-ascending `asc` or time-descending `desc` results.

    :param value: Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "TIME_ASCENDING": "asc",
            "TIME_DESCENDING": "desc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
