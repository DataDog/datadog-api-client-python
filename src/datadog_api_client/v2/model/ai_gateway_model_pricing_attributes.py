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
    from datadog_api_client.v2.model.ai_gateway_model_pricing_effective_source import (
        AiGatewayModelPricingEffectiveSource,
    )
    from datadog_api_client.v2.model.ai_gateway_model_pricing_config import AiGatewayModelPricingConfig


class AiGatewayModelPricingAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_effective_source import (
            AiGatewayModelPricingEffectiveSource,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_config import AiGatewayModelPricingConfig

        return {
            "effective_source": (AiGatewayModelPricingEffectiveSource,),
            "pricing_config": (AiGatewayModelPricingConfig,),
        }

    attribute_map = {
        "effective_source": "effective_source",
        "pricing_config": "pricing_config",
    }

    def __init__(
        self_,
        effective_source: Union[AiGatewayModelPricingEffectiveSource, UnsetType] = unset,
        pricing_config: Union[AiGatewayModelPricingConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a model pricing resource.

        :param effective_source: Effective source of the model pricing data.
        :type effective_source: AiGatewayModelPricingEffectiveSource, optional

        :param pricing_config: Pricing configuration for a model.
        :type pricing_config: AiGatewayModelPricingConfig, optional
        """
        if effective_source is not unset:
            kwargs["effective_source"] = effective_source
        if pricing_config is not unset:
            kwargs["pricing_config"] = pricing_config
        super().__init__(kwargs)
