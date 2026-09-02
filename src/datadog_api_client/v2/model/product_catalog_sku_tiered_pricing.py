# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_catalog_sku_pricing_tier import ProductCatalogSKUPricingTier


class ProductCatalogSKUTieredPricing(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_catalog_sku_pricing_tier import ProductCatalogSKUPricingTier

        return {
            "tiers": ([ProductCatalogSKUPricingTier],),
        }

    attribute_map = {
        "tiers": "tiers",
    }

    def __init__(self_, tiers: List[ProductCatalogSKUPricingTier], **kwargs):
        """
        The tiered pricing applied to on-demand usage of the SKU. ``null`` when the SKU is priced
        with a single list price instead.

        :param tiers: The pricing tiers, ordered by ascending usage quantity.
        :type tiers: [ProductCatalogSKUPricingTier]
        """
        super().__init__(kwargs)

        self_.tiers = tiers
