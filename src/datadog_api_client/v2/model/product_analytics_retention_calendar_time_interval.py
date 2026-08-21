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
    from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval_type import (
        ProductAnalyticsRetentionCalendarTimeIntervalType,
    )
    from datadog_api_client.v2.model.product_analytics_calendar_interval import ProductAnalyticsCalendarInterval


class ProductAnalyticsRetentionCalendarTimeInterval(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval_type import (
            ProductAnalyticsRetentionCalendarTimeIntervalType,
        )
        from datadog_api_client.v2.model.product_analytics_calendar_interval import ProductAnalyticsCalendarInterval

        return {
            "type": (ProductAnalyticsRetentionCalendarTimeIntervalType,),
            "value": (ProductAnalyticsCalendarInterval,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        type: ProductAnalyticsRetentionCalendarTimeIntervalType,
        value: ProductAnalyticsCalendarInterval,
        **kwargs,
    ):
        """
        A retention interval aligned to calendar boundaries.

        :param type: The discriminator identifying a calendar-aligned retention interval.
        :type type: ProductAnalyticsRetentionCalendarTimeIntervalType

        :param value: A calendar-aligned bucket definition, such as "every 1 week starting on Monday".
        :type value: ProductAnalyticsCalendarInterval
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
