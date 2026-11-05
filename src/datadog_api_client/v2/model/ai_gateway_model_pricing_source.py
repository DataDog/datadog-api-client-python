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
    from datadog_api_client.v2.model.ai_gateway_model_pricing_source_type import AiGatewayModelPricingSourceType


class AiGatewayModelPricingSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_source_type import AiGatewayModelPricingSourceType

        return {
            "provider_id": (str,),
            "type": (AiGatewayModelPricingSourceType,),
        }

    attribute_map = {
        "provider_id": "provider_id",
        "type": "type",
    }

    def __init__(self_, type: AiGatewayModelPricingSourceType, provider_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Source information for a model's pricing.

        :param provider_id: Pricing catalog provider identifier.
        :type provider_id: str, optional

        :param type: Source type for the pricing configuration.
        :type type: AiGatewayModelPricingSourceType
        """
        if provider_id is not unset:
            kwargs["provider_id"] = provider_id
        super().__init__(kwargs)

        self_.type = type
