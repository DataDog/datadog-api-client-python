# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsLocalVariableParsingOptionsType(ModelSimple):
    """
    Property of the Synthetic Test Response to extract into a local variable.

    :param value: Must be one of ["grpc_message", "grpc_metadata", "http_body", "http_header", "http_status_code"].
    :type value: str
    """

    allowed_values = {
        "grpc_message",
        "grpc_metadata",
        "http_body",
        "http_header",
        "http_status_code",
    }
    GRPC_MESSAGE: ClassVar["SyntheticsLocalVariableParsingOptionsType"]
    GRPC_METADATA: ClassVar["SyntheticsLocalVariableParsingOptionsType"]
    HTTP_BODY: ClassVar["SyntheticsLocalVariableParsingOptionsType"]
    HTTP_HEADER: ClassVar["SyntheticsLocalVariableParsingOptionsType"]
    HTTP_STATUS_CODE: ClassVar["SyntheticsLocalVariableParsingOptionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsLocalVariableParsingOptionsType.GRPC_MESSAGE = SyntheticsLocalVariableParsingOptionsType("grpc_message")
SyntheticsLocalVariableParsingOptionsType.GRPC_METADATA = SyntheticsLocalVariableParsingOptionsType("grpc_metadata")
SyntheticsLocalVariableParsingOptionsType.HTTP_BODY = SyntheticsLocalVariableParsingOptionsType("http_body")
SyntheticsLocalVariableParsingOptionsType.HTTP_HEADER = SyntheticsLocalVariableParsingOptionsType("http_header")
SyntheticsLocalVariableParsingOptionsType.HTTP_STATUS_CODE = SyntheticsLocalVariableParsingOptionsType(
    "http_status_code"
)
