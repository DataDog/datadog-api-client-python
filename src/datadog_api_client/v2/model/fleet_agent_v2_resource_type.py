# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAgentV2ResourceType(ModelSimple):
    """
    The type of the agent resource.

    :param value: If omitted defaults to "agent". Must be one of ["agent"].
    :type value: str
    """

    allowed_values = {
        "agent",
    }
    AGENT: ClassVar["FleetAgentV2ResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAgentV2ResourceType.AGENT = FleetAgentV2ResourceType("agent")
