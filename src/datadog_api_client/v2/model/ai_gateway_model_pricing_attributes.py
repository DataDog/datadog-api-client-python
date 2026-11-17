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
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing import AiGatewayModelAutomaticPricing
    from datadog_api_client.v2.model.ai_gateway_model_pricing_effective_source import (
        AiGatewayModelPricingEffectiveSource,
    )
    from datadog_api_client.v2.model.ai_gateway_model_pricing_config import AiGatewayModelPricingConfig
    from datadog_api_client.v2.model.ai_gateway_model_pricing_status import AiGatewayModelPricingStatus


class AiGatewayModelPricingAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing import AiGatewayModelAutomaticPricing
        from datadog_api_client.v2.model.ai_gateway_model_pricing_effective_source import (
            AiGatewayModelPricingEffectiveSource,
        )
        from datadog_api_client.v2.model.ai_gateway_model_pricing_config import AiGatewayModelPricingConfig
        from datadog_api_client.v2.model.ai_gateway_model_pricing_status import AiGatewayModelPricingStatus

        return {
            "authoritative": (bool,),
            "automatic_pricing": (AiGatewayModelAutomaticPricing,),
            "blocks_budgeted_requests": (bool,),
            "cost_multiplier": (float,),
            "duration_priced": (bool,),
            "effective_source": (AiGatewayModelPricingEffectiveSource,),
            "pricing_config": (AiGatewayModelPricingConfig,),
            "status": (AiGatewayModelPricingStatus,),
            "unpriced_description": (str,),
            "unpriced_reason": (str,),
        }

    attribute_map = {
        "authoritative": "authoritative",
        "automatic_pricing": "automatic_pricing",
        "blocks_budgeted_requests": "blocks_budgeted_requests",
        "cost_multiplier": "cost_multiplier",
        "duration_priced": "duration_priced",
        "effective_source": "effective_source",
        "pricing_config": "pricing_config",
        "status": "status",
        "unpriced_description": "unpriced_description",
        "unpriced_reason": "unpriced_reason",
    }

    def __init__(
        self_,
        authoritative: Union[bool, UnsetType] = unset,
        automatic_pricing: Union[AiGatewayModelAutomaticPricing, UnsetType] = unset,
        blocks_budgeted_requests: Union[bool, UnsetType] = unset,
        cost_multiplier: Union[float, UnsetType] = unset,
        duration_priced: Union[bool, UnsetType] = unset,
        effective_source: Union[AiGatewayModelPricingEffectiveSource, UnsetType] = unset,
        pricing_config: Union[AiGatewayModelPricingConfig, UnsetType] = unset,
        status: Union[AiGatewayModelPricingStatus, UnsetType] = unset,
        unpriced_description: Union[str, UnsetType] = unset,
        unpriced_reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a model pricing resource.

        :param authoritative: True when models.dev pricing is authoritative for this organization and provider.
        :type authoritative: bool, optional

        :param automatic_pricing: The published models.dev price. Present only when it is the effective price.
        :type automatic_pricing: AiGatewayModelAutomaticPricing, optional

        :param blocks_budgeted_requests: True when a ``BLOCK`` budget covering this model rejects its requests before they reach the provider.
        :type blocks_budgeted_requests: bool, optional

        :param cost_multiplier: Effective provider multiplier applied to every reported rate.
        :type cost_multiplier: float, optional

        :param duration_priced: True when the provider bills this model per minute of audio instead of per token, as with transcription
            models. The gateway prices only per token, so it can't charge for these models, and a per-token
            override can't express their rate.
        :type duration_priced: bool, optional

        :param effective_source: Effective source of the model pricing data.
        :type effective_source: AiGatewayModelPricingEffectiveSource, optional

        :param pricing_config: Pricing configuration for a model.
        :type pricing_config: AiGatewayModelPricingConfig, optional

        :param status: Whether the gateway has a price for the model.
        :type status: AiGatewayModelPricingStatus, optional

        :param unpriced_description: Human-readable sentence for ``unpriced_reason``. Omitted when the model is priced or the code has no description yet.
        :type unpriced_description: str, optional

        :param unpriced_reason: Stable code explaining why the model has no price, such as ``automatic_price_absent``. Omitted when the model is priced.
        :type unpriced_reason: str, optional
        """
        if authoritative is not unset:
            kwargs["authoritative"] = authoritative
        if automatic_pricing is not unset:
            kwargs["automatic_pricing"] = automatic_pricing
        if blocks_budgeted_requests is not unset:
            kwargs["blocks_budgeted_requests"] = blocks_budgeted_requests
        if cost_multiplier is not unset:
            kwargs["cost_multiplier"] = cost_multiplier
        if duration_priced is not unset:
            kwargs["duration_priced"] = duration_priced
        if effective_source is not unset:
            kwargs["effective_source"] = effective_source
        if pricing_config is not unset:
            kwargs["pricing_config"] = pricing_config
        if status is not unset:
            kwargs["status"] = status
        if unpriced_description is not unset:
            kwargs["unpriced_description"] = unpriced_description
        if unpriced_reason is not unset:
            kwargs["unpriced_reason"] = unpriced_reason
        super().__init__(kwargs)
