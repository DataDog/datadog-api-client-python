# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_monitor_attributes import ProductAnalyticsMonitorAttributes
    from datadog_api_client.v2.model.product_analytics_monitor_type import ProductAnalyticsMonitorType


class ProductAnalyticsMonitorData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_attributes import ProductAnalyticsMonitorAttributes
        from datadog_api_client.v2.model.product_analytics_monitor_type import ProductAnalyticsMonitorType

        return {
            "attributes": (ProductAnalyticsMonitorAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsMonitorType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsMonitorAttributes, id: str, type: ProductAnalyticsMonitorType, **kwargs
    ):
        """
        A Product Analytics monitor.

        :param attributes: Attributes of a Product Analytics monitor.
        :type attributes: ProductAnalyticsMonitorAttributes

        :param id: ID of the monitor.
        :type id: str

        :param type: Product Analytics monitor resource type.
        :type type: ProductAnalyticsMonitorType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
