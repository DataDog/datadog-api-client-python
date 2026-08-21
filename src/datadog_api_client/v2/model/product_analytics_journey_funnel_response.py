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
    from datadog_api_client.v2.model.product_analytics_journey_funnel_response_data import (
        ProductAnalyticsJourneyFunnelResponseData,
    )


class ProductAnalyticsJourneyFunnelResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_funnel_response_data import (
            ProductAnalyticsJourneyFunnelResponseData,
        )

        return {
            "data": (ProductAnalyticsJourneyFunnelResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyFunnelResponseData, **kwargs):
        """
        Response for a journey funnel analysis.

        :param data: The single JSON:API resource holding a computed funnel. Its attributes contain the number of
            entities that entered, the end-to-end conversion, and one entry per funnel step.
        :type data: ProductAnalyticsJourneyFunnelResponseData
        """
        super().__init__(kwargs)

        self_.data = data
