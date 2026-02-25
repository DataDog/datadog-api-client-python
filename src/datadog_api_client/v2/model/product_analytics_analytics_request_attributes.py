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
    from datadog_api_client.v2.model.product_analytics_execution_type import ProductAnalyticsExecutionType
    from datadog_api_client.v2.model.product_analytics_analytics_query import ProductAnalyticsAnalyticsQuery


class ProductAnalyticsAnalyticsRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_execution_type import ProductAnalyticsExecutionType
        from datadog_api_client.v2.model.product_analytics_analytics_query import ProductAnalyticsAnalyticsQuery

        return {
            "enforced_execution_type": (ProductAnalyticsExecutionType,),
            "_from": (int,),
            "query": (ProductAnalyticsAnalyticsQuery,),
            "request_id": (str,),
            "to": (int,),
        }

    attribute_map = {
        "enforced_execution_type": "enforced_execution_type",
        "_from": "from",
        "query": "query",
        "request_id": "request_id",
        "to": "to",
    }

    def __init__(
        self_,
        _from: int,
        query: ProductAnalyticsAnalyticsQuery,
        to: int,
        enforced_execution_type: Union[ProductAnalyticsExecutionType, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an analytics request.

        :param enforced_execution_type: Override the query execution strategy.
        :type enforced_execution_type: ProductAnalyticsExecutionType, optional

        :param _from: Start time in epoch milliseconds. Must be less than ``to``.
        :type _from: int

        :param query: The analytics query definition containing a base query, compute rule, and optional grouping.
        :type query: ProductAnalyticsAnalyticsQuery

        :param request_id: Optional request ID for multi-step query continuation.
        :type request_id: str, optional

        :param to: End time in epoch milliseconds.
        :type to: int
        """
        if enforced_execution_type is not unset:
            kwargs["enforced_execution_type"] = enforced_execution_type
        if request_id is not unset:
            kwargs["request_id"] = request_id
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
