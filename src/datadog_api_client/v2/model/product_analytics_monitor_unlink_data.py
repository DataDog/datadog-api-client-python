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
    from datadog_api_client.v2.model.product_analytics_monitor_unlink_attributes import (
        ProductAnalyticsMonitorUnlinkAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_monitor_unlink_request_type import (
        ProductAnalyticsMonitorUnlinkRequestType,
    )


class ProductAnalyticsMonitorUnlinkData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_unlink_attributes import (
            ProductAnalyticsMonitorUnlinkAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_monitor_unlink_request_type import (
            ProductAnalyticsMonitorUnlinkRequestType,
        )

        return {
            "attributes": (ProductAnalyticsMonitorUnlinkAttributes,),
            "type": (ProductAnalyticsMonitorUnlinkRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsMonitorUnlinkAttributes,
        type: ProductAnalyticsMonitorUnlinkRequestType,
        **kwargs,
    ):
        """
        Data of the Product Analytics monitor unlink request.

        :param attributes: The chart link to remove. It must match the stored link exactly:
            ``chart_id`` alone for a saved chart, or ``chart_id`` and ``dashboard_id`` for a dashboard widget.
        :type attributes: ProductAnalyticsMonitorUnlinkAttributes

        :param type: Product Analytics monitor unlink request resource type.
        :type type: ProductAnalyticsMonitorUnlinkRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
