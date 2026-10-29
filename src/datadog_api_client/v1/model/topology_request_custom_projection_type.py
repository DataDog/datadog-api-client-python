# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyRequestCustomProjectionType(ModelSimple):
    """
    Projection type. Each result row is a node.

    :param value: If omitted defaults to "custom_topology_map_node". Must be one of ["custom_topology_map_node"].
    :type value: str
    """

    allowed_values = {
        "custom_topology_map_node",
    }
    CUSTOM_TOPOLOGY_MAP_NODE: ClassVar["TopologyRequestCustomProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyRequestCustomProjectionType.CUSTOM_TOPOLOGY_MAP_NODE = TopologyRequestCustomProjectionType(
    "custom_topology_map_node"
)
