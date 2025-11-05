# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAgentVersionResourceType(ModelSimple):
    """
    The type of Agent version resource.

    :param value: If omitted defaults to "agent_version". Must be one of ["agent_version"].
    :type value: str
    """

    allowed_values = {
        "agent_version",
    }
    AGENT_VERSION: ClassVar["FleetAgentVersionResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAgentVersionResourceType.AGENT_VERSION = FleetAgentVersionResourceType("agent_version")
