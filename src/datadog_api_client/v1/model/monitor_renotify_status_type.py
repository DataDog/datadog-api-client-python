# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MonitorRenotifyStatusType(ModelSimple):
    """
    The different statuses for which renotification is supported.

    :param value: Must be one of ["alert", "warn", "no data"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ALERT": "alert",
            "WARN": "warn",
            "NO_DATA": "no data",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
