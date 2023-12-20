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
    from datadog_api_client.v2.model.relationship_to_user_team_team import RelationshipToUserTeamTeam
    from datadog_api_client.v2.model.relationship_to_user_team_user import RelationshipToUserTeamUser


class UserTeamRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user_team_team import RelationshipToUserTeamTeam
        from datadog_api_client.v2.model.relationship_to_user_team_user import RelationshipToUserTeamUser

        return {
            "team": (RelationshipToUserTeamTeam,),
            "user": (RelationshipToUserTeamUser,),
        }

    attribute_map = {
        "team": "team",
        "user": "user",
    }

    def __init__(
        self_,
        team: Union[RelationshipToUserTeamTeam, UnsetType] = unset,
        user: Union[RelationshipToUserTeamUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationship between membership and a user

        :param team: Relationship between team membership and team
        :type team: RelationshipToUserTeamTeam, optional

        :param user: Relationship between team membership and user
        :type user: RelationshipToUserTeamUser, optional
        """
        if team is not unset:
            kwargs["team"] = team
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
