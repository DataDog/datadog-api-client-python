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


class LLMObsInferenceToolResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "result": (str,),
            "tool_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "result": "result",
        "tool_id": "tool_id",
        "type": "type",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        result: Union[str, UnsetType] = unset,
        tool_id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The result returned by a tool call during LLM inference.

        :param name: The name of the tool that produced this result.
        :type name: str, optional

        :param result: The result content returned by the tool.
        :type result: str, optional

        :param tool_id: Identifier matching the corresponding tool call.
        :type tool_id: str, optional

        :param type: The type of tool result.
        :type type: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if result is not unset:
            kwargs["result"] = result
        if tool_id is not unset:
            kwargs["tool_id"] = tool_id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
