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
    from datadog_api_client.v2.model.product_analytics_launch_property_finding import (
        ProductAnalyticsLaunchPropertyFinding,
    )
    from datadog_api_client.v2.model.product_analytics_launch_code_status import ProductAnalyticsLaunchCodeStatus


class ProductAnalyticsLaunchEventFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_property_finding import (
            ProductAnalyticsLaunchPropertyFinding,
        )
        from datadog_api_client.v2.model.product_analytics_launch_code_status import ProductAnalyticsLaunchCodeStatus

        return {
            "name": (str,),
            "properties": ([ProductAnalyticsLaunchPropertyFinding],),
            "status": (ProductAnalyticsLaunchCodeStatus,),
        }

    attribute_map = {
        "name": "name",
        "properties": "properties",
        "status": "status",
    }

    def __init__(
        self_,
        name: str,
        status: ProductAnalyticsLaunchCodeStatus,
        properties: Union[List[ProductAnalyticsLaunchPropertyFinding], UnsetType] = unset,
        **kwargs,
    ):
        """
        Code analysis result for an event of the tracking plan.

        :param name: Name of the event in the tracking plan.
        :type name: str

        :param properties: Results for the properties of the event. Only allowed when the event is ``found``.
        :type properties: [ProductAnalyticsLaunchPropertyFinding], optional

        :param status: Whether the inspected code sends the event, or attaches the property to the event.
        :type status: ProductAnalyticsLaunchCodeStatus
        """
        if properties is not unset:
            kwargs["properties"] = properties
        super().__init__(kwargs)

        self_.name = name
        self_.status = status
