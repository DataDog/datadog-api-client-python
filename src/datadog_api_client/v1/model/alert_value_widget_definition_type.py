# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AlertValueWidgetDefinitionType(ModelSimple):
    """
    Type of the alert value widget.

    :param value: If omitted defaults to "alert_value". Must be one of ["alert_value"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ALERT_VALUE": "alert_value",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
