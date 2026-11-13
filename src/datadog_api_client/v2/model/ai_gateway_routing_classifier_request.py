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


class AiGatewayRoutingClassifierRequest(ModelNormal):
    validations = {
        "confidence_threshold": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
        "context": {
            "max_length": 2000,
        },
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "confidence_threshold": (float, none_type),
            "context": (str,),
            "model": (str,),
            "provider": (str,),
        }

    attribute_map = {
        "confidence_threshold": "confidence_threshold",
        "context": "context",
        "model": "model",
        "provider": "provider",
    }

    def __init__(
        self_,
        confidence_threshold: Union[float, none_type, UnsetType] = unset,
        context: Union[str, UnsetType] = unset,
        model: Union[str, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Decision model and settings for a classified tier. Omission preserves the saved classifier; null clears it. Newly selected models require provider View.

        :param confidence_threshold: Minimum decision confidence. Omission preserves a saved value; new classifiers and explicit null default to 0.5.
        :type confidence_threshold: float, none_type, optional

        :param context: Traffic context for the classifier. Omission preserves saved context.
        :type context: str, optional

        :param model: Decision model on the provider. Omit together with provider to preserve the saved selection.
        :type model: str, optional

        :param provider: Decision-model provider slug. It must name a provider of type ``openai`` , ``baseten`` , or ``typesafe`` , the provider types that serve a decision model. Omit together with model to preserve the saved selection.
        :type provider: str, optional
        """
        if confidence_threshold is not unset:
            kwargs["confidence_threshold"] = confidence_threshold
        if context is not unset:
            kwargs["context"] = context
        if model is not unset:
            kwargs["model"] = model
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)
