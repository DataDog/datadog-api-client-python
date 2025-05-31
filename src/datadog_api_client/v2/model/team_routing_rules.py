# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_routing_rules_data import TeamRoutingRulesData
    from datadog_api_client.v2.model.team_routing_rules_included import TeamRoutingRulesIncluded
    from datadog_api_client.v2.model.routing_rule import RoutingRule


class TeamRoutingRules(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_data import TeamRoutingRulesData
        from datadog_api_client.v2.model.team_routing_rules_included import TeamRoutingRulesIncluded

        return {
            "data": (TeamRoutingRulesData,),
            "included": ([TeamRoutingRulesIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[TeamRoutingRulesData, UnsetType] = unset,
        included: Union[List[Union[TeamRoutingRulesIncluded, RoutingRule]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a complete set of team routing rules, including data and optionally included related resources.

        :param data: Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type.
        :type data: TeamRoutingRulesData, optional

        :param included: Provides related routing rules or other included resources.
        :type included: [TeamRoutingRulesIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
