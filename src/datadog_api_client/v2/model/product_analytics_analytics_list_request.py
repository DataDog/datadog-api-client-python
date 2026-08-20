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
    from datadog_api_client.v2.model.product_analytics_analytics_list_request_data import (
        ProductAnalyticsAnalyticsListRequestData,
    )


class ProductAnalyticsAnalyticsListRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_request_data import (
            ProductAnalyticsAnalyticsListRequestData,
        )

        return {
            "data": (ProductAnalyticsAnalyticsListRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ProductAnalyticsAnalyticsListRequestData, **kwargs):
        """
        Request for listing the individual event records matching an analytics query.

        :param data: Data object for an analytics list request.
        :type data: ProductAnalyticsAnalyticsListRequestData
        """
        super().__init__(kwargs)

        self_.data = data
