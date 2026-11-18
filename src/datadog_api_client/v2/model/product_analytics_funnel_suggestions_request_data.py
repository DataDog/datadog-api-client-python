# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_attributes import (
        ProductAnalyticsFunnelSuggestionsRequestAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_type import (
        ProductAnalyticsFunnelSuggestionsRequestType,
    )


class ProductAnalyticsFunnelSuggestionsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_attributes import (
            ProductAnalyticsFunnelSuggestionsRequestAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_type import (
            ProductAnalyticsFunnelSuggestionsRequestType,
        )

        return {
            "attributes": (ProductAnalyticsFunnelSuggestionsRequestAttributes,),
            "type": (ProductAnalyticsFunnelSuggestionsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: ProductAnalyticsFunnelSuggestionsRequestType,
        attributes: Union[ProductAnalyticsFunnelSuggestionsRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of a feature suggestions request.

        :param attributes: Attributes of a feature suggestions request.
        :type attributes: ProductAnalyticsFunnelSuggestionsRequestAttributes, optional

        :param type: Type of a feature suggestions request.
        :type type: ProductAnalyticsFunnelSuggestionsRequestType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
