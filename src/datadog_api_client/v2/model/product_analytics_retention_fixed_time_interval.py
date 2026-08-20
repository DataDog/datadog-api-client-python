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
    from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval_type import (
        ProductAnalyticsRetentionFixedTimeIntervalType,
    )
    from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval_unit import (
        ProductAnalyticsRetentionFixedTimeIntervalUnit,
    )


class ProductAnalyticsRetentionFixedTimeInterval(ModelNormal):
    validations = {
        "value": {
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval_type import (
            ProductAnalyticsRetentionFixedTimeIntervalType,
        )
        from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval_unit import (
            ProductAnalyticsRetentionFixedTimeIntervalUnit,
        )

        return {
            "type": (ProductAnalyticsRetentionFixedTimeIntervalType,),
            "unit": (ProductAnalyticsRetentionFixedTimeIntervalUnit,),
            "value": (float,),
        }

    attribute_map = {
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(
        self_,
        type: ProductAnalyticsRetentionFixedTimeIntervalType,
        unit: ProductAnalyticsRetentionFixedTimeIntervalUnit,
        value: float,
        **kwargs,
    ):
        """
        A retention interval of fixed length, such as "7 days".

        :param type: The discriminator identifying a fixed-length retention interval.
        :type type: ProductAnalyticsRetentionFixedTimeIntervalType

        :param unit: Time unit for a fixed-length retention interval.
        :type unit: ProductAnalyticsRetentionFixedTimeIntervalUnit

        :param value: Length of the interval, expressed in ``unit``.
        :type value: float
        """
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value
