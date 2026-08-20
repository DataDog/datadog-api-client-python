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
    from datadog_api_client.v2.model.product_analytics_retention_grid_request_data import (
        ProductAnalyticsRetentionGridRequestData,
    )


class ProductAnalyticsRetentionGridRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_request_data import (
            ProductAnalyticsRetentionGridRequestData,
        )

        return {
            "data": (ProductAnalyticsRetentionGridRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsRetentionGridRequestData, **kwargs):
        """
        Request body for a retention grid query.

        :param data: The single JSON:API resource carrying a retention grid query. Its attributes hold the time
            window to query and the cohort and return criteria that define the grid.
        :type data: ProductAnalyticsRetentionGridRequestData
        """
        super().__init__(kwargs)

        self_.data = data
