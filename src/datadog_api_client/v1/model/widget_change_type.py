# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetChangeType(ModelSimple):
    """
    Show the absolute or the relative change.

    :param value: Must be one of ["absolute", "relative"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ABSOLUTE": "absolute",
            "RELATIVE": "relative",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
