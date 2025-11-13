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
    from datadog_api_client.v2.model.team_connection_attributes import TeamConnectionAttributes
    from datadog_api_client.v2.model.team_connection_relationships import TeamConnectionRelationships
    from datadog_api_client.v2.model.team_connection_type import TeamConnectionType


class TeamConnection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_connection_attributes import TeamConnectionAttributes
        from datadog_api_client.v2.model.team_connection_relationships import TeamConnectionRelationships
        from datadog_api_client.v2.model.team_connection_type import TeamConnectionType

        return {
            "attributes": (TeamConnectionAttributes,),
            "id": (str,),
            "relationships": (TeamConnectionRelationships,),
            "type": (TeamConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: TeamConnectionType,
        attributes: Union[TeamConnectionAttributes, UnsetType] = unset,
        relationships: Union[TeamConnectionRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A relationship between a Datadog team and a team from another external system.

        :param attributes: Attributes of the team connection.
        :type attributes: TeamConnectionAttributes, optional

        :param id: The unique identifier of the team connection.
        :type id: str

        :param relationships: Relationships of the team connection.
        :type relationships: TeamConnectionRelationships, optional

        :param type: Team connection resource type.
        :type type: TeamConnectionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
