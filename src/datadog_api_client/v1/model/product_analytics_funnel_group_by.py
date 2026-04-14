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
    from datadog_api_client.v1.model.product_analytics_funnel_group_by_sort import ProductAnalyticsFunnelGroupBySort
    from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget


class ProductAnalyticsFunnelGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_funnel_group_by_sort import ProductAnalyticsFunnelGroupBySort
        from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget

        return {
            "facet": (str,),
            "limit": (int,),
            "should_exclude_missing": (bool,),
            "sort": (ProductAnalyticsFunnelGroupBySort,),
            "target": (UserJourneySearchTarget,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "should_exclude_missing": "should_exclude_missing",
        "sort": "sort",
        "target": "target",
    }

    def __init__(
        self_,
        facet: str,
        limit: Union[int, UnsetType] = unset,
        should_exclude_missing: Union[bool, UnsetType] = unset,
        sort: Union[ProductAnalyticsFunnelGroupBySort, UnsetType] = unset,
        target: Union[UserJourneySearchTarget, UnsetType] = unset,
        **kwargs,
    ):
        """
        Group by configuration for user journey funnel.

        :param facet: Facet to group by.
        :type facet: str

        :param limit: Maximum number of groups.
        :type limit: int, optional

        :param should_exclude_missing: Whether to exclude missing values.
        :type should_exclude_missing: bool, optional

        :param sort: Sort configuration for user journey funnel group by.
        :type sort: ProductAnalyticsFunnelGroupBySort, optional

        :param target: Target for user journey search.
        :type target: UserJourneySearchTarget, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if should_exclude_missing is not unset:
            kwargs["should_exclude_missing"] = should_exclude_missing
        if sort is not unset:
            kwargs["sort"] = sort
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.facet = facet
