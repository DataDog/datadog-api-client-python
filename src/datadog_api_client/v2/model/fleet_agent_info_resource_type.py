# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAgentInfoResourceType(ModelSimple):
    """
    The type of Agent info resource.

    :param value: If omitted defaults to "datadog_agent_key". Must be one of ["datadog_agent_key"].
    :type value: str
    """

    allowed_values = {
        "datadog_agent_key",
    }
    DATADOG_AGENT_KEY: ClassVar["FleetAgentInfoResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAgentInfoResourceType.DATADOG_AGENT_KEY = FleetAgentInfoResourceType("datadog_agent_key")
