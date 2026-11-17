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
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_data import (
        ProductAnalyticsJourneyDropOffResponseData,
    )


class ProductAnalyticsJourneyDropOffResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_response_data import (
            ProductAnalyticsJourneyDropOffResponseData,
        )

        return {
            "data": (ProductAnalyticsJourneyDropOffResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyDropOffResponseData, **kwargs):
        """
        Response for a journey drop-off analysis.

        :param data: The journey drop-off analysis results.
        :type data: ProductAnalyticsJourneyDropOffResponseData
        """
        super().__init__(kwargs)

        self_.data = data
