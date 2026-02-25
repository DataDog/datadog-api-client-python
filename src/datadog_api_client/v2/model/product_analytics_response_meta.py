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
    from datadog_api_client.v2.model.product_analytics_response_meta_status import ProductAnalyticsResponseMetaStatus


class ProductAnalyticsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_response_meta_status import (
            ProductAnalyticsResponseMetaStatus,
        )

        return {
            "request_id": (str,),
            "status": (ProductAnalyticsResponseMetaStatus,),
        }

    attribute_map = {
        "request_id": "request_id",
        "status": "status",
    }

    def __init__(
        self_,
        request_id: Union[str, UnsetType] = unset,
        status: Union[ProductAnalyticsResponseMetaStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for a Product Analytics query response.

        :param request_id:
        :type request_id: str, optional

        :param status:
        :type status: ProductAnalyticsResponseMetaStatus, optional
        """
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
