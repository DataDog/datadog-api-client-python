# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SunburstWidgetLegendInlineAutomaticType(ModelSimple):
    """
    Whether to show the legend inline or let it be automatically generated.

    :param value: Must be one of ["inline", "automatic"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "INLINE": "inline",
            "AUTOMATIC": "automatic",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
