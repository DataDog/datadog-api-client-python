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


class AgenticEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
            "payload": (dict,),
            "type": (str,),
        }

    attribute_map = {
        "message": "message",
        "payload": "payload",
        "type": "type",
    }

    def __init__(self_, message: str, type: str, payload: Union[dict, UnsetType] = unset, **kwargs):
        """


        :param message: The message content.
        :type message: str

        :param payload: Additional payload data for the event.
        :type payload: dict, optional

        :param type: The type of agentic event.
        :type type: str
        """
        if payload is not unset:
            kwargs["payload"] = payload
        super().__init__(kwargs)

        self_.message = message
        self_.type = type
