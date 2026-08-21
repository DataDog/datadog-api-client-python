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
    from datadog_api_client.v2.model.product_analytics_journey_list_request_data import (
        ProductAnalyticsJourneyListRequestData,
    )


class ProductAnalyticsJourneyListRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_list_request_data import (
            ProductAnalyticsJourneyListRequestData,
        )

        return {
            "data": (ProductAnalyticsJourneyListRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyListRequestData, **kwargs):
        """
        Request body for a journey list query.

        :param data: The single JSON:API resource carrying a journey list query. Its attributes hold the time window
            and the journey whose matching entities should be listed, one row each.
        :type data: ProductAnalyticsJourneyListRequestData
        """
        super().__init__(kwargs)

        self_.data = data
