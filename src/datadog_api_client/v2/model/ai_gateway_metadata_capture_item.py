# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayMetadataCaptureItem(ModelSimple):
    """
    An item Metadata-only capture can add to LLM Observability spans. Each is structure or a number, never conversation text. `tool_usage` adds tool call and result counts; `tool_output_size` adds estimated tool output tokens, total and average; `tool_names` adds each tool call and result with its name, ID and type; `conversation_shape` adds every message with its role and no text; `input_size_by_role` adds estimated input tokens per role; `available_tools` adds the names of the tools the request offered; `generation_settings` adds numeric and enumerated settings such as temperature and the finish reason.

    :param value: Must be one of ["tool_usage", "tool_output_size", "tool_names", "conversation_shape", "input_size_by_role", "available_tools", "generation_settings"].
    :type value: str
    """

    allowed_values = {
        "tool_usage",
        "tool_output_size",
        "tool_names",
        "conversation_shape",
        "input_size_by_role",
        "available_tools",
        "generation_settings",
    }
    TOOL_USAGE: ClassVar["AiGatewayMetadataCaptureItem"]
    TOOL_OUTPUT_SIZE: ClassVar["AiGatewayMetadataCaptureItem"]
    TOOL_NAMES: ClassVar["AiGatewayMetadataCaptureItem"]
    CONVERSATION_SHAPE: ClassVar["AiGatewayMetadataCaptureItem"]
    INPUT_SIZE_BY_ROLE: ClassVar["AiGatewayMetadataCaptureItem"]
    AVAILABLE_TOOLS: ClassVar["AiGatewayMetadataCaptureItem"]
    GENERATION_SETTINGS: ClassVar["AiGatewayMetadataCaptureItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayMetadataCaptureItem.TOOL_USAGE = AiGatewayMetadataCaptureItem("tool_usage")
AiGatewayMetadataCaptureItem.TOOL_OUTPUT_SIZE = AiGatewayMetadataCaptureItem("tool_output_size")
AiGatewayMetadataCaptureItem.TOOL_NAMES = AiGatewayMetadataCaptureItem("tool_names")
AiGatewayMetadataCaptureItem.CONVERSATION_SHAPE = AiGatewayMetadataCaptureItem("conversation_shape")
AiGatewayMetadataCaptureItem.INPUT_SIZE_BY_ROLE = AiGatewayMetadataCaptureItem("input_size_by_role")
AiGatewayMetadataCaptureItem.AVAILABLE_TOOLS = AiGatewayMetadataCaptureItem("available_tools")
AiGatewayMetadataCaptureItem.GENERATION_SETTINGS = AiGatewayMetadataCaptureItem("generation_settings")
