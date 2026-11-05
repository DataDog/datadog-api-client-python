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


class AiGatewayModelLimits(ModelNormal):
    validations = {
        "context_window_tokens": {
            "inclusive_minimum": 0,
        },
        "max_input_tokens": {
            "inclusive_minimum": 0,
        },
        "max_output_tokens": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "context_window_tokens": (int,),
            "max_input_tokens": (int,),
            "max_output_tokens": (int,),
        }

    attribute_map = {
        "context_window_tokens": "context_window_tokens",
        "max_input_tokens": "max_input_tokens",
        "max_output_tokens": "max_output_tokens",
    }

    def __init__(
        self_,
        context_window_tokens: Union[int, UnsetType] = unset,
        max_input_tokens: Union[int, UnsetType] = unset,
        max_output_tokens: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Token limits reported by the enrichment source.

        :param context_window_tokens: Total model context window in tokens.
        :type context_window_tokens: int, optional

        :param max_input_tokens: Maximum input tokens when reported separately.
        :type max_input_tokens: int, optional

        :param max_output_tokens: Maximum output tokens.
        :type max_output_tokens: int, optional
        """
        if context_window_tokens is not unset:
            kwargs["context_window_tokens"] = context_window_tokens
        if max_input_tokens is not unset:
            kwargs["max_input_tokens"] = max_input_tokens
        if max_output_tokens is not unset:
            kwargs["max_output_tokens"] = max_output_tokens
        super().__init__(kwargs)
