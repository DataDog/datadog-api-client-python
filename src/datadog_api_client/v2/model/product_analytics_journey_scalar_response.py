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
    from datadog_api_client.v2.model.product_analytics_journey_scalar_response_data import (
        ProductAnalyticsJourneyScalarResponseData,
    )


class ProductAnalyticsJourneyScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_scalar_response_data import (
            ProductAnalyticsJourneyScalarResponseData,
        )

        return {
            "data": (ProductAnalyticsJourneyScalarResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyScalarResponseData, **kwargs):
        """
        Response for a journey scalar query.

        :param data: The single JSON:API resource holding journey scalar results. Its attributes contain one value
            per group, suitable for a query value or top list widget.
        :type data: ProductAnalyticsJourneyScalarResponseData
        """
        super().__init__(kwargs)

        self_.data = data
