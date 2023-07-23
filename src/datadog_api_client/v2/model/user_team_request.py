# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team_create import UserTeamCreate
    from datadog_api_client.v2.model.user_team_role import UserTeamRole


@dataclass
class UserTeamRequestJSON:
    role: Union[UserTeamRole, none_type, UnsetType] = unset
    user: Union[str, UnsetType] = unset


class UserTeamRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team_create import UserTeamCreate

        return {
            "data": (UserTeamCreate,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = UserTeamRequestJSON

    def __init__(self_, data: UserTeamCreate, **kwargs):
        """
        Team membership request

        :param data: A user's relationship with a team
        :type data: UserTeamCreate
        """
        super().__init__(kwargs)

        self_.data = data
