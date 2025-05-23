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
    from datadog_api_client.v2.model.team_routing_rules_request_data_attributes import (
        TeamRoutingRulesRequestDataAttributes,
    )
    from datadog_api_client.v2.model.team_routing_rules_request_data_type import TeamRoutingRulesRequestDataType


class TeamRoutingRulesRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_routing_rules_request_data_attributes import (
            TeamRoutingRulesRequestDataAttributes,
        )
        from datadog_api_client.v2.model.team_routing_rules_request_data_type import TeamRoutingRulesRequestDataType

        return {
            "attributes": (TeamRoutingRulesRequestDataAttributes,),
            "id": (str,),
            "type": (TeamRoutingRulesRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: TeamRoutingRulesRequestDataType,
        attributes: Union[TeamRoutingRulesRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Holds the data necessary to create or update team routing rules, including attributes, ID, and resource type.

        :param attributes: Represents the attributes of a request to update or create team routing rules.
        :type attributes: TeamRoutingRulesRequestDataAttributes, optional

        :param id: Specifies the unique identifier for this set of team routing rules.
        :type id: str, optional

        :param type: Team routing rules resource type.
        :type type: TeamRoutingRulesRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
