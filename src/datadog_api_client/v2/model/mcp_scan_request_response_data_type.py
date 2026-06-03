# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class McpScanRequestResponseDataType(ModelSimple):
    """
    The type identifier for MCP SCA scan request responses.

    :param value: If omitted defaults to "mcpscanrequestresponse". Must be one of ["mcpscanrequestresponse"].
    :type value: str
    """

    allowed_values = {
        "mcpscanrequestresponse",
    }
    MCPSCANREQUESTRESPONSE: ClassVar["McpScanRequestResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


McpScanRequestResponseDataType.MCPSCANREQUESTRESPONSE = McpScanRequestResponseDataType("mcpscanrequestresponse")
