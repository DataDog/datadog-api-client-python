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
    from datadog_api_client.v2.model.team_routing_rules_request_rule import TeamRoutingRulesRequestRule


class TeamRoutingRulesRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_request_rule import TeamRoutingRulesRequestRule

        return {
            "rules": ([TeamRoutingRulesRequestRule],),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: Union[List[TeamRoutingRulesRequestRule], UnsetType] = unset, **kwargs):
        """
        Represents the attributes of a request to update or create team routing rules.

        :param rules: A list of routing rule items that define how incoming pages should be handled.
        :type rules: [TeamRoutingRulesRequestRule], optional
        """
        if rules is not unset:
            kwargs["rules"] = rules
        super().__init__(kwargs)
