# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetImageSizing(ModelSimple):
    """
    How to size the image on the widget. The values are based on the image `object-fit` CSS properties.
        **Note**: `zoom`, `fit` and `center` values are deprecated.

    :param value: Must be one of ["fill", "contain", "cover", "none", "scale-down", "zoom", "fit", "center"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "FILL": "fill",
            "CONTAIN": "contain",
            "COVER": "cover",
            "NONE": "none",
            "SCALEDOWN": "scale-down",
            "ZOOM": "zoom",
            "FIT": "fit",
            "CENTER": "center",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
