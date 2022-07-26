# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsAssertionJSONPathOperator(ModelSimple):
    """
    Assertion operator to apply.

    :param value: If omitted defaults to "validatesJSONPath". Must be one of ["validatesJSONPath"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "VALIDATES_JSON_PATH": "validatesJSONPath",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
