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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_request_data import (
        ProductAnalyticsJourneyFunnelRequestData,
    )


class ProductAnalyticsJourneyFunnelRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_funnel_request_data import (
            ProductAnalyticsJourneyFunnelRequestData,
        )

        return {
            "data": (ProductAnalyticsJourneyFunnelRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyFunnelRequestData, **kwargs):
        """
        Request body for a journey funnel analysis.

        :param data: The single JSON:API resource carrying a funnel query. Its attributes hold the time window to
            query and the journey whose step-to-step conversion should be measured.
        :type data: ProductAnalyticsJourneyFunnelRequestData
        """
        super().__init__(kwargs)

        self_.data = data
