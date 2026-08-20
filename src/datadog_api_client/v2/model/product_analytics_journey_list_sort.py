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
    from datadog_api_client.v2.model.query_sort_order import QuerySortOrder


class ProductAnalyticsJourneyListSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_sort_order import QuerySortOrder

        return {
            "facet": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "facet": "facet",
        "order": "order",
    }

    def __init__(
        self_, facet: Union[str, UnsetType] = unset, order: Union[QuerySortOrder, UnsetType] = unset, **kwargs
    ):
        """
        Sort configuration for the returned rows. The sort is applied only when ``facet``
        is one of the returned columns; otherwise it is ignored.

        :param facet: Column to sort on.
        :type facet: str, optional

        :param order: Direction of sort.
        :type order: QuerySortOrder, optional
        """
        if facet is not unset:
            kwargs["facet"] = facet
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)
