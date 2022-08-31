# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsGlobalVariableParseTestOptionsType(ModelSimple):
    """
    Property of the Synthetics Test Response to use for a Synthetics global variable.

    :param value: Must be one of ["http_body", "http_header", "local_variable"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "HTTP_BODY": "http_body",
            "HTTP_HEADER": "http_header",
            "LOCAL_VARIABLE": "local_variable",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
