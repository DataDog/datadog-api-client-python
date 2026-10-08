# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.routing_rule_reroute_to_team_action_type import RoutingRuleRerouteToTeamActionType


class RoutingRuleRerouteToTeamAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_reroute_to_team_action_type import (
            RoutingRuleRerouteToTeamActionType,
        )

        return {
            "destination_team_id": (UUID,),
            "type": (RoutingRuleRerouteToTeamActionType,),
        }

    attribute_map = {
        "destination_team_id": "destination_team_id",
        "type": "type",
    }

    def __init__(self_, destination_team_id: UUID, type: RoutingRuleRerouteToTeamActionType, **kwargs):
        """
        Reroutes the page to another team, which then evaluates it against its own routing rules. Each routing rule can include this action only once. It can be combined only with ``send_slack_message`` and ``send_teams_message`` actions. It can't be used with ``escalation_policy`` or ``workflow`` actions, or when the routing rule sets ``policy_id``.

        :param destination_team_id: The ID of the team to reroute the page to.
        :type destination_team_id: UUID

        :param type: Indicates that the action reroutes the page to another team's routing rules.
        :type type: RoutingRuleRerouteToTeamActionType
        """
        super().__init__(kwargs)

        self_.destination_team_id = destination_team_id
        self_.type = type
