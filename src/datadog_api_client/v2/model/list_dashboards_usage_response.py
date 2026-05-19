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
    from datadog_api_client.v2.model.dashboard_usage import DashboardUsage
    from datadog_api_client.v2.model.list_dashboards_usage_response_links import ListDashboardsUsageResponseLinks
    from datadog_api_client.v2.model.list_dashboards_usage_response_meta import ListDashboardsUsageResponseMeta


class ListDashboardsUsageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_usage import DashboardUsage
        from datadog_api_client.v2.model.list_dashboards_usage_response_links import ListDashboardsUsageResponseLinks
        from datadog_api_client.v2.model.list_dashboards_usage_response_meta import ListDashboardsUsageResponseMeta

        return {
            "data": ([DashboardUsage],),
            "links": (ListDashboardsUsageResponseLinks,),
            "meta": (ListDashboardsUsageResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[DashboardUsage],
        meta: ListDashboardsUsageResponseMeta,
        links: Union[ListDashboardsUsageResponseLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Paginated list of dashboard usage records.

        :param data: Dashboard usage records, one per dashboard in the caller's organization.
        :type data: [DashboardUsage]

        :param links: Pagination links for a list of dashboard usage records.
        :type links: ListDashboardsUsageResponseLinks, optional

        :param meta: Pagination metadata for a list of dashboard usage records.
        :type meta: ListDashboardsUsageResponseMeta
        """
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
