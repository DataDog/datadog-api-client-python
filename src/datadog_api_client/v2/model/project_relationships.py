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
    from datadog_api_client.v2.model.relationship_to_team_links import RelationshipToTeamLinks
    from datadog_api_client.v2.model.users_relationship import UsersRelationship


class ProjectRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_team_links import RelationshipToTeamLinks
        from datadog_api_client.v2.model.users_relationship import UsersRelationship

        return {
            "member_team": (RelationshipToTeamLinks,),
            "member_user": (UsersRelationship,),
        }

    attribute_map = {
        "member_team": "member_team",
        "member_user": "member_user",
    }

    def __init__(
        self_,
        member_team: Union[RelationshipToTeamLinks, UnsetType] = unset,
        member_user: Union[UsersRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project relationships

        :param member_team: Relationship between a team and a team link
        :type member_team: RelationshipToTeamLinks, optional

        :param member_user: Relationship to users.
        :type member_user: UsersRelationship, optional
        """
        if member_team is not unset:
            kwargs["member_team"] = member_team
        if member_user is not unset:
            kwargs["member_user"] = member_user
        super().__init__(kwargs)
