# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_mapping import (
        AiGatewayModelAutomaticPricingMapping,
    )
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_mode_trigger import (
        AiGatewayModelAutomaticPricingModeTrigger,
    )
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_rate import AiGatewayModelAutomaticPricingRate
    from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_source import (
        AiGatewayModelAutomaticPricingSource,
    )


class AiGatewayModelAutomaticPricing(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_mapping import (
            AiGatewayModelAutomaticPricingMapping,
        )
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_mode_trigger import (
            AiGatewayModelAutomaticPricingModeTrigger,
        )
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_rate import (
            AiGatewayModelAutomaticPricingRate,
        )
        from datadog_api_client.v2.model.ai_gateway_model_automatic_pricing_source import (
            AiGatewayModelAutomaticPricingSource,
        )

        return {
            "last_validated_at": (datetime,),
            "mapping": (AiGatewayModelAutomaticPricingMapping,),
            "mode_triggers": ([AiGatewayModelAutomaticPricingModeTrigger],),
            "observed_at": (datetime,),
            "rates": ([AiGatewayModelAutomaticPricingRate],),
            "source": (AiGatewayModelAutomaticPricingSource,),
            "stale": (bool,),
        }

    attribute_map = {
        "last_validated_at": "last_validated_at",
        "mapping": "mapping",
        "mode_triggers": "mode_triggers",
        "observed_at": "observed_at",
        "rates": "rates",
        "source": "source",
        "stale": "stale",
    }

    def __init__(
        self_,
        last_validated_at: datetime,
        observed_at: datetime,
        rates: List[AiGatewayModelAutomaticPricingRate],
        source: AiGatewayModelAutomaticPricingSource,
        stale: bool,
        mapping: Union[AiGatewayModelAutomaticPricingMapping, UnsetType] = unset,
        mode_triggers: Union[List[AiGatewayModelAutomaticPricingModeTrigger], UnsetType] = unset,
        **kwargs,
    ):
        """
        The published models.dev price. Present only when it is the effective price.

        :param last_validated_at: Time the price was last revalidated against the source.
        :type last_validated_at: datetime

        :param mapping: The reviewed endpoint mapping used to identify a custom provider. Omitted when the provider and model identity matched exactly.
        :type mapping: AiGatewayModelAutomaticPricingMapping, optional

        :param mode_triggers: Request fields that select each priced mode, such as ``speed: fast`` for ``anthropic`` models. Omitted when the model has a single mode.
        :type mode_triggers: [AiGatewayModelAutomaticPricingModeTrigger], optional

        :param observed_at: Time the price was observed in the source.
        :type observed_at: datetime

        :param rates: Published rates.
        :type rates: [AiGatewayModelAutomaticPricingRate]

        :param source: The pricing source entry the price was read from.
        :type source: AiGatewayModelAutomaticPricingSource

        :param stale: True when the price has not been revalidated recently and is being retained as last-known-good.
        :type stale: bool
        """
        if mapping is not unset:
            kwargs["mapping"] = mapping
        if mode_triggers is not unset:
            kwargs["mode_triggers"] = mode_triggers
        super().__init__(kwargs)

        self_.last_validated_at = last_validated_at
        self_.observed_at = observed_at
        self_.rates = rates
        self_.source = source
        self_.stale = stale
