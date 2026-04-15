# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.funnel_comparison_duration import FunnelComparisonDuration
    from datadog_api_client.v1.model.product_analytics_funnel_query import ProductAnalyticsFunnelQuery
    from datadog_api_client.v1.model.product_analytics_funnel_request_type import ProductAnalyticsFunnelRequestType


class ProductAnalyticsFunnelRequest(ModelNormal):
    validations = {
        "comparison_segments": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.funnel_comparison_duration import FunnelComparisonDuration
        from datadog_api_client.v1.model.product_analytics_funnel_query import ProductAnalyticsFunnelQuery
        from datadog_api_client.v1.model.product_analytics_funnel_request_type import ProductAnalyticsFunnelRequestType

        return {
            "comparison_segments": ([str],),
            "comparison_time": (FunnelComparisonDuration,),
            "query": (ProductAnalyticsFunnelQuery,),
            "request_type": (ProductAnalyticsFunnelRequestType,),
        }

    attribute_map = {
        "comparison_segments": "comparison_segments",
        "comparison_time": "comparison_time",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        query: ProductAnalyticsFunnelQuery,
        request_type: ProductAnalyticsFunnelRequestType,
        comparison_segments: Union[List[str], UnsetType] = unset,
        comparison_time: Union[FunnelComparisonDuration, UnsetType] = unset,
        **kwargs,
    ):
        """
        User journey funnel widget request.

        :param comparison_segments: Comparison segments.
        :type comparison_segments: [str], optional

        :param comparison_time: Comparison time configuration for funnel widgets.
        :type comparison_time: FunnelComparisonDuration, optional

        :param query: User journey funnel query definition.
        :type query: ProductAnalyticsFunnelQuery

        :param request_type: Request type for user journey funnel widget.
        :type request_type: ProductAnalyticsFunnelRequestType
        """
        if comparison_segments is not unset:
            kwargs["comparison_segments"] = comparison_segments
        if comparison_time is not unset:
            kwargs["comparison_time"] = comparison_time
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
