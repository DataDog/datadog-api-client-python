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
    from datadog_api_client.v2.model.product_analytics_retention_grid_response_data import (
        ProductAnalyticsRetentionGridResponseData,
    )


class ProductAnalyticsRetentionGridResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_response_data import (
            ProductAnalyticsRetentionGridResponseData,
        )

        return {
            "data": (ProductAnalyticsRetentionGridResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsRetentionGridResponseData, **kwargs):
        """
        Response for a retention grid query.

        :param data: The single JSON:API resource holding a computed retention grid. Its attributes contain the
            return periods forming the columns and the cohorts forming the rows.
        :type data: ProductAnalyticsRetentionGridResponseData
        """
        super().__init__(kwargs)

        self_.data = data
