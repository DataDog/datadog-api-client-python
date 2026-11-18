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
    from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_data import (
        ProductAnalyticsJourneyDropOffRequestData,
    )


class ProductAnalyticsJourneyDropOffRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_drop_off_request_data import (
            ProductAnalyticsJourneyDropOffRequestData,
        )

        return {
            "data": (ProductAnalyticsJourneyDropOffRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyDropOffRequestData, **kwargs):
        """
        Request body for a journey drop-off analysis.

        :param data: The definition of a journey drop-off analysis request body.
        :type data: ProductAnalyticsJourneyDropOffRequestData
        """
        super().__init__(kwargs)

        self_.data = data
