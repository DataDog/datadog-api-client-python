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
    from datadog_api_client.v2.model.product_analytics_monitor_update_attributes import (
        ProductAnalyticsMonitorUpdateAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_monitor_request_type import ProductAnalyticsMonitorRequestType


class ProductAnalyticsMonitorUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_update_attributes import (
            ProductAnalyticsMonitorUpdateAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_monitor_request_type import (
            ProductAnalyticsMonitorRequestType,
        )

        return {
            "attributes": (ProductAnalyticsMonitorUpdateAttributes,),
            "type": (ProductAnalyticsMonitorRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsMonitorUpdateAttributes, type: ProductAnalyticsMonitorRequestType, **kwargs
    ):
        """
        Data of the Product Analytics monitor update.

        :param attributes: Attributes to update on a Product Analytics monitor. Fields that are not set are left unchanged.
            When set, ``options`` or ``tags`` replaces the stored value.
        :type attributes: ProductAnalyticsMonitorUpdateAttributes

        :param type: Product Analytics monitor request resource type.
        :type type: ProductAnalyticsMonitorRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
