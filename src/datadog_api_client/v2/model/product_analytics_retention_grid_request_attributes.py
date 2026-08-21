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
    from datadog_api_client.v2.model.product_analytics_retention_grid_query import ProductAnalyticsRetentionGridQuery


class ProductAnalyticsRetentionGridRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_query import (
            ProductAnalyticsRetentionGridQuery,
        )

        return {
            "exclude_anonymous_traffic": (bool,),
            "_from": (int,),
            "query": (ProductAnalyticsRetentionGridQuery,),
            "to": (int,),
        }

    attribute_map = {
        "exclude_anonymous_traffic": "exclude_anonymous_traffic",
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_,
        _from: int,
        query: ProductAnalyticsRetentionGridQuery,
        to: int,
        exclude_anonymous_traffic: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a retention grid request.

        :param exclude_anonymous_traffic: Whether to exclude sessions that are not tied to an identified user.
        :type exclude_anonymous_traffic: bool, optional

        :param _from: Start of the query window, in epoch milliseconds.
        :type _from: int

        :param query: Query definition for a retention grid or retention metadata request.
        :type query: ProductAnalyticsRetentionGridQuery

        :param to: End of the query window, in epoch milliseconds.
        :type to: int
        """
        if exclude_anonymous_traffic is not unset:
            kwargs["exclude_anonymous_traffic"] = exclude_anonymous_traffic
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
