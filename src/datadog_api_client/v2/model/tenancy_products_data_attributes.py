# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tenancy_products_data_attributes_products_items import (
        TenancyProductsDataAttributesProductsItems,
    )


class TenancyProductsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tenancy_products_data_attributes_products_items import (
            TenancyProductsDataAttributesProductsItems,
        )

        return {
            "products": ([TenancyProductsDataAttributesProductsItems],),
        }

    attribute_map = {
        "products": "products",
    }

    def __init__(self_, products: Union[List[TenancyProductsDataAttributesProductsItems], UnsetType] = unset, **kwargs):
        """


        :param products:
        :type products: [TenancyProductsDataAttributesProductsItems], optional
        """
        if products is not unset:
            kwargs["products"] = products
        super().__init__(kwargs)
