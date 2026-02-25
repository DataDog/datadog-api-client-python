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
    from datadog_api_client.v2.model.product_analytics_sankey_request_attributes import (
        ProductAnalyticsSankeyRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_sankey_request_type import ProductAnalyticsSankeyRequestType


class ProductAnalyticsSankeyRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_request_attributes import (
            ProductAnalyticsSankeyRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_sankey_request_type import ProductAnalyticsSankeyRequestType

        return {
            "attributes": (ProductAnalyticsSankeyRequestAttributes,),
            "type": (ProductAnalyticsSankeyRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsSankeyRequestAttributes, type: ProductAnalyticsSankeyRequestType, **kwargs
    ):
        """


        :param attributes: Attributes for a Sankey request.
        :type attributes: ProductAnalyticsSankeyRequestAttributes

        :param type:
        :type type: ProductAnalyticsSankeyRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
