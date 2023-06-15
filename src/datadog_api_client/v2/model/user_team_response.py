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


from datadog_api_client.v2.model.user_team_role import UserTeamRole
from datadog_api_client.v2.model.user_team_role import UserTeamRole

if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team import UserTeam


@dataclass
class UserTeamResponseJSON:
    id: str
    role: Union[UserTeamRole, none_type, UnsetType] = unset
    user: Union[str, UnsetType] = unset


class UserTeamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team import UserTeam

        return {
            "data": (UserTeam,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = UserTeamResponseJSON

    def __init__(self_, data: Union[UserTeam, UnsetType] = unset, **kwargs):
        """
        Team membership response

        :param data: A user's relationship with a team
        :type data: UserTeam, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
