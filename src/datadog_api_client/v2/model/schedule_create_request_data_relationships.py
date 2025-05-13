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
    from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams


class ScheduleCreateRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams

        return {
            "teams": (DataRelationshipsTeams,),
        }

    attribute_map = {
        "teams": "teams",
    }

    def __init__(self_, teams: Union[DataRelationshipsTeams, UnsetType] = unset, **kwargs):
        """
        Gathers relationship objects for the schedule creation request, including the teams to associate.

        :param teams: Associates teams with this schedule in a data structure.
        :type teams: DataRelationshipsTeams, optional
        """
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
