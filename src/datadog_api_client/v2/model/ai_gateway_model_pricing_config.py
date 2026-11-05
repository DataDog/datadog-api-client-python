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
    from datadog_api_client.v2.model.ai_gateway_model_pricing_source import AiGatewayModelPricingSource


class AiGatewayModelPricingConfig(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_rates import AiGatewayModelPricingRates
        from datadog_api_client.v2.model.ai_gateway_model_pricing_source import AiGatewayModelPricingSource

        return {
            "overrides": (AiGatewayModelPricingRates,),
            "rates": (AiGatewayModelPricingRates,),
            "source": (AiGatewayModelPricingSource,),
            "version": (int,),
        }

    attribute_map = {
        "overrides": "overrides",
        "rates": "rates",
        "source": "source",
        "version": "version",
    }

    def __init__(
        self_,
        source: AiGatewayModelPricingSource,
        version: int,
        overrides: Union[AiGatewayModelPricingRates, UnsetType] = unset,
        rates: Union[AiGatewayModelPricingRates, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pricing configuration for a model.

        :param overrides: Pricing rates for a model.
        :type overrides: AiGatewayModelPricingRates, optional

        :param rates: Pricing rates for a model.
        :type rates: AiGatewayModelPricingRates, optional

        :param source: Source information for a model's pricing.
        :type source: AiGatewayModelPricingSource

        :param version: Pricing configuration version. The only supported version is ``1``.
        :type version: int
        """
        if overrides is not unset:
            kwargs["overrides"] = overrides
        if rates is not unset:
            kwargs["rates"] = rates
        super().__init__(kwargs)

        self_.source = source
        self_.version = version
