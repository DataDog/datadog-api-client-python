# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomTopologyMapProjectionType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "custom_topology_map_node". Must be one of ["custom_topology_map_node"].
    :type value: str
    """

    allowed_values = {
        "custom_topology_map_node",
    }
    CUSTOM_TOPOLOGY_MAP_NODE: ClassVar["CustomTopologyMapProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomTopologyMapProjectionType.CUSTOM_TOPOLOGY_MAP_NODE = CustomTopologyMapProjectionType("custom_topology_map_node")
