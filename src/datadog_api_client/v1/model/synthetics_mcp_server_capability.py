# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMCPServerCapability(ModelSimple):
    """
    A capability advertised by an MCP server.

    :param value: Must be one of ["completions", "experimental", "logging", "prompts", "resources", "tools"].
    :type value: str
    """

    allowed_values = {
        "completions",
        "experimental",
        "logging",
        "prompts",
        "resources",
        "tools",
    }
    COMPLETIONS: ClassVar["SyntheticsMCPServerCapability"]
    EXPERIMENTAL: ClassVar["SyntheticsMCPServerCapability"]
    LOGGING: ClassVar["SyntheticsMCPServerCapability"]
    PROMPTS: ClassVar["SyntheticsMCPServerCapability"]
    RESOURCES: ClassVar["SyntheticsMCPServerCapability"]
    TOOLS: ClassVar["SyntheticsMCPServerCapability"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMCPServerCapability.COMPLETIONS = SyntheticsMCPServerCapability("completions")
SyntheticsMCPServerCapability.EXPERIMENTAL = SyntheticsMCPServerCapability("experimental")
SyntheticsMCPServerCapability.LOGGING = SyntheticsMCPServerCapability("logging")
SyntheticsMCPServerCapability.PROMPTS = SyntheticsMCPServerCapability("prompts")
SyntheticsMCPServerCapability.RESOURCES = SyntheticsMCPServerCapability("resources")
SyntheticsMCPServerCapability.TOOLS = SyntheticsMCPServerCapability("tools")
