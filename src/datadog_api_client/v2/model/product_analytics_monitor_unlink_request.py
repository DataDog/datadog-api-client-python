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
    from datadog_api_client.v2.model.product_analytics_monitor_unlink_data import ProductAnalyticsMonitorUnlinkData


class ProductAnalyticsMonitorUnlinkRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_unlink_data import ProductAnalyticsMonitorUnlinkData

        return {
            "data": (ProductAnalyticsMonitorUnlinkData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsMonitorUnlinkData, **kwargs):
        """
        Request to unlink a Product Analytics monitor from its chart.

        :param data: Data of the Product Analytics monitor unlink request.
        :type data: ProductAnalyticsMonitorUnlinkData
        """
        super().__init__(kwargs)

        self_.data = data
