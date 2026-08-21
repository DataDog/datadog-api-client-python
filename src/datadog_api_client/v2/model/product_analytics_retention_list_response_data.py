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
    from datadog_api_client.v2.model.product_analytics_retention_list_response_attributes import (
        ProductAnalyticsRetentionListResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_retention_list_response_type import (
        ProductAnalyticsRetentionListResponseType,
    )


class ProductAnalyticsRetentionListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_response_attributes import (
            ProductAnalyticsRetentionListResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_retention_list_response_type import (
            ProductAnalyticsRetentionListResponseType,
        )

        return {
            "attributes": (ProductAnalyticsRetentionListResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsRetentionListResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsRetentionListResponseAttributes,
        id: str,
        type: ProductAnalyticsRetentionListResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding the entities behind one retention cell. Its attributes
        contain the entity whose retention was measured and one row per matching entity.

        :param attributes: Attributes of a retention list response, containing the matching entity rows.
        :type attributes: ProductAnalyticsRetentionListResponseAttributes

        :param id: Unique identifier for this response data object.
        :type id: str

        :param type: The resource type identifier for a retention list response.
        :type type: ProductAnalyticsRetentionListResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
