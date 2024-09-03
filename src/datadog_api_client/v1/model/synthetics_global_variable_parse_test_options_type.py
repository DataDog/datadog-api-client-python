# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsGlobalVariableParseTestOptionsType(ModelSimple):
    """
    Type of value to extract from a test for a Synthetic global variable.

    :param value: Must be one of ["http_body", "http_header", "http_status_code", "local_variable"].
    :type value: str
    """

    allowed_values = {
        "http_body",
        "http_header",
        "http_status_code",
        "local_variable",
    }
    HTTP_BODY: ClassVar["SyntheticsGlobalVariableParseTestOptionsType"]
    HTTP_HEADER: ClassVar["SyntheticsGlobalVariableParseTestOptionsType"]
    HTTP_STATUS_CODE: ClassVar["SyntheticsGlobalVariableParseTestOptionsType"]
    LOCAL_VARIABLE: ClassVar["SyntheticsGlobalVariableParseTestOptionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsGlobalVariableParseTestOptionsType.HTTP_BODY = SyntheticsGlobalVariableParseTestOptionsType("http_body")
SyntheticsGlobalVariableParseTestOptionsType.HTTP_HEADER = SyntheticsGlobalVariableParseTestOptionsType("http_header")
SyntheticsGlobalVariableParseTestOptionsType.HTTP_STATUS_CODE = SyntheticsGlobalVariableParseTestOptionsType(
    "http_status_code"
)
SyntheticsGlobalVariableParseTestOptionsType.LOCAL_VARIABLE = SyntheticsGlobalVariableParseTestOptionsType(
    "local_variable"
)
