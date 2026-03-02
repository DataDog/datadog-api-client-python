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


class LLMObsExperimentSpanError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
            "stack": (str,),
            "type": (str,),
        }

    attribute_map = {
        "message": "message",
        "stack": "stack",
        "type": "type",
    }

    def __init__(
        self_,
        message: Union[str, UnsetType] = unset,
        stack: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Error details for an experiment span.

        :param message: Error message.
        :type message: str, optional

        :param stack: Stack trace of the error.
        :type stack: str, optional

        :param type: Type or class of the error.
        :type type: str, optional
        """
        if message is not unset:
            kwargs["message"] = message
        if stack is not unset:
            kwargs["stack"] = stack
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
