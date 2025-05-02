# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamRoutingRulesRequestDataType(ModelSimple):
    """
    Team routing rules resource type.

    :param value: If omitted defaults to "team_routing_rules". Must be one of ["team_routing_rules"].
    :type value: str
    """

    allowed_values = {
        "team_routing_rules",
    }
    TEAM_ROUTING_RULES: ClassVar["TeamRoutingRulesRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamRoutingRulesRequestDataType.TEAM_ROUTING_RULES = TeamRoutingRulesRequestDataType("team_routing_rules")
