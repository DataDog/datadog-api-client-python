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


from datadog_api_client.v2.model.team_attributes import TeamAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_type import TeamType


@dataclass
class TeamDataJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    description: Union[str, none_type, UnsetType] = unset
    handle: Union[str, UnsetType] = unset
    link_count: Union[int, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    summary: Union[str, none_type, UnsetType] = unset
    user_count: Union[int, UnsetType] = unset


class TeamData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_type import TeamType

        return {
            "attributes": (TeamAttributes,),
            "id": (str,),
            "type": (TeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = TeamDataJSON

    def __init__(self_, attributes: TeamAttributes, id: str, type: TeamType, **kwargs):
        """
        A team

        :param attributes: Team attributes
        :type attributes: TeamAttributes

        :param id: The team's identifier
        :type id: str

        :param type: Team type
        :type type: TeamType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
