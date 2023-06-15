# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_update import TeamUpdate


@dataclass
class TeamUpdateRequestJSON:
    color: Union[int, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    handle: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    team_links: Union[List[str], UnsetType] = unset


class TeamUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_update import TeamUpdate

        return {
            "data": (TeamUpdate,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = TeamUpdateRequestJSON

    def __init__(self_, data: TeamUpdate, **kwargs):
        """
        Team update request

        :param data: Team update request
        :type data: TeamUpdate
        """
        super().__init__(kwargs)

        self_.data = data
