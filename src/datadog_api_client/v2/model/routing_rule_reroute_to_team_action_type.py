# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RoutingRuleRerouteToTeamActionType(ModelSimple):
    """
    Indicates that the action reroutes the page to another team's routing rules.

    :param value: If omitted defaults to "reroute_to_team". Must be one of ["reroute_to_team"].
    :type value: str
    """

    allowed_values = {
        "reroute_to_team",
    }
    REROUTE_TO_TEAM: ClassVar["RoutingRuleRerouteToTeamActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RoutingRuleRerouteToTeamActionType.REROUTE_TO_TEAM = RoutingRuleRerouteToTeamActionType("reroute_to_team")
