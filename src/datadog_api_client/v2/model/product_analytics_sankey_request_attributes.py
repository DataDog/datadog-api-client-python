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
    from datadog_api_client.v2.model.product_analytics_sankey_definition import ProductAnalyticsSankeyDefinition
    from datadog_api_client.v2.model.product_analytics_execution_type import ProductAnalyticsExecutionType
    from datadog_api_client.v2.model.product_analytics_sampling import ProductAnalyticsSampling
    from datadog_api_client.v2.model.product_analytics_sankey_search import ProductAnalyticsSankeySearch
    from datadog_api_client.v2.model.product_analytics_sankey_time import ProductAnalyticsSankeyTime


class ProductAnalyticsSankeyRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_definition import ProductAnalyticsSankeyDefinition
        from datadog_api_client.v2.model.product_analytics_execution_type import ProductAnalyticsExecutionType
        from datadog_api_client.v2.model.product_analytics_sampling import ProductAnalyticsSampling
        from datadog_api_client.v2.model.product_analytics_sankey_search import ProductAnalyticsSankeySearch
        from datadog_api_client.v2.model.product_analytics_sankey_time import ProductAnalyticsSankeyTime

        return {
            "data_source": (str,),
            "definition": (ProductAnalyticsSankeyDefinition,),
            "enforced_execution_type": (ProductAnalyticsExecutionType,),
            "request_id": (str,),
            "sampling": (ProductAnalyticsSampling,),
            "search": (ProductAnalyticsSankeySearch,),
            "time": (ProductAnalyticsSankeyTime,),
        }

    attribute_map = {
        "data_source": "data_source",
        "definition": "definition",
        "enforced_execution_type": "enforced_execution_type",
        "request_id": "request_id",
        "sampling": "sampling",
        "search": "search",
        "time": "time",
    }

    def __init__(
        self_,
        data_source: str,
        definition: ProductAnalyticsSankeyDefinition,
        search: ProductAnalyticsSankeySearch,
        time: ProductAnalyticsSankeyTime,
        enforced_execution_type: Union[ProductAnalyticsExecutionType, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        sampling: Union[ProductAnalyticsSampling, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a Sankey request.

        :param data_source: The data source for the Sankey query.
        :type data_source: str

        :param definition: Sankey visualization definition. Set either ``source`` or ``target`` , not both.
            Use ``source`` for forward flow (where do users go after this page?) or
            ``target`` for backward flow (where did users come from?).
        :type definition: ProductAnalyticsSankeyDefinition

        :param enforced_execution_type: Override the query execution strategy.
        :type enforced_execution_type: ProductAnalyticsExecutionType, optional

        :param request_id:
        :type request_id: str, optional

        :param sampling: Sampling configuration.
        :type sampling: ProductAnalyticsSampling, optional

        :param search: Search parameters for a Sankey query.
        :type search: ProductAnalyticsSankeySearch

        :param time: Time range for the Sankey query.
        :type time: ProductAnalyticsSankeyTime
        """
        if enforced_execution_type is not unset:
            kwargs["enforced_execution_type"] = enforced_execution_type
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if sampling is not unset:
            kwargs["sampling"] = sampling
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.definition = definition
        self_.search = search
        self_.time = time
