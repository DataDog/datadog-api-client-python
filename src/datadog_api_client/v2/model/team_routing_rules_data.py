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
    from datadog_api_client.v2.model.team_routing_rules_data_relationships import TeamRoutingRulesDataRelationships
    from datadog_api_client.v2.model.team_routing_rules_data_type import TeamRoutingRulesDataType


class TeamRoutingRulesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_data_relationships import TeamRoutingRulesDataRelationships
        from datadog_api_client.v2.model.team_routing_rules_data_type import TeamRoutingRulesDataType

        return {
            "id": (str,),
            "relationships": (TeamRoutingRulesDataRelationships,),
            "type": (TeamRoutingRulesDataType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: TeamRoutingRulesDataType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[TeamRoutingRulesDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type.

        :param id: Specifies the unique identifier of this team routing rules record.
        :type id: str, optional

        :param relationships: Specifies relationships for team routing rules, including rule references.
        :type relationships: TeamRoutingRulesDataRelationships, optional

        :param type: Team routing rules resource type.
        :type type: TeamRoutingRulesDataType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
