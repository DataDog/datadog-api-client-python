# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ProductAnalyticsRetentionTimeInterval(ModelComposed):
    def __init__(self, **kwargs):
        """
        A retention interval, either aligned to calendar boundaries or of a fixed length.
        Cohort criteria use calendar intervals; return criteria use fixed intervals.

        :param type: The discriminator identifying a calendar-aligned retention interval.
        :type type: ProductAnalyticsRetentionCalendarTimeIntervalType

        :param value: A calendar-aligned bucket definition, such as "every 1 week starting on Monday".
        :type value: ProductAnalyticsCalendarInterval

        :param unit: Time unit for a fixed-length retention interval.
        :type unit: ProductAnalyticsRetentionFixedTimeIntervalUnit
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.product_analytics_retention_calendar_time_interval import (
            ProductAnalyticsRetentionCalendarTimeInterval,
        )
        from datadog_api_client.v2.model.product_analytics_retention_fixed_time_interval import (
            ProductAnalyticsRetentionFixedTimeInterval,
        )

        return {
            "oneOf": [
                ProductAnalyticsRetentionCalendarTimeInterval,
                ProductAnalyticsRetentionFixedTimeInterval,
            ],
        }
