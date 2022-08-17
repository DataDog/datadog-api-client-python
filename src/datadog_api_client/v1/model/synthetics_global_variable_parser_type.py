# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsGlobalVariableParserType(ModelSimple):
    """
    Type of parser for a Synthetics global variable from a synthetics test.

    :param value: Must be one of ["raw", "json_path", "regex", "x_path"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "RAW": "raw",
            "JSON_PATH": "json_path",
            "REGEX": "regex",
            "X_PATH": "x_path",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
