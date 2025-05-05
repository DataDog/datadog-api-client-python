# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules_data_items_type import (
        TeamRoutingRulesDataRelationshipsRulesDataItemsType,
    )


class TeamRoutingRulesDataRelationshipsRulesDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules_data_items_type import (
            TeamRoutingRulesDataRelationshipsRulesDataItemsType,
        )

        return {
            "id": (str,),
            "type": (TeamRoutingRulesDataRelationshipsRulesDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: TeamRoutingRulesDataRelationshipsRulesDataItemsType, **kwargs):
        """
        Defines a relationship item to link a routing rule by its ID and type.

        :param id: Specifies the unique identifier for the related routing rule.
        :type id: str

        :param type: Indicates that the resource is of type 'team_routing_rules'.
        :type type: TeamRoutingRulesDataRelationshipsRulesDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
