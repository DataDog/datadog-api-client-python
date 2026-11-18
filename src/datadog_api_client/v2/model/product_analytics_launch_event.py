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
    from datadog_api_client.v2.model.product_analytics_launch_event_property import ProductAnalyticsLaunchEventProperty


class ProductAnalyticsLaunchEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_event_property import (
            ProductAnalyticsLaunchEventProperty,
        )

        return {
            "description": (str,),
            "kpis": ([str],),
            "name": (str,),
            "properties": ([ProductAnalyticsLaunchEventProperty],),
            "trigger": (str,),
            "views": ([str],),
        }

    attribute_map = {
        "description": "description",
        "kpis": "kpis",
        "name": "name",
        "properties": "properties",
        "trigger": "trigger",
        "views": "views",
    }

    def __init__(
        self_,
        name: str,
        description: Union[str, UnsetType] = unset,
        kpis: Union[List[str], UnsetType] = unset,
        properties: Union[List[ProductAnalyticsLaunchEventProperty], UnsetType] = unset,
        trigger: Union[str, UnsetType] = unset,
        views: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        An event to instrument for the launch.

        :param description: What the event records.
        :type description: str, optional

        :param kpis: IDs of the launch KPIs that the event measures.
        :type kpis: [str], optional

        :param name: Name of the event, unique within the tracking plan.
        :type name: str

        :param properties: Properties that the event carries.
        :type properties: [ProductAnalyticsLaunchEventProperty], optional

        :param trigger: What causes the event to be sent.
        :type trigger: str, optional

        :param views: Views where the event is sent. Each value must be unique and not blank.
        :type views: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if kpis is not unset:
            kwargs["kpis"] = kpis
        if properties is not unset:
            kwargs["properties"] = properties
        if trigger is not unset:
            kwargs["trigger"] = trigger
        if views is not unset:
            kwargs["views"] = views
        super().__init__(kwargs)

        self_.name = name
