# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_pricing_required_rates import AiGatewayModelPricingRequiredRates
    from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_source import (
        AiGatewayModelPricingCustomRequestSource,
    )
    from datadog_api_client.v2.model.ai_gateway_model_pricing_tier import AiGatewayModelPricingTier


class AiGatewayModelPricingCustomRequestConfig(ModelNormal):
    validations = {
        "tiers": {
            "max_items": 16,
        },
        "version": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_required_rates import (
            AiGatewayModelPricingRequiredRates,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_source import (
            AiGatewayModelPricingCustomRequestSource,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_tier import AiGatewayModelPricingTier

        return {
            "rates": (AiGatewayModelPricingRequiredRates,),
            "source": (AiGatewayModelPricingCustomRequestSource,),
            "tiers": ([AiGatewayModelPricingTier],),
            "version": (int,),
        }

    attribute_map = {
        "rates": "rates",
        "source": "source",
        "tiers": "tiers",
        "version": "version",
    }

    def __init__(
        self_,
        rates: AiGatewayModelPricingRequiredRates,
        source: AiGatewayModelPricingCustomRequestSource,
        version: int,
        tiers: Union[List[AiGatewayModelPricingTier], UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom pricing configuration. All four rates are required.

        :param rates: Complete set of rates required for custom pricing.
        :type rates: AiGatewayModelPricingRequiredRates

        :param source: Source for a custom pricing configuration.
        :type source: AiGatewayModelPricingCustomRequestSource

        :param tiers: Custom prices that replace the base rates for the requests they select. Only valid for custom pricing.
            At most 16 tiers, and no two may share the same ``service_tier`` and ``context_min_tokens``.
        :type tiers: [AiGatewayModelPricingTier], optional

        :param version: Pricing configuration version. The only supported version is ``1``.
        :type version: int
        """
        if tiers is not unset:
            kwargs["tiers"] = tiers
        super().__init__(kwargs)

        self_.rates = rates
        self_.source = source
        self_.version = version
