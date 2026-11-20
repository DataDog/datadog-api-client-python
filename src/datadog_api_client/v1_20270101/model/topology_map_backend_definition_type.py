# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyMapBackendDefinitionType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "topology_map". Must be one of ["topology_map"].
    :type value: str
    """

    allowed_values = {
        "topology_map",
    }
    TOPOLOGY_MAP: ClassVar["TopologyMapBackendDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyMapBackendDefinitionType.TOPOLOGY_MAP = TopologyMapBackendDefinitionType("topology_map")
