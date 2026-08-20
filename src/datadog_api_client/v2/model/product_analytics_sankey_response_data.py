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
    from datadog_api_client.v2.model.product_analytics_sankey_response_attributes import (
        ProductAnalyticsSankeyResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_sankey_response_type import ProductAnalyticsSankeyResponseType


class ProductAnalyticsSankeyResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_response_attributes import (
            ProductAnalyticsSankeyResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_sankey_response_type import (
            ProductAnalyticsSankeyResponseType,
        )

        return {
            "attributes": (ProductAnalyticsSankeyResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsSankeyResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsSankeyResponseAttributes,
        id: str,
        type: ProductAnalyticsSankeyResponseType,
        **kwargs,
    ):
        """
        The single JSON:API resource holding a computed Sankey diagram. Its attributes contain the
        nodes of every column and the links that carry sessions between them.

        :param attributes: Attributes of a Sankey response, containing the nodes and the links between them.
        :type attributes: ProductAnalyticsSankeyResponseAttributes

        :param id: Unique identifier for this response data object.
        :type id: str

        :param type: The resource type identifier for a Sankey response.
        :type type: ProductAnalyticsSankeyResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
