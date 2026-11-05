# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_pricing_catalog_request_source_type import (
        AiGatewayModelPricingCatalogRequestSourceType,
    )


class AiGatewayModelPricingCatalogRequestSource(ModelNormal):
    validations = {
        "provider_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_pricing_catalog_request_source_type import (
            AiGatewayModelPricingCatalogRequestSourceType,
        )

        return {
            "provider_id": (str,),
            "type": (AiGatewayModelPricingCatalogRequestSourceType,),
        }

    attribute_map = {
        "provider_id": "provider_id",
        "type": "type",
    }

    def __init__(self_, provider_id: str, type: AiGatewayModelPricingCatalogRequestSourceType, **kwargs):
        """
        Source for a catalog pricing configuration.

        :param provider_id: Pricing catalog provider identifier.
        :type provider_id: str

        :param type: Catalog pricing source type.
        :type type: AiGatewayModelPricingCatalogRequestSourceType
        """
        super().__init__(kwargs)

        self_.provider_id = provider_id
        self_.type = type
