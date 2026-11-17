# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_issue import ProductAnalyticsJourneyDropOffIssue


class ProductAnalyticsJourneyDropOffResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_issue import (
            ProductAnalyticsJourneyDropOffIssue,
        )

        return {
            "drop_off_count": (int,),
            "issues": ([ProductAnalyticsJourneyDropOffIssue],),
            "sessions_with_errors": (int,),
            "sessions_with_frustration_signals": (int,),
        }

    attribute_map = {
        "drop_off_count": "drop_off_count",
        "issues": "issues",
        "sessions_with_errors": "sessions_with_errors",
        "sessions_with_frustration_signals": "sessions_with_frustration_signals",
    }

    def __init__(
        self_,
        drop_off_count: int,
        issues: List[ProductAnalyticsJourneyDropOffIssue],
        sessions_with_errors: int,
        sessions_with_frustration_signals: int,
        **kwargs,
    ):
        """
        Attributes of a journey drop-off analysis response.

        :param drop_off_count: Number of sessions that reached the step before the target but not the target step.
        :type drop_off_count: int

        :param issues: The issues most associated with the drop-off.
        :type issues: [ProductAnalyticsJourneyDropOffIssue]

        :param sessions_with_errors: Number of dropped-off sessions that contained an error.
        :type sessions_with_errors: int

        :param sessions_with_frustration_signals: Number of dropped-off sessions that contained a frustration signal.
        :type sessions_with_frustration_signals: int
        """
        super().__init__(kwargs)

        self_.drop_off_count = drop_off_count
        self_.issues = issues
        self_.sessions_with_errors = sessions_with_errors
        self_.sessions_with_frustration_signals = sessions_with_frustration_signals
