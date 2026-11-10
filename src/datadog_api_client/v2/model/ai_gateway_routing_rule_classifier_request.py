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


class AiGatewayRoutingRuleClassifierRequest(ModelNormal):
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
        Decision model that picks the destination of a classified tier.

        :param confidence_threshold: Probability from 0 to 1 that the picked destination must reach. Below it, the request goes to the default destination. Omitted or null defaults to 0.5.
        :type confidence_threshold: float, none_type, optional

        :param context: Optional prompt that tells the decision model about the rule's traffic, in up to 2000 characters.
        :type context: str, optional

        :param model: Canonical name of the decision model on that provider. The model must be enabled on the provider and support its decision API. Required when the rule has no saved decision model. On replacement, omit both provider and model to keep the rule's saved decision model.
        :type model: str, optional

        :param provider: Slug of the provider that serves the decision model. Its known_provider must be ``openai`` , ``baseten`` , or ``typesafe`` , and "*" is not allowed. A new selection requires provider View. Required when the rule has no saved decision model. On replacement, omit both provider and model to keep the rule's saved decision model.
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
