# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamRoutingRulesDataRelationshipsRulesDataItemsType(ModelSimple):
    """
    Indicates that the resource is of type 'team_routing_rules'.

    :param value: If omitted defaults to "team_routing_rules". Must be one of ["team_routing_rules"].
    :type value: str
    """

    allowed_values = {
        "team_routing_rules",
    }
    TEAM_ROUTING_RULES: ClassVar["TeamRoutingRulesDataRelationshipsRulesDataItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamRoutingRulesDataRelationshipsRulesDataItemsType.TEAM_ROUTING_RULES = (
    TeamRoutingRulesDataRelationshipsRulesDataItemsType("team_routing_rules")
)
