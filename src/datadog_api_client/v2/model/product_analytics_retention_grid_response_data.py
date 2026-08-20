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
    from datadog_api_client.v2.model.product_analytics_retention_grid_response_attributes import (
        ProductAnalyticsRetentionGridResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_retention_grid_response_type import (
        ProductAnalyticsRetentionGridResponseType,
    )


class ProductAnalyticsRetentionGridResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_response_attributes import (
            ProductAnalyticsRetentionGridResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_retention_grid_response_type import (
            ProductAnalyticsRetentionGridResponseType,
        )

        return {
            "attributes": (ProductAnalyticsRetentionGridResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsRetentionGridResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsRetentionGridResponseAttributes,
        id: str,
        type: ProductAnalyticsRetentionGridResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding a computed retention grid. Its attributes contain the
        return periods forming the columns and the cohorts forming the rows.

        :param attributes: Attributes of a retention grid response, containing the cohort rows and the period columns.
        :type attributes: ProductAnalyticsRetentionGridResponseAttributes

        :param id: Unique identifier for this response data object.
        :type id: str

        :param type: The resource type identifier for a retention grid response.
        :type type: ProductAnalyticsRetentionGridResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
