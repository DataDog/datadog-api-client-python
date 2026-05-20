# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class LLMObsSpanToolCall(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arguments": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "name": (str,),
            "tool_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "arguments": "arguments",
        "name": "name",
        "tool_id": "tool_id",
        "type": "type",
    }

    def __init__(
        self_,
        arguments: Union[Dict[str, Any], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        tool_id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tool call made during a span.

        :param arguments: Arguments passed to the tool.
        :type arguments: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Name of the tool called.
        :type name: str, optional

        :param tool_id: Identifier of the tool call.
        :type tool_id: str, optional

        :param type: Type of the tool call.
        :type type: str, optional
        """
        if arguments is not unset:
            kwargs["arguments"] = arguments
        if name is not unset:
            kwargs["name"] = name
        if tool_id is not unset:
            kwargs["tool_id"] = tool_id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
