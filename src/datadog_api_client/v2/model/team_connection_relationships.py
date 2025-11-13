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
    from datadog_api_client.v2.model.connected_team_ref import ConnectedTeamRef
    from datadog_api_client.v2.model.team_ref import TeamRef


class TeamConnectionRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connected_team_ref import ConnectedTeamRef
        from datadog_api_client.v2.model.team_ref import TeamRef

        return {
            "connected_team": (ConnectedTeamRef,),
            "team": (TeamRef,),
        }

    attribute_map = {
        "connected_team": "connected_team",
        "team": "team",
    }

    def __init__(
        self_,
        connected_team: Union[ConnectedTeamRef, UnsetType] = unset,
        team: Union[TeamRef, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of the team connection.

        :param connected_team: Reference to a team from an external system.
        :type connected_team: ConnectedTeamRef, optional

        :param team: Reference to a Datadog team.
        :type team: TeamRef, optional
        """
        if connected_team is not unset:
            kwargs["connected_team"] = connected_team
        if team is not unset:
            kwargs["team"] = team
        super().__init__(kwargs)
