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
    from datadog_api_client.v2.model.product_analytics_launch_attributes import ProductAnalyticsLaunchAttributes
    from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType


class ProductAnalyticsLaunchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_attributes import ProductAnalyticsLaunchAttributes
        from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType

        return {
            "attributes": (ProductAnalyticsLaunchAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsLaunchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsLaunchAttributes, id: str, type: ProductAnalyticsLaunchType, **kwargs
    ):
        """
        A launch.

        :param attributes: Attributes of a launch.
        :type attributes: ProductAnalyticsLaunchAttributes

        :param id: UUID of the launch.
        :type id: str

        :param type: Launch resource type.
        :type type: ProductAnalyticsLaunchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
