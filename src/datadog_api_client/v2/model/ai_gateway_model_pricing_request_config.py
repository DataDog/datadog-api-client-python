# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class AiGatewayModelPricingRequestConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Pricing configuration accepted when setting model pricing.

        :param rates: Complete set of rates required for custom pricing.
        :type rates: AiGatewayModelPricingRequiredRates

        :param source: Source for a custom pricing configuration.
        :type source: AiGatewayModelPricingCustomRequestSource

        :param version: Pricing configuration version. The only supported version is `1`.
        :type version: int

        :param overrides: Pricing rates for a model.
        :type overrides: AiGatewayModelPricingRates, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_config import (
            AiGatewayModelPricingCustomRequestConfig,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_catalog_request_config import (
            AiGatewayModelPricingCatalogRequestConfig,
        )

        return {
            "oneOf": [
                AiGatewayModelPricingCustomRequestConfig,
                AiGatewayModelPricingCatalogRequestConfig,
            ],
        }
