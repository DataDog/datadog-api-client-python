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
    from datadog_api_client.v2.model.sankey_response_data_attributes_links_items import (
        SankeyResponseDataAttributesLinksItems,
    )
    from datadog_api_client.v2.model.sankey_response_data_attributes_nodes_items import (
        SankeyResponseDataAttributesNodesItems,
    )


class SankeyResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sankey_response_data_attributes_links_items import (
            SankeyResponseDataAttributesLinksItems,
        )
        from datadog_api_client.v2.model.sankey_response_data_attributes_nodes_items import (
            SankeyResponseDataAttributesNodesItems,
        )

        return {
            "links": ([SankeyResponseDataAttributesLinksItems],),
            "nodes": ([SankeyResponseDataAttributesNodesItems],),
        }

    attribute_map = {
        "links": "links",
        "nodes": "nodes",
    }

    def __init__(
        self_,
        links: Union[List[SankeyResponseDataAttributesLinksItems], UnsetType] = unset,
        nodes: Union[List[SankeyResponseDataAttributesNodesItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param links:
        :type links: [SankeyResponseDataAttributesLinksItems], optional

        :param nodes:
        :type nodes: [SankeyResponseDataAttributesNodesItems], optional
        """
        if links is not unset:
            kwargs["links"] = links
        if nodes is not unset:
            kwargs["nodes"] = nodes
        super().__init__(kwargs)
