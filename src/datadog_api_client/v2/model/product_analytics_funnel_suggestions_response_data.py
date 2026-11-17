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
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_response_attributes import (
        ProductAnalyticsFunnelSuggestionsResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_response_type import (
        ProductAnalyticsFunnelSuggestionsResponseType,
    )


class ProductAnalyticsFunnelSuggestionsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_response_attributes import (
            ProductAnalyticsFunnelSuggestionsResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_response_type import (
            ProductAnalyticsFunnelSuggestionsResponseType,
        )

        return {
            "attributes": (ProductAnalyticsFunnelSuggestionsResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsFunnelSuggestionsResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ProductAnalyticsFunnelSuggestionsResponseAttributes,
        id: str,
        type: ProductAnalyticsFunnelSuggestionsResponseType,
        **kwargs,
    ):
        """
        Data of a feature suggestions response.

        :param attributes: Attributes of a feature suggestions response.
        :type attributes: ProductAnalyticsFunnelSuggestionsResponseAttributes

        :param id: ID of the response.
        :type id: str

        :param type: Type of a feature suggestions response.
        :type type: ProductAnalyticsFunnelSuggestionsResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
