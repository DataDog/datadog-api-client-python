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
    from datadog_api_client.v2.model.product_catalog_sku_data_attributes_response import (
        ProductCatalogSKUDataAttributesResponse,
    )
    from datadog_api_client.v2.model.product_catalog_sku_type import ProductCatalogSKUType


class ProductCatalogSKUDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_catalog_sku_data_attributes_response import (
            ProductCatalogSKUDataAttributesResponse,
        )
        from datadog_api_client.v2.model.product_catalog_sku_type import ProductCatalogSKUType

        return {
            "attributes": (ProductCatalogSKUDataAttributesResponse,),
            "id": (str,),
            "type": (ProductCatalogSKUType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductCatalogSKUDataAttributesResponse, id: str, type: ProductCatalogSKUType, **kwargs
    ):
        """
        A SKU and the pricing metadata that applies to it.

        :param attributes: The pricing and allotment metadata of a SKU.
        :type attributes: ProductCatalogSKUDataAttributesResponse

        :param id: The code that identifies the SKU.
        :type id: str

        :param type: The SKU resource type.
        :type type: ProductCatalogSKUType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
