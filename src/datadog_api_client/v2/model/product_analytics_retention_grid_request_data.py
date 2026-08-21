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
    from datadog_api_client.v2.model.product_analytics_retention_grid_request_attributes import (
        ProductAnalyticsRetentionGridRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_retention_grid_request_type import (
        ProductAnalyticsRetentionGridRequestType,
    )


class ProductAnalyticsRetentionGridRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_request_attributes import (
            ProductAnalyticsRetentionGridRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_retention_grid_request_type import (
            ProductAnalyticsRetentionGridRequestType,
        )

        return {
            "attributes": (ProductAnalyticsRetentionGridRequestAttributes,),
            "type": (ProductAnalyticsRetentionGridRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsRetentionGridRequestAttributes,
        type: ProductAnalyticsRetentionGridRequestType,
        **kwargs,
    ):
        """
        The single JSON:API resource carrying a retention grid query. Its attributes hold the time
        window to query and the cohort and return criteria that define the grid.

        :param attributes: Attributes of a retention grid request.
        :type attributes: ProductAnalyticsRetentionGridRequestAttributes

        :param type: The resource type identifier for a retention grid request.
        :type type: ProductAnalyticsRetentionGridRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
