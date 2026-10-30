# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AIGuardToolCallFunction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arguments": (str,),
            "name": (str,),
        }

    attribute_map = {
        "arguments": "arguments",
        "name": "name",
    }

    def __init__(self_, arguments: str, name: str, **kwargs):
        """
        The function invoked by a tool call.

        :param arguments: The arguments of the function call, serialized as a JSON string.
        :type arguments: str

        :param name: The name of the function to call.
        :type name: str
        """
        super().__init__(kwargs)

        self_.arguments = arguments
        self_.name = name
