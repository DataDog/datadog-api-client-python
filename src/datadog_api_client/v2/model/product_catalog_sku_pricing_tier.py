# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_catalog_sku_pricing_unit_type import ProductCatalogSKUPricingUnitType


class ProductCatalogSKUPricingTier(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_catalog_sku_pricing_unit_type import ProductCatalogSKUPricingUnitType

        return {
            "max_usage_quantity": (int, none_type),
            "min_usage_quantity": (int,),
            "price": (str,),
            "pricing_unit_type": (ProductCatalogSKUPricingUnitType,),
        }

    attribute_map = {
        "max_usage_quantity": "max_usage_quantity",
        "min_usage_quantity": "min_usage_quantity",
        "price": "price",
        "pricing_unit_type": "pricing_unit_type",
    }

    def __init__(
        self_,
        max_usage_quantity: Union[int, none_type],
        min_usage_quantity: int,
        price: str,
        pricing_unit_type: ProductCatalogSKUPricingUnitType,
        **kwargs,
    ):
        """
        A usage range and the price that applies to usage falling inside it.

        :param max_usage_quantity: The exclusive upper bound of the usage range the tier prices. ``null`` on the final
            tier, which is unbounded.
        :type max_usage_quantity: int, none_type

        :param min_usage_quantity: The inclusive lower bound of the usage range the tier prices.
        :type min_usage_quantity: int

        :param price: The price applied to usage in the tier, as a decimal string. The number of decimal
            places is not normalized, so free tiers appear as either ``0`` or ``0.00``.
        :type price: str

        :param pricing_unit_type: Whether the tier's price applies per unit of usage or to a block of usage.
        :type pricing_unit_type: ProductCatalogSKUPricingUnitType
        """
        super().__init__(kwargs)

        self_.max_usage_quantity = max_usage_quantity
        self_.min_usage_quantity = min_usage_quantity
        self_.price = price
        self_.pricing_unit_type = pricing_unit_type
