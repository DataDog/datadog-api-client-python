# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_catalog_sku_allotment import ProductCatalogSKUAllotment
    from datadog_api_client.v2.model.product_catalog_sku_on_demand_option import ProductCatalogSKUOnDemandOption
    from datadog_api_client.v2.model.product_catalog_sku_tiered_pricing import ProductCatalogSKUTieredPricing
    from datadog_api_client.v2.model.product_catalog_sku_pricing_type import ProductCatalogSKUPricingType


class ProductCatalogSKUDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_catalog_sku_allotment import ProductCatalogSKUAllotment
        from datadog_api_client.v2.model.product_catalog_sku_on_demand_option import ProductCatalogSKUOnDemandOption
        from datadog_api_client.v2.model.product_catalog_sku_tiered_pricing import ProductCatalogSKUTieredPricing
        from datadog_api_client.v2.model.product_catalog_sku_pricing_type import ProductCatalogSKUPricingType

        return {
            "allotments": ([ProductCatalogSKUAllotment],),
            "billing_dimension": (str,),
            "billing_units": (str, none_type),
            "currency": (str,),
            "default_on_demand_option": (ProductCatalogSKUOnDemandOption,),
            "number_of_units_included_in_price": (int,),
            "on_demand_list_price": (str, none_type),
            "on_demand_tiered": (ProductCatalogSKUTieredPricing,),
            "pricing_type": (ProductCatalogSKUPricingType,),
            "sku_name": (str,),
        }

    attribute_map = {
        "allotments": "allotments",
        "billing_dimension": "billing_dimension",
        "billing_units": "billing_units",
        "currency": "currency",
        "default_on_demand_option": "default_on_demand_option",
        "number_of_units_included_in_price": "number_of_units_included_in_price",
        "on_demand_list_price": "on_demand_list_price",
        "on_demand_tiered": "on_demand_tiered",
        "pricing_type": "pricing_type",
        "sku_name": "sku_name",
    }

    def __init__(
        self_,
        allotments: List[ProductCatalogSKUAllotment],
        billing_dimension: str,
        billing_units: Union[str, none_type],
        currency: str,
        default_on_demand_option: ProductCatalogSKUOnDemandOption,
        number_of_units_included_in_price: int,
        on_demand_list_price: Union[str, none_type],
        on_demand_tiered: Union[ProductCatalogSKUTieredPricing, none_type],
        pricing_type: ProductCatalogSKUPricingType,
        sku_name: str,
        **kwargs,
    ):
        """
        The pricing and allotment metadata of a SKU.

        :param allotments: The allotments the SKU provides to other SKUs. Every entry carries the code of this
            SKU as its ``parent_sku_code``. Empty when the SKU provides no allotments.
        :type allotments: [ProductCatalogSKUAllotment]

        :param billing_dimension: The identifier of the billing dimension the SKU is billed on, as used by the usage
            metering endpoints. Several SKUs can share one billing dimension, so this value does
            not identify a SKU.
        :type billing_dimension: str

        :param billing_units: The billable usage unit the SKU is priced per. ``null`` for SKUs that are not priced
            per unit of usage, such as those whose ``pricing_type`` is ``percent``.
        :type billing_units: str, none_type

        :param currency: The ISO-4217 code of the currency the prices are expressed in.
        :type currency: str

        :param default_on_demand_option: The billing frequency applied to on-demand usage of the SKU by default.
        :type default_on_demand_option: ProductCatalogSKUOnDemandOption

        :param number_of_units_included_in_price: The number of billable usage units included in the price. ``0`` for SKUs that are not
            priced per unit of usage, such as those whose ``pricing_type`` is ``percent``.
        :type number_of_units_included_in_price: int

        :param on_demand_list_price: The public list price of on-demand usage of the SKU, as a decimal string. The number
            of decimal places is not normalized, so values such as ``0`` , ``0.9`` , and ``30000.00``
            all occur. ``null`` when the SKU is priced with tiers, in which case the prices are in
            ``on_demand_tiered``.
        :type on_demand_list_price: str, none_type

        :param on_demand_tiered: The tiered pricing applied to on-demand usage of the SKU. ``null`` when the SKU is priced
            with a single list price instead.
        :type on_demand_tiered: ProductCatalogSKUTieredPricing, none_type

        :param pricing_type: How the SKU is priced. ``usage`` prices each billable usage unit, and ``percent`` prices a
            percentage; percent-priced SKUs have no ``billing_units``.
        :type pricing_type: ProductCatalogSKUPricingType

        :param sku_name: The human-readable name of the SKU.
        :type sku_name: str
        """
        super().__init__(kwargs)

        self_.allotments = allotments
        self_.billing_dimension = billing_dimension
        self_.billing_units = billing_units
        self_.currency = currency
        self_.default_on_demand_option = default_on_demand_option
        self_.number_of_units_included_in_price = number_of_units_included_in_price
        self_.on_demand_list_price = on_demand_list_price
        self_.on_demand_tiered = on_demand_tiered
        self_.pricing_type = pricing_type
        self_.sku_name = sku_name
