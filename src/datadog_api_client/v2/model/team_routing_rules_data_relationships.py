# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules import (
        TeamRoutingRulesDataRelationshipsRules,
    )


class TeamRoutingRulesDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules import (
            TeamRoutingRulesDataRelationshipsRules,
        )

        return {
            "rules": (TeamRoutingRulesDataRelationshipsRules,),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: Union[TeamRoutingRulesDataRelationshipsRules, UnsetType] = unset, **kwargs):
        """
        Specifies relationships for team routing rules, including rule references.

        :param rules: Holds references to a set of routing rules in a relationship.
        :type rules: TeamRoutingRulesDataRelationshipsRules, optional
        """
        if rules is not unset:
            kwargs["rules"] = rules
        super().__init__(kwargs)
