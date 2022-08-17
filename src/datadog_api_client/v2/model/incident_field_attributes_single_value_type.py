# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class IncidentFieldAttributesSingleValueType(ModelSimple):
    """
    Type of the single value field definitions.

    :param value: If omitted defaults to "dropdown". Must be one of ["dropdown", "textbox"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "DROPDOWN": "dropdown",
            "TEXTBOX": "textbox",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
