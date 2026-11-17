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
    from datadog_api_client.v2.model.product_analytics_launch_data import ProductAnalyticsLaunchData


class ProductAnalyticsLaunchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_data import ProductAnalyticsLaunchData

        return {
            "data": (ProductAnalyticsLaunchData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsLaunchData, **kwargs):
        """
        Response containing a launch.

        :param data: A launch.
        :type data: ProductAnalyticsLaunchData
        """
        super().__init__(kwargs)

        self_.data = data
