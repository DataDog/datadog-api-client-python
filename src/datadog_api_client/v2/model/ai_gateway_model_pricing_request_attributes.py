# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_pricing_request_config import AiGatewayModelPricingRequestConfig
    from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_config import (
        AiGatewayModelPricingCustomRequestConfig,
    )
    from datadog_api_client.v2.model.ai_gateway_model_pricing_catalog_request_config import (
        AiGatewayModelPricingCatalogRequestConfig,
    )


class AiGatewayModelPricingRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_request_config import (
            AiGatewayModelPricingRequestConfig,
        )

        return {
            "pricing_config": (AiGatewayModelPricingRequestConfig,),
        }

    attribute_map = {
        "pricing_config": "pricing_config",
    }

    def __init__(
        self_,
        pricing_config: Union[
            AiGatewayModelPricingRequestConfig,
            AiGatewayModelPricingCustomRequestConfig,
            AiGatewayModelPricingCatalogRequestConfig,
        ],
        **kwargs,
    ):
        """
        Attributes for a model pricing request.

        :param pricing_config: Pricing configuration accepted when setting model pricing.
        :type pricing_config: AiGatewayModelPricingRequestConfig
        """
        super().__init__(kwargs)

        self_.pricing_config = pricing_config
