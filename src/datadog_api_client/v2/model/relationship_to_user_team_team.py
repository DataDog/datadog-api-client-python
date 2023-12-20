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
    from datadog_api_client.v2.model.relationship_to_user_team_team_data import RelationshipToUserTeamTeamData


class RelationshipToUserTeamTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user_team_team_data import RelationshipToUserTeamTeamData

        return {
            "data": (RelationshipToUserTeamTeamData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RelationshipToUserTeamTeamData, **kwargs):
        """
        Relationship between team membership and team

        :param data: The team associated with the membership
        :type data: RelationshipToUserTeamTeamData
        """
        super().__init__(kwargs)

        self_.data = data
