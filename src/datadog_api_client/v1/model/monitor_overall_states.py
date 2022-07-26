# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MonitorOverallStates(ModelSimple):
    """
    The different states your monitor can be in.

    :param value: Must be one of ["Alert", "Ignored", "No Data", "OK", "Skipped", "Unknown", "Warn"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ALERT": "Alert",
            "IGNORED": "Ignored",
            "NO_DATA": "No Data",
            "OK": "OK",
            "SKIPPED": "Skipped",
            "UNKNOWN": "Unknown",
            "WARN": "Warn",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
