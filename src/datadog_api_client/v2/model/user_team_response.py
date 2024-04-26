# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team import UserTeam
    from datadog_api_client.v2.model.user_team_included import UserTeamIncluded
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.team import Team


class UserTeamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team import UserTeam
        from datadog_api_client.v2.model.user_team_included import UserTeamIncluded

        return {
            "data": (UserTeam,),
            "included": ([UserTeamIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[UserTeam, UnsetType] = unset,
        included: Union[List[Union[UserTeamIncluded, User, Team]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Team membership response

        :param data: A user's relationship with a team
        :type data: UserTeam, optional

        :param included: Resources related to the team memberships
        :type included: [UserTeamIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
