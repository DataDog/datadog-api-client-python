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
    from datadog_api_client.v1.model.product_analytics_funnel_compute import ProductAnalyticsFunnelCompute
    from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
    from datadog_api_client.v1.model.product_analytics_funnel_group_by import ProductAnalyticsFunnelGroupBy
    from datadog_api_client.v1.model.user_journey_search import UserJourneySearch


class ProductAnalyticsFunnelQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_funnel_compute import ProductAnalyticsFunnelCompute
        from datadog_api_client.v1.model.product_analytics_funnel_data_source import ProductAnalyticsFunnelDataSource
        from datadog_api_client.v1.model.product_analytics_funnel_group_by import ProductAnalyticsFunnelGroupBy
        from datadog_api_client.v1.model.user_journey_search import UserJourneySearch

        return {
            "compute": (ProductAnalyticsFunnelCompute,),
            "data_source": (ProductAnalyticsFunnelDataSource,),
            "group_by": ([ProductAnalyticsFunnelGroupBy],),
            "search": (UserJourneySearch,),
            "subquery_id": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "search": "search",
        "subquery_id": "subquery_id",
    }

    def __init__(
        self_,
        data_source: ProductAnalyticsFunnelDataSource,
        search: UserJourneySearch,
        compute: Union[ProductAnalyticsFunnelCompute, UnsetType] = unset,
        group_by: Union[List[ProductAnalyticsFunnelGroupBy], UnsetType] = unset,
        subquery_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        User journey funnel query definition.

        :param compute: Compute configuration for user journey funnel.
        :type compute: ProductAnalyticsFunnelCompute, optional

        :param data_source: Data source for user journey funnel queries.
        :type data_source: ProductAnalyticsFunnelDataSource

        :param group_by: Group by configuration.
        :type group_by: [ProductAnalyticsFunnelGroupBy], optional

        :param search: User journey search configuration.
        :type search: UserJourneySearch

        :param subquery_id: Subquery ID.
        :type subquery_id: str, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if subquery_id is not unset:
            kwargs["subquery_id"] = subquery_id
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.search = search
