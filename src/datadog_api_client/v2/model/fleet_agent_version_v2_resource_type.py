# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAgentVersionV2ResourceType(ModelSimple):
    """
    The type of the agent version resource.

    :param value: If omitted defaults to "agent_version". Must be one of ["agent_version"].
    :type value: str
    """

    allowed_values = {
        "agent_version",
    }
    AGENT_VERSION: ClassVar["FleetAgentVersionV2ResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAgentVersionV2ResourceType.AGENT_VERSION = FleetAgentVersionV2ResourceType("agent_version")
