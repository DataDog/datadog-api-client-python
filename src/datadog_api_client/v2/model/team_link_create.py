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


from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_link_type import TeamLinkType


@dataclass
class TeamLinkCreateJSON:
    label: Union[str, UnsetType] = unset
    position: Union[int, UnsetType] = unset
    team_id: Union[str, UnsetType] = unset
    url: Union[str, UnsetType] = unset


class TeamLinkCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_link_type import TeamLinkType

        return {
            "attributes": (TeamLinkAttributes,),
            "type": (TeamLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = TeamLinkCreateJSON

    def __init__(self_, attributes: TeamLinkAttributes, type: TeamLinkType, **kwargs):
        """
        Team link create

        :param attributes: Team link attributes
        :type attributes: TeamLinkAttributes

        :param type: Team link type
        :type type: TeamLinkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
