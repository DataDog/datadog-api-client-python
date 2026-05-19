# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsAssertionMCPServerCapabilitiesType(ModelSimple):
    """
    Type of the assertion.

    :param value: If omitted defaults to "mcpServerCapabilities". Must be one of ["mcpServerCapabilities"].
    :type value: str
    """

    allowed_values = {
        "mcpServerCapabilities",
    }
    MCP_SERVER_CAPABILITIES: ClassVar["SyntheticsAssertionMCPServerCapabilitiesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsAssertionMCPServerCapabilitiesType.MCP_SERVER_CAPABILITIES = SyntheticsAssertionMCPServerCapabilitiesType(
    "mcpServerCapabilities"
)
