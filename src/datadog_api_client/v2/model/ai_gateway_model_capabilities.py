# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AiGatewayModelCapabilities(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attachment": (bool,),
            "interleaved_reasoning": (bool,),
            "reasoning": (bool,),
            "structured_output": (bool,),
            "temperature": (bool,),
            "tool_call": (bool,),
        }

    attribute_map = {
        "attachment": "attachment",
        "interleaved_reasoning": "interleaved_reasoning",
        "reasoning": "reasoning",
        "structured_output": "structured_output",
        "temperature": "temperature",
        "tool_call": "tool_call",
    }

    def __init__(
        self_,
        attachment: Union[bool, UnsetType] = unset,
        interleaved_reasoning: Union[bool, UnsetType] = unset,
        reasoning: Union[bool, UnsetType] = unset,
        structured_output: Union[bool, UnsetType] = unset,
        temperature: Union[bool, UnsetType] = unset,
        tool_call: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Model features reported by the enrichment source. Omitted properties are unknown.

        :param attachment: Whether attachment input is supported.
        :type attachment: bool, optional

        :param interleaved_reasoning: Whether reasoning can be interleaved with tool use.
        :type interleaved_reasoning: bool, optional

        :param reasoning: Whether reasoning is supported.
        :type reasoning: bool, optional

        :param structured_output: Whether structured output is supported.
        :type structured_output: bool, optional

        :param temperature: Whether temperature can be configured.
        :type temperature: bool, optional

        :param tool_call: Whether tool calls are supported.
        :type tool_call: bool, optional
        """
        if attachment is not unset:
            kwargs["attachment"] = attachment
        if interleaved_reasoning is not unset:
            kwargs["interleaved_reasoning"] = interleaved_reasoning
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if structured_output is not unset:
            kwargs["structured_output"] = structured_output
        if temperature is not unset:
            kwargs["temperature"] = temperature
        if tool_call is not unset:
            kwargs["tool_call"] = tool_call
        super().__init__(kwargs)
