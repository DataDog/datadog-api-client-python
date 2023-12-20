# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team_team_type import UserTeamTeamType


class RelationshipToUserTeamTeamData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team_team_type import UserTeamTeamType

        return {
            "id": (str,),
            "type": (UserTeamTeamType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: UserTeamTeamType, **kwargs):
        """
        The team associated with the membership

        :param id: The ID of the team associated with the membership
        :type id: str

        :param type: User team team type
        :type type: UserTeamTeamType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
