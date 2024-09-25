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
    from datadog_api_client.v2.model.teams_response_links import TeamsResponseLinks
    from datadog_api_client.v2.model.teams_response_meta import TeamsResponseMeta
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.team import Team


class UserTeamsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team import UserTeam
        from datadog_api_client.v2.model.user_team_included import UserTeamIncluded
        from datadog_api_client.v2.model.teams_response_links import TeamsResponseLinks
        from datadog_api_client.v2.model.teams_response_meta import TeamsResponseMeta

        return {
            "data": ([UserTeam],),
            "included": ([UserTeamIncluded],),
            "links": (TeamsResponseLinks,),
            "meta": (TeamsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[UserTeam], UnsetType] = unset,
        included: Union[List[Union[UserTeamIncluded, User, Team]], UnsetType] = unset,
        links: Union[TeamsResponseLinks, UnsetType] = unset,
        meta: Union[TeamsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team memberships response

        :param data: Team memberships response data
        :type data: [UserTeam], optional

        :param included: Resources related to the team memberships
        :type included: [UserTeamIncluded], optional

        :param links: Teams response links.
        :type links: TeamsResponseLinks, optional

        :param meta: Teams response metadata.
        :type meta: TeamsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
