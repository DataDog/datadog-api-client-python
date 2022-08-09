# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class IncidentFieldAttributesValueType(ModelSimple):
    """
    Type of the multiple value field definitions.

    :param value: If omitted defaults to "multiselect". Must be one of ["multiselect", "textarray", "metrictag", "autocomplete"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "MULTISELECT": "multiselect",
            "TEXTARRAY": "textarray",
            "METRICTAG": "metrictag",
            "AUTOCOMPLETE": "autocomplete",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
