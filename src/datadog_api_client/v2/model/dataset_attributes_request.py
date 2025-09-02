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
    from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct


class DatasetAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

        return {
            "name": (str,),
            "principals": ([str],),
            "product_filters": ([FiltersPerProduct],),
        }

    attribute_map = {
        "name": "name",
        "principals": "principals",
        "product_filters": "product_filters",
    }

    def __init__(self_, name: str, principals: List[str], product_filters: List[FiltersPerProduct], **kwargs):
        """
        Dataset metadata and configurations.

        :param name: Name of the dataset.
        :type name: str

        :param principals: List of access principals, formatted as ``principal_type:id``. Principal can be 'team' or 'role'.
        :type principals: [str]

        :param product_filters: List of product-specific filters.
        :type product_filters: [FiltersPerProduct]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.principals = principals
        self_.product_filters = product_filters
