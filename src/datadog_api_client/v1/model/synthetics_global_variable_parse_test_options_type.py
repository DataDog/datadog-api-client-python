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
        "http_body",
        "http_header",
        "local_variable",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsGlobalVariableParseTestOptionsType.HTTP_BODY = SyntheticsGlobalVariableParseTestOptionsType("http_body")
SyntheticsGlobalVariableParseTestOptionsType.HTTP_HEADER = SyntheticsGlobalVariableParseTestOptionsType("http_header")
SyntheticsGlobalVariableParseTestOptionsType.LOCAL_VARIABLE = SyntheticsGlobalVariableParseTestOptionsType(
    "local_variable"
)
