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
    from datadog_api_client.v2.model.schedule_update_request_data_relationships_teams import (
        ScheduleUpdateRequestDataRelationshipsTeams,
    )


class ScheduleUpdateRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_relationships_teams import (
            ScheduleUpdateRequestDataRelationshipsTeams,
        )

        return {
            "teams": (ScheduleUpdateRequestDataRelationshipsTeams,),
        }

    attribute_map = {
        "teams": "teams",
    }

    def __init__(self_, teams: Union[ScheduleUpdateRequestDataRelationshipsTeams, UnsetType] = unset, **kwargs):
        """
        Houses relationships for the schedule update, typically referencing teams.

        :param teams: Defines the teams that this schedule update is associated with.
        :type teams: ScheduleUpdateRequestDataRelationshipsTeams, optional
        """
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
