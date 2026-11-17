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
    from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
    from datadog_api_client.v2.model.product_analytics_monitor_tags import ProductAnalyticsMonitorTags


class ProductAnalyticsMonitorUpdateAttributes(ModelNormal):
    validations = {
        "priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
        from datadog_api_client.v2.model.product_analytics_monitor_tags import ProductAnalyticsMonitorTags

        return {
            "message": (str,),
            "name": (str,),
            "options": (ProductAnalyticsMonitorOptions,),
            "priority": (int,),
            "query": (str,),
            "tags": (ProductAnalyticsMonitorTags,),
        }

    attribute_map = {
        "message": "message",
        "name": "name",
        "options": "options",
        "priority": "priority",
        "query": "query",
        "tags": "tags",
    }

    def __init__(
        self_,
        message: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        options: Union[ProductAnalyticsMonitorOptions, UnsetType] = unset,
        priority: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        tags: Union[ProductAnalyticsMonitorTags, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to update on a Product Analytics monitor. Fields that are not set are left unchanged.
        When set, ``options`` or ``tags`` replaces the stored value.

        :param message: Notification message sent when the monitor alerts.
        :type message: str, optional

        :param name: Name of the monitor.
        :type name: str, optional

        :param options: Options of a Product Analytics monitor.
        :type options: ProductAnalyticsMonitorOptions, optional

        :param priority: Priority of the monitor, from 1 (highest) to 5 (lowest).
        :type priority: int, optional

        :param query: Monitor query.
        :type query: str, optional

        :param tags: Monitor tags as key and value pairs. Each pair is stored as a ``key:value`` tag.
            ``chart_id`` and ``dashboard_id`` link the monitor to the chart it was created from. ``dashboard_id`` requires
            ``chart_id``.
        :type tags: ProductAnalyticsMonitorTags, optional
        """
        if message is not unset:
            kwargs["message"] = message
        if name is not unset:
            kwargs["name"] = name
        if options is not unset:
            kwargs["options"] = options
        if priority is not unset:
            kwargs["priority"] = priority
        if query is not unset:
            kwargs["query"] = query
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
