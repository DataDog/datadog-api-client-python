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
    from datadog_api_client.v2.model.product_analytics_scalar_response_data import ProductAnalyticsScalarResponseData
    from datadog_api_client.v2.model.product_analytics_response_meta import ProductAnalyticsResponseMeta


class ProductAnalyticsScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_scalar_response_data import (
            ProductAnalyticsScalarResponseData,
        )
        from datadog_api_client.v2.model.product_analytics_response_meta import ProductAnalyticsResponseMeta

        return {
            "data": (ProductAnalyticsScalarResponseData,),
            "meta": (ProductAnalyticsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[ProductAnalyticsScalarResponseData, UnsetType] = unset,
        meta: Union[ProductAnalyticsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a scalar analytics query.

        :param data: Data object for a scalar response.
        :type data: ProductAnalyticsScalarResponseData, optional

        :param meta: Metadata for a Product Analytics query response.
        :type meta: ProductAnalyticsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
