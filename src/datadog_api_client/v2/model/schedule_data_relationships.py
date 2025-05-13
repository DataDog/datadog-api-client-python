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
    from datadog_api_client.v2.model.schedule_data_relationships_layers import ScheduleDataRelationshipsLayers
    from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams


class ScheduleDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data_relationships_layers import ScheduleDataRelationshipsLayers
        from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams

        return {
            "layers": (ScheduleDataRelationshipsLayers,),
            "teams": (DataRelationshipsTeams,),
        }

    attribute_map = {
        "layers": "layers",
        "teams": "teams",
    }

    def __init__(
        self_,
        layers: Union[ScheduleDataRelationshipsLayers, UnsetType] = unset,
        teams: Union[DataRelationshipsTeams, UnsetType] = unset,
        **kwargs,
    ):
        """
        Groups the relationships for a schedule object, referencing layers and teams.

        :param layers: Associates layers with this schedule in a data structure.
        :type layers: ScheduleDataRelationshipsLayers, optional

        :param teams: Associates teams with this schedule in a data structure.
        :type teams: DataRelationshipsTeams, optional
        """
        if layers is not unset:
            kwargs["layers"] = layers
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
