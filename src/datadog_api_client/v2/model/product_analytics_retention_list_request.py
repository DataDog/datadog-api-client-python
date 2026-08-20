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
    from datadog_api_client.v2.model.product_analytics_retention_list_request_data import (
        ProductAnalyticsRetentionListRequestData,
    )


class ProductAnalyticsRetentionListRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_request_data import (
            ProductAnalyticsRetentionListRequestData,
        )

        return {
            "data": (ProductAnalyticsRetentionListRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsRetentionListRequestData, **kwargs):
        """
        Request body listing the individual entities behind one cell of the retention grid.

        :param data: The single JSON:API resource carrying a retention list query. Its attributes hold the time
            window, the cell to list, and the columns to return for each entity.
        :type data: ProductAnalyticsRetentionListRequestData
        """
        super().__init__(kwargs)

        self_.data = data
