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


class AiGatewayRoutingRuleClassifier(ModelNormal):
    validations = {
        "confidence_threshold": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "confidence_threshold": (float,),
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
        self_, confidence_threshold: float, model: str, provider: str, context: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Decision model of a classified tier.

        :param confidence_threshold: Probability from 0 to 1 that the picked destination must reach. Below it, the request goes to the default destination.
        :type confidence_threshold: float

        :param context: Prompt that tells the decision model about the rule's traffic. Omitted when empty.
        :type context: str, optional

        :param model: Canonical name of the decision model. Empty when the caller cannot view its provider.
        :type model: str

        :param provider: Slug of the provider that serves the decision model. Empty when the caller cannot view the provider.
        :type provider: str
        """
        if context is not unset:
            kwargs["context"] = context
        super().__init__(kwargs)

        self_.confidence_threshold = confidence_threshold
        self_.model = model
        self_.provider = provider
