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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_monitor_creator import ProductAnalyticsMonitorCreator
    from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
    from datadog_api_client.v2.model.product_analytics_monitor_status import ProductAnalyticsMonitorStatus


class ProductAnalyticsMonitorAttributes(ModelNormal):
    validations = {
        "priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_creator import ProductAnalyticsMonitorCreator
        from datadog_api_client.v2.model.product_analytics_monitor_options import ProductAnalyticsMonitorOptions
        from datadog_api_client.v2.model.product_analytics_monitor_status import ProductAnalyticsMonitorStatus

        return {
            "created_time": (datetime,),
            "creator": (ProductAnalyticsMonitorCreator,),
            "message": (str,),
            "modified_time": (datetime,),
            "name": (str,),
            "options": (ProductAnalyticsMonitorOptions,),
            "org_id": (int,),
            "priority": (int,),
            "query": (str,),
            "status": (ProductAnalyticsMonitorStatus,),
            "tags": ([str], none_type),
        }

    attribute_map = {
        "created_time": "created_time",
        "creator": "creator",
        "message": "message",
        "modified_time": "modified_time",
        "name": "name",
        "options": "options",
        "org_id": "org_id",
        "priority": "priority",
        "query": "query",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        message: str,
        name: str,
        options: ProductAnalyticsMonitorOptions,
        org_id: int,
        query: str,
        status: ProductAnalyticsMonitorStatus,
        created_time: Union[datetime, UnsetType] = unset,
        creator: Union[ProductAnalyticsMonitorCreator, UnsetType] = unset,
        modified_time: Union[datetime, UnsetType] = unset,
        priority: Union[int, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Product Analytics monitor.

        :param created_time: Time the monitor was created.
        :type created_time: datetime, optional

        :param creator: The user who created the monitor.
        :type creator: ProductAnalyticsMonitorCreator, optional

        :param message: Notification message sent when the monitor alerts.
        :type message: str

        :param modified_time: Time the monitor was last modified.
        :type modified_time: datetime, optional

        :param name: Name of the monitor.
        :type name: str

        :param options: Options of a Product Analytics monitor.
        :type options: ProductAnalyticsMonitorOptions

        :param org_id: ID of the organization that owns the monitor.
        :type org_id: int

        :param priority: Priority of the monitor, from 1 (highest) to 5 (lowest).
        :type priority: int, optional

        :param query: Monitor query.
        :type query: str

        :param status: Current alert status of the monitor. ``No Data`` is returned when the monitor has not been evaluated yet.
        :type status: ProductAnalyticsMonitorStatus

        :param tags: Monitor tags, as ``key:value`` strings.
        :type tags: [str], none_type, optional
        """
        if created_time is not unset:
            kwargs["created_time"] = created_time
        if creator is not unset:
            kwargs["creator"] = creator
        if modified_time is not unset:
            kwargs["modified_time"] = modified_time
        if priority is not unset:
            kwargs["priority"] = priority
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.message = message
        self_.name = name
        self_.options = options
        self_.org_id = org_id
        self_.query = query
        self_.status = status
