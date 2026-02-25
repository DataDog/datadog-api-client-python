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
    from datadog_api_client.v2.model.product_analytics_sankey_link import ProductAnalyticsSankeyLink
    from datadog_api_client.v2.model.product_analytics_sankey_node import ProductAnalyticsSankeyNode


class ProductAnalyticsSankeyResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_sankey_link import ProductAnalyticsSankeyLink
        from datadog_api_client.v2.model.product_analytics_sankey_node import ProductAnalyticsSankeyNode

        return {
            "links": ([ProductAnalyticsSankeyLink],),
            "nodes": ([ProductAnalyticsSankeyNode],),
        }

    attribute_map = {
        "links": "links",
        "nodes": "nodes",
    }

    def __init__(
        self_,
        links: Union[List[ProductAnalyticsSankeyLink], UnsetType] = unset,
        nodes: Union[List[ProductAnalyticsSankeyNode], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param links: The links (flows) between nodes.
        :type links: [ProductAnalyticsSankeyLink], optional

        :param nodes: The nodes (pages) in the Sankey diagram.
        :type nodes: [ProductAnalyticsSankeyNode], optional
        """
        if links is not unset:
            kwargs["links"] = links
        if nodes is not unset:
            kwargs["nodes"] = nodes
        super().__init__(kwargs)
