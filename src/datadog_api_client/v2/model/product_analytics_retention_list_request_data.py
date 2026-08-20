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
    from datadog_api_client.v2.model.product_analytics_retention_list_request_attributes import (
        ProductAnalyticsRetentionListRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_retention_list_request_type import (
        ProductAnalyticsRetentionListRequestType,
    )


class ProductAnalyticsRetentionListRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_request_attributes import (
            ProductAnalyticsRetentionListRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_retention_list_request_type import (
            ProductAnalyticsRetentionListRequestType,
        )

        return {
            "attributes": (ProductAnalyticsRetentionListRequestAttributes,),
            "type": (ProductAnalyticsRetentionListRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsRetentionListRequestAttributes,
        type: ProductAnalyticsRetentionListRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a retention list query. Its attributes hold the time
        window, the cell to list, and the columns to return for each entity.

        :param attributes: Attributes of a retention list request.
        :type attributes: ProductAnalyticsRetentionListRequestAttributes

        :param type: The resource type identifier for a retention list request.
        :type type: ProductAnalyticsRetentionListRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
