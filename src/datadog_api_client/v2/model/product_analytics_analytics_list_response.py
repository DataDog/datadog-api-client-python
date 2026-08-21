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
    from datadog_api_client.v2.model.product_analytics_analytics_list_response_data import (
        ProductAnalyticsAnalyticsListResponseData,
    )
    from datadog_api_client.v2.model.product_analytics_response_meta import ProductAnalyticsResponseMeta


class ProductAnalyticsAnalyticsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_response_data import (
            ProductAnalyticsAnalyticsListResponseData,
        )
        from datadog_api_client.v2.model.product_analytics_response_meta import ProductAnalyticsResponseMeta

        return {
            "data": (ProductAnalyticsAnalyticsListResponseData,),
            "meta": (ProductAnalyticsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: ProductAnalyticsAnalyticsListResponseData,
        meta: Union[ProductAnalyticsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for an analytics list query, containing individual event records.

        :param data: Data object for an analytics list response.
        :type data: ProductAnalyticsAnalyticsListResponseData

        :param meta: Metadata for a Product Analytics query response.
        :type meta: ProductAnalyticsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
