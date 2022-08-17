# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class DashboardLayoutType(ModelSimple):
    """
    Layout type of the dashboard.

    :param value: Must be one of ["ordered", "free"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ORDERED": "ordered",
            "FREE": "free",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
