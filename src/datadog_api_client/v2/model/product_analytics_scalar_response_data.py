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
    from datadog_api_client.v2.model.product_analytics_scalar_response_attributes import (
        ProductAnalyticsScalarResponseAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_scalar_response_type import ProductAnalyticsScalarResponseType


class ProductAnalyticsScalarResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_scalar_response_attributes import (
            ProductAnalyticsScalarResponseAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_scalar_response_type import (
            ProductAnalyticsScalarResponseType,
        )

        return {
            "attributes": (ProductAnalyticsScalarResponseAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsScalarResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ProductAnalyticsScalarResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ProductAnalyticsScalarResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a scalar response.

        :param attributes:
        :type attributes: ProductAnalyticsScalarResponseAttributes, optional

        :param id:
        :type id: str, optional

        :param type:
        :type type: ProductAnalyticsScalarResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
