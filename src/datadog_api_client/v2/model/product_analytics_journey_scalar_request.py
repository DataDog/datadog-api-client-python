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
    from datadog_api_client.v2.model.product_analytics_journey_scalar_request_data import (
        ProductAnalyticsJourneyScalarRequestData,
    )


class ProductAnalyticsJourneyScalarRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_scalar_request_data import (
            ProductAnalyticsJourneyScalarRequestData,
        )

        return {
            "data": (ProductAnalyticsJourneyScalarRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsJourneyScalarRequestData, **kwargs):
        """
        Request body for a journey scalar query.

        :param data: The single JSON:API resource carrying a journey scalar query. Its attributes hold the time
            window and the journey metric to reduce to one value over that window.
        :type data: ProductAnalyticsJourneyScalarRequestData
        """
        super().__init__(kwargs)

        self_.data = data
