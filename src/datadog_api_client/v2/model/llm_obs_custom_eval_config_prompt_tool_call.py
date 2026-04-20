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


class LLMObsCustomEvalConfigPromptToolCall(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arguments": (str,),
            "id": (str,),
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "arguments": "arguments",
        "id": "id",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        arguments: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tool call within a prompt message.

        :param arguments: JSON-encoded arguments for the tool call.
        :type arguments: str, optional

        :param id: Unique identifier of the tool call.
        :type id: str, optional

        :param name: Name of the tool being called.
        :type name: str, optional

        :param type: Type of the tool call.
        :type type: str, optional
        """
        if arguments is not unset:
            kwargs["arguments"] = arguments
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
