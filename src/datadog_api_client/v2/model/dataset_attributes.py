# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct


class DatasetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

        return {
            "created_at": (datetime, none_type),
            "created_by": (UUID,),
            "name": (str,),
            "principals": ([str],),
            "product_filters": ([FiltersPerProduct],),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "name": "name",
        "principals": "principals",
        "product_filters": "product_filters",
    }

    def __init__(
        self_,
        name: str,
        principals: List[str],
        product_filters: List[FiltersPerProduct],
        created_at: Union[datetime, none_type, UnsetType] = unset,
        created_by: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dataset metadata and configuration(s).

        :param created_at: Timestamp when the dataset was created.
        :type created_at: datetime, none_type, optional

        :param created_by: Unique ID of the user who created the dataset.
        :type created_by: UUID, optional

        :param name: Name of the dataset.
        :type name: str

        :param principals: List of access principals, formatted as ``principal_type:id``. Principal can be 'team' or 'role'.
        :type principals: [str]

        :param product_filters: List of product-specific filters.
        :type product_filters: [FiltersPerProduct]
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        super().__init__(kwargs)

        self_.name = name
        self_.principals = principals
        self_.product_filters = product_filters
