# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_data import TeamData


@dataclass
class TeamResponseJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    description: Union[str, none_type, UnsetType] = unset
    handle: Union[str, UnsetType] = unset
    link_count: Union[int, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    summary: Union[str, none_type, UnsetType] = unset
    user_count: Union[int, UnsetType] = unset


class TeamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_data import TeamData

        return {
            "data": (TeamData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = TeamResponseJSON

    def __init__(self_, data: Union[TeamData, UnsetType] = unset, **kwargs):
        """
        Response with a team

        :param data: A team
        :type data: TeamData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
