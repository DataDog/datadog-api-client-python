# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetMargin(ModelSimple):
    """
    Size of the margins around the image.
        **Note**: `small` and `large` values are deprecated.

    :param value: Must be one of ["sm", "md", "lg", "small", "large"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "SM": "sm",
            "MD": "md",
            "LG": "lg",
            "SMALL": "small",
            "LARGE": "large",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
