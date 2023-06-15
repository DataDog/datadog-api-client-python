# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData


@dataclass
class IncidentTeamCreateRequestJSON:
    name: Union[str, UnsetType] = unset
    created_by: Union[str, UnsetType] = unset
    last_modified_by: Union[str, UnsetType] = unset


class IncidentTeamCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData

        return {
            "data": (IncidentTeamCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentTeamCreateRequestJSON

    def __init__(self_, data: IncidentTeamCreateData, **kwargs):
        """
        Create request with an incident team payload.

        :param data: Incident Team data for a create request.
        :type data: IncidentTeamCreateData
        """
        super().__init__(kwargs)

        self_.data = data
