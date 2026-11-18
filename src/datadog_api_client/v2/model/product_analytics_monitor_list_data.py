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
    from datadog_api_client.v2.model.product_analytics_monitor_list_attributes import (
        ProductAnalyticsMonitorListAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_monitor_list_type import ProductAnalyticsMonitorListType


class ProductAnalyticsMonitorListData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_list_attributes import (
            ProductAnalyticsMonitorListAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_monitor_list_type import ProductAnalyticsMonitorListType

        return {
            "attributes": (ProductAnalyticsMonitorListAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsMonitorListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsMonitorListAttributes,
        id: str,
        type: ProductAnalyticsMonitorListType,
        **kwargs,
    ):
        """
        Data of a Product Analytics monitor list.

        :param attributes: A list of Product Analytics monitors.
        :type attributes: ProductAnalyticsMonitorListAttributes

        :param id: ID of the list resource. Always ``list``.
        :type id: str

        :param type: Product Analytics monitor list resource type.
        :type type: ProductAnalyticsMonitorListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
