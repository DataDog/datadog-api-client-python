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
    from datadog_api_client.v2.model.product_analytics_journey_timeseries_response_data import (
        ProductAnalyticsJourneyTimeseriesResponseData,
    )


class ProductAnalyticsJourneyTimeseriesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_timeseries_response_data import (
            ProductAnalyticsJourneyTimeseriesResponseData,
        )

        return {
            "data": (ProductAnalyticsJourneyTimeseriesResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyTimeseriesResponseData, **kwargs):
        """
        Response for a journey timeseries query.

        :param data: The single JSON:API resource holding journey timeseries results. Its attributes contain one
            series per group along with the timestamps the points fall on.
        :type data: ProductAnalyticsJourneyTimeseriesResponseData
        """
        super().__init__(kwargs)

        self_.data = data
