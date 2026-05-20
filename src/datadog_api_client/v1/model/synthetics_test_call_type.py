# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestCallType(ModelSimple):
    """
    The type of call to perform. Used by gRPC steps (`healthcheck`, `unary`)
        and MCP steps (`init`, `tool_list`, `tool_call`). Valid values depend on
        the parent step's `subtype`.

    :param value: Must be one of ["healthcheck", "unary", "init", "tool_list", "tool_call"].
    :type value: str
    """

    allowed_values = {
        "healthcheck",
        "unary",
        "init",
        "tool_list",
        "tool_call",
    }
    HEALTHCHECK: ClassVar["SyntheticsTestCallType"]
    UNARY: ClassVar["SyntheticsTestCallType"]
    INIT: ClassVar["SyntheticsTestCallType"]
    TOOL_LIST: ClassVar["SyntheticsTestCallType"]
    TOOL_CALL: ClassVar["SyntheticsTestCallType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestCallType.HEALTHCHECK = SyntheticsTestCallType("healthcheck")
SyntheticsTestCallType.UNARY = SyntheticsTestCallType("unary")
SyntheticsTestCallType.INIT = SyntheticsTestCallType("init")
SyntheticsTestCallType.TOOL_LIST = SyntheticsTestCallType("tool_list")
SyntheticsTestCallType.TOOL_CALL = SyntheticsTestCallType("tool_call")
