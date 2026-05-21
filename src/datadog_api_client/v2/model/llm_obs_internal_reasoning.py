# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class LLMObsInternalReasoning(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "reasoning_tokens": (int, none_type),
            "text": (str,),
        }

    attribute_map = {
        "reasoning_tokens": "reasoning_tokens",
        "text": "text",
    }

    def __init__(self_, text: str, reasoning_tokens: Union[int, none_type, UnsetType] = unset, **kwargs):
        """
        The model's internal reasoning or thinking output, if available.

        :param reasoning_tokens: Number of tokens used for internal reasoning.
        :type reasoning_tokens: int, none_type, optional

        :param text: The reasoning text produced by the model.
        :type text: str
        """
        if reasoning_tokens is not unset:
            kwargs["reasoning_tokens"] = reasoning_tokens
        super().__init__(kwargs)

        self_.text = text
