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
    from datadog_api_client.v2.model.product_analytics_analytics_request_attributes import (
        ProductAnalyticsAnalyticsRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_analytics_request_type import (
        ProductAnalyticsAnalyticsRequestType,
    )


class ProductAnalyticsAnalyticsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_request_attributes import (
            ProductAnalyticsAnalyticsRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_analytics_request_type import (
            ProductAnalyticsAnalyticsRequestType,
        )

        return {
            "attributes": (ProductAnalyticsAnalyticsRequestAttributes,),
            "type": (ProductAnalyticsAnalyticsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsAnalyticsRequestAttributes,
        type: ProductAnalyticsAnalyticsRequestType,
        **kwargs,
    ):
        """
        Data object for an analytics request.

        :param attributes: Attributes for an analytics request.
        :type attributes: ProductAnalyticsAnalyticsRequestAttributes

        :param type: The resource type for analytics requests.
        :type type: ProductAnalyticsAnalyticsRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
