# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetTextAlign(ModelSimple):
    """
    How to align the text on the widget.

    :param value: Must be one of ["center", "left", "right"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CENTER": "center",
            "LEFT": "left",
            "RIGHT": "right",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
