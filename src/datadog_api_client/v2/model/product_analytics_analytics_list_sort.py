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
    from datadog_api_client.v2.model.product_analytics_analytics_list_sort_order import (
        ProductAnalyticsAnalyticsListSortOrder,
    )


class ProductAnalyticsAnalyticsListSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_sort_order import (
            ProductAnalyticsAnalyticsListSortOrder,
        )

        return {
            "facet": (str,),
            "order": (ProductAnalyticsAnalyticsListSortOrder,),
        }

    attribute_map = {
        "facet": "facet",
        "order": "order",
    }

    def __init__(
        self_,
        facet: Union[str, UnsetType] = unset,
        order: Union[ProductAnalyticsAnalyticsListSortOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        The sort applied to the returned event rows.

        :param facet: Name of the facet to sort the rows by.
        :type facet: str, optional

        :param order: The direction rows are sorted in.
        :type order: ProductAnalyticsAnalyticsListSortOrder, optional
        """
        if facet is not unset:
            kwargs["facet"] = facet
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)
