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
    from datadog_api_client.v2.model.product_analytics_launch_request_attributes import (
        ProductAnalyticsLaunchRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType


class ProductAnalyticsLaunchCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_request_attributes import (
            ProductAnalyticsLaunchRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType

        return {
            "attributes": (ProductAnalyticsLaunchRequestAttributes,),
            "type": (ProductAnalyticsLaunchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsLaunchRequestAttributes, type: ProductAnalyticsLaunchType, **kwargs
    ):
        """
        Data of the launch to create.

        :param attributes: Attributes of a launch to create or replace.
        :type attributes: ProductAnalyticsLaunchRequestAttributes

        :param type: Launch resource type.
        :type type: ProductAnalyticsLaunchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
