# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team import Team
    from datadog_api_client.v2.model.team_included import TeamIncluded
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.team_link import TeamLink
    from datadog_api_client.v2.model.user_team_permission import UserTeamPermission


@dataclass
class TeamsResponseJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    description: Union[str, none_type, UnsetType] = unset
    handle: Union[str, UnsetType] = unset
    link_count: Union[int, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    summary: Union[str, none_type, UnsetType] = unset
    user_count: Union[int, UnsetType] = unset
    team_links: Union[List[str], UnsetType] = unset
    user_team_permissions: Union[str, UnsetType] = unset


class TeamsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team import Team
        from datadog_api_client.v2.model.team_included import TeamIncluded

        return {
            "data": ([Team],),
            "included": ([TeamIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    json_api_model = TeamsResponseJSON

    def __init__(
        self_,
        data: Union[List[Team], UnsetType] = unset,
        included: Union[List[Union[TeamIncluded, User, TeamLink, UserTeamPermission]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with multiple teams

        :param data: Teams response data
        :type data: [Team], optional

        :param included: Resources related to the team
        :type included: [TeamIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
