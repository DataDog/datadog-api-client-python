# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetAstResponseDataType(ModelSimple):
    """
    Get AST response resource type.

    :param value: If omitted defaults to "get_ast_response". Must be one of ["get_ast_response"].
    :type value: str
    """

    allowed_values = {
        "get_ast_response",
    }
    GET_AST_RESPONSE: ClassVar["GetAstResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetAstResponseDataType.GET_AST_RESPONSE = GetAstResponseDataType("get_ast_response")
