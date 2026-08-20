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
    from datadog_api_client.v2.model.product_analytics_analytics_list_response_attributes import (
        ProductAnalyticsAnalyticsListResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_analytics_list_response_type import (
        ProductAnalyticsAnalyticsListResponseType,
    )


class ProductAnalyticsAnalyticsListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_response_attributes import (
            ProductAnalyticsAnalyticsListResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_analytics_list_response_type import (
            ProductAnalyticsAnalyticsListResponseType,
        )

        return {
            "attributes": (ProductAnalyticsAnalyticsListResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsAnalyticsListResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsAnalyticsListResponseAttributes,
        id: str,
        type: ProductAnalyticsAnalyticsListResponseType,
        **kwargs,
    ):
        """
        Data object for an analytics list response.

        :param attributes: Attributes of an analytics list response, containing the matching event rows.
        :type attributes: ProductAnalyticsAnalyticsListResponseAttributes

        :param id: Unique identifier for this response data object.
        :type id: str

        :param type: The resource type identifier for an analytics list response.
        :type type: ProductAnalyticsAnalyticsListResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
