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
    from datadog_api_client.v2.model.product_analytics_formula_journey_request_data import (
        ProductAnalyticsFormulaJourneyRequestData,
    )


class ProductAnalyticsFormulaJourneyRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_formula_journey_request_data import (
            ProductAnalyticsFormulaJourneyRequestData,
        )

        return {
            "data": (ProductAnalyticsFormulaJourneyRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsFormulaJourneyRequestData, **kwargs):
        """
        Request body for a journey timeseries query.

        :param data: The single JSON:API resource carrying a journey timeseries query. Its attributes hold the time
            window, the bucket interval that splits it, and the journey metric to compute per bucket.
        :type data: ProductAnalyticsFormulaJourneyRequestData
        """
        super().__init__(kwargs)

        self_.data = data
