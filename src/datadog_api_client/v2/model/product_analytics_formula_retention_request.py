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
    from datadog_api_client.v2.model.product_analytics_formula_retention_request_data import (
        ProductAnalyticsFormulaRetentionRequestData,
    )


class ProductAnalyticsFormulaRetentionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_formula_retention_request_data import (
            ProductAnalyticsFormulaRetentionRequestData,
        )

        return {
            "data": (ProductAnalyticsFormulaRetentionRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsFormulaRetentionRequestData, **kwargs):
        """
        Request body for a retention scalar or retention timeseries query.

        :param data: The single JSON:API resource carrying a retention scalar or timeseries query. Its attributes
            hold the time window to query and the retention query definition to evaluate.
        :type data: ProductAnalyticsFormulaRetentionRequestData
        """
        super().__init__(kwargs)

        self_.data = data
