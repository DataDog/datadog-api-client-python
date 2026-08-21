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
    from datadog_api_client.v2.model.product_analytics_retention_list_response_data import (
        ProductAnalyticsRetentionListResponseData,
    )


class ProductAnalyticsRetentionListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_response_data import (
            ProductAnalyticsRetentionListResponseData,
        )

        return {
            "data": (ProductAnalyticsRetentionListResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsRetentionListResponseData, **kwargs):
        """
        Response for a retention list query.

        :param data: The single JSON:API resource holding the entities behind one retention cell. Its attributes
            contain the entity whose retention was measured and one row per matching entity.
        :type data: ProductAnalyticsRetentionListResponseData
        """
        super().__init__(kwargs)

        self_.data = data
