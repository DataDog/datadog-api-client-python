# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_pricing_rates import AiGatewayModelPricingRates


class AiGatewayModelPricingTier(ModelNormal):
    validations = {
        "context_min_tokens": {
            "inclusive_minimum": 0,
        },
        "service_tier": {
            "max_length": 64,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_rates import AiGatewayModelPricingRates

        return {
            "context_min_tokens": (int,),
            "rates": (AiGatewayModelPricingRates,),
            "service_tier": (str,),
        }

    attribute_map = {
        "context_min_tokens": "context_min_tokens",
        "rates": "rates",
        "service_tier": "service_tier",
    }

    def __init__(
        self_,
        rates: AiGatewayModelPricingRates,
        context_min_tokens: Union[int, UnsetType] = unset,
        service_tier: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom price for requests at or above ``context_min_tokens`` input tokens, in ``service_tier`` when it is set.
        Each tier needs a ``service_tier`` , a positive ``context_min_tokens`` , or both. Rates it omits keep the base custom rate.

        :param context_min_tokens: Minimum input tokens for the price to apply.
        :type context_min_tokens: int, optional

        :param rates: Pricing rates for a model.
        :type rates: AiGatewayModelPricingRates

        :param service_tier: Provider service tier the price applies to. Lowercase letters, digits, ``_`` and ``-``.
        :type service_tier: str, optional
        """
        if context_min_tokens is not unset:
            kwargs["context_min_tokens"] = context_min_tokens
        if service_tier is not unset:
            kwargs["service_tier"] = service_tier
        super().__init__(kwargs)

        self_.rates = rates
