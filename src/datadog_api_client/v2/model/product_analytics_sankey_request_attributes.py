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
    from datadog_api_client.v2.model.product_analytics_sankey_definition import ProductAnalyticsSankeyDefinition
    from datadog_api_client.v2.model.product_analytics_sankey_search import ProductAnalyticsSankeySearch
    from datadog_api_client.v2.model.product_analytics_sankey_time import ProductAnalyticsSankeyTime


class ProductAnalyticsSankeyRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_definition import ProductAnalyticsSankeyDefinition
        from datadog_api_client.v2.model.product_analytics_sankey_search import ProductAnalyticsSankeySearch
        from datadog_api_client.v2.model.product_analytics_sankey_time import ProductAnalyticsSankeyTime

        return {
            "definition": (ProductAnalyticsSankeyDefinition,),
            "search": (ProductAnalyticsSankeySearch,),
            "time": (ProductAnalyticsSankeyTime,),
        }

    attribute_map = {
        "definition": "definition",
        "search": "search",
        "time": "time",
    }

    def __init__(
        self_,
        definition: ProductAnalyticsSankeyDefinition,
        search: ProductAnalyticsSankeySearch,
        time: ProductAnalyticsSankeyTime,
        **kwargs,
    ):
        """
        Attributes of a Sankey request.

        :param definition: The shape of the Sankey diagram, expressed as the facets to flow between and how many steps to show.
        :type definition: ProductAnalyticsSankeyDefinition

        :param search: Selects the sessions a Sankey diagram is built from.
        :type search: ProductAnalyticsSankeySearch

        :param time: The time window a Sankey query covers.
        :type time: ProductAnalyticsSankeyTime
        """
        super().__init__(kwargs)

        self_.definition = definition
        self_.search = search
        self_.time = time
