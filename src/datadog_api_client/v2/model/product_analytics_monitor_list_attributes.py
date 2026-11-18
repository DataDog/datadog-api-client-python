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
    from datadog_api_client.v2.model.product_analytics_monitor_list_item import ProductAnalyticsMonitorListItem


class ProductAnalyticsMonitorListAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_list_item import ProductAnalyticsMonitorListItem

        return {
            "monitors": ([ProductAnalyticsMonitorListItem],),
            "total": (int,),
        }

    attribute_map = {
        "monitors": "monitors",
        "total": "total",
    }

    def __init__(self_, monitors: List[ProductAnalyticsMonitorListItem], total: int, **kwargs):
        """
        A list of Product Analytics monitors.

        :param monitors: The monitors.
        :type monitors: [ProductAnalyticsMonitorListItem]

        :param total: Total number of monitors that match, across all pages.
        :type total: int
        """
        super().__init__(kwargs)

        self_.monitors = monitors
        self_.total = total
