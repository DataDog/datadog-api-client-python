# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AgentHealthAgentType(ModelSimple):
    """
    Agent type associated with the resource.

    :param value: If omitted defaults to "node". Must be one of ["node", "cluster"].
    :type value: str
    """

    allowed_values = {
        "node",
        "cluster",
    }
    NODE: ClassVar["AgentHealthAgentType"]
    CLUSTER: ClassVar["AgentHealthAgentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AgentHealthAgentType.NODE = AgentHealthAgentType("node")
AgentHealthAgentType.CLUSTER = AgentHealthAgentType("cluster")
