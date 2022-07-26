# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class DashboardType(ModelSimple):
    """
    The type of the dashboard.

    :param value: Must be one of ["custom_timeboard", "custom_screenboard", "integration_screenboard", "integration_timeboard", "host_timeboard"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CUSTOM_TIMEBOARD": "custom_timeboard",
            "CUSTOM_SCREENBOARD": "custom_screenboard",
            "INTEGRATION_SCREENBOARD": "integration_screenboard",
            "INTEGRATION_TIMEBOARD": "integration_timeboard",
            "HOST_TIMEBOARD": "host_timeboard",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
