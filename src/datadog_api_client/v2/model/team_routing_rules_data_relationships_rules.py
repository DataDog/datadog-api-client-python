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
    from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules_data_items import (
        TeamRoutingRulesDataRelationshipsRulesDataItems,
    )


class TeamRoutingRulesDataRelationshipsRules(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_data_relationships_rules_data_items import (
            TeamRoutingRulesDataRelationshipsRulesDataItems,
        )

        return {
            "data": ([TeamRoutingRulesDataRelationshipsRulesDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[TeamRoutingRulesDataRelationshipsRulesDataItems], UnsetType] = unset, **kwargs
    ):
        """
        Holds references to a set of routing rules in a relationship.

        :param data: An array of references to the routing rules associated with this team.
        :type data: [TeamRoutingRulesDataRelationshipsRulesDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
