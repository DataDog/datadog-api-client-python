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
    from datadog_api_client.v2.model.relationship_to_team import RelationshipToTeam


class AuthNMappingRelationshipToTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_team import RelationshipToTeam

        return {
            "team": (RelationshipToTeam,),
        }

    attribute_map = {
        "team": "team",
    }

    def __init__(self_, team: RelationshipToTeam, **kwargs):
        """
        Relationship of AuthN Mapping to a Team.

        :param team: Relationship to team.
        :type team: RelationshipToTeam
        """
        super().__init__(kwargs)

        self_.team = team
