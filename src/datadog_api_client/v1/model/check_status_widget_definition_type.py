# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class CheckStatusWidgetDefinitionType(ModelSimple):
    """
    Type of the check status widget.

    :param value: If omitted defaults to "check_status". Must be one of ["check_status"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CHECK_STATUS": "check_status",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
