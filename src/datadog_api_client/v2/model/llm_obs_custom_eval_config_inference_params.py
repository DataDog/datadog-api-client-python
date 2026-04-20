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


class LLMObsCustomEvalConfigInferenceParams(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "frequency_penalty": (float,),
            "max_tokens": (int,),
            "presence_penalty": (float,),
            "temperature": (float,),
            "top_k": (int,),
            "top_p": (float,),
        }

    attribute_map = {
        "frequency_penalty": "frequency_penalty",
        "max_tokens": "max_tokens",
        "presence_penalty": "presence_penalty",
        "temperature": "temperature",
        "top_k": "top_k",
        "top_p": "top_p",
    }

    def __init__(
        self_,
        frequency_penalty: Union[float, UnsetType] = unset,
        max_tokens: Union[int, UnsetType] = unset,
        presence_penalty: Union[float, UnsetType] = unset,
        temperature: Union[float, UnsetType] = unset,
        top_k: Union[int, UnsetType] = unset,
        top_p: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        LLM inference parameters for a custom evaluator.

        :param frequency_penalty: Frequency penalty to reduce repetition.
        :type frequency_penalty: float, optional

        :param max_tokens: Maximum number of tokens to generate.
        :type max_tokens: int, optional

        :param presence_penalty: Presence penalty to reduce repetition.
        :type presence_penalty: float, optional

        :param temperature: Sampling temperature for the LLM.
        :type temperature: float, optional

        :param top_k: Top-k sampling parameter.
        :type top_k: int, optional

        :param top_p: Top-p (nucleus) sampling parameter.
        :type top_p: float, optional
        """
        if frequency_penalty is not unset:
            kwargs["frequency_penalty"] = frequency_penalty
        if max_tokens is not unset:
            kwargs["max_tokens"] = max_tokens
        if presence_penalty is not unset:
            kwargs["presence_penalty"] = presence_penalty
        if temperature is not unset:
            kwargs["temperature"] = temperature
        if top_k is not unset:
            kwargs["top_k"] = top_k
        if top_p is not unset:
            kwargs["top_p"] = top_p
        super().__init__(kwargs)
