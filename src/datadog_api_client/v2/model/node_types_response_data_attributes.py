# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.node_type import NodeType


class NodeTypesResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.node_type import NodeType

        return {
            "node_types": ([NodeType],),
        }

    attribute_map = {
        "node_types": "node_types",
    }

    def __init__(self_, node_types: List[NodeType], **kwargs):
        """
        The attributes of the node types response, containing the list of node type definitions for the requested language.

        :param node_types: The list of tree-sitter node type definitions for the language.
        :type node_types: [NodeType]
        """
        super().__init__(kwargs)

        self_.node_types = node_types
