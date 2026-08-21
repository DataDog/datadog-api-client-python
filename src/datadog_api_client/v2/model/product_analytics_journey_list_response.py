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
    from datadog_api_client.v2.model.product_analytics_journey_list_response_data import (
        ProductAnalyticsJourneyListResponseData,
    )


class ProductAnalyticsJourneyListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_list_response_data import (
            ProductAnalyticsJourneyListResponseData,
        )

        return {
            "data": (ProductAnalyticsJourneyListResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyListResponseData, **kwargs):
        """
        Response for a journey list query.

        :param data: The single JSON:API resource holding the entities matching a journey. Its attributes contain
            the returned rows and the total number of rows that matched, ignoring ``limit``.
        :type data: ProductAnalyticsJourneyListResponseData
        """
        super().__init__(kwargs)

        self_.data = data
