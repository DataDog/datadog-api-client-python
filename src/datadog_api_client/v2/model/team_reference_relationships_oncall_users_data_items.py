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
    from datadog_api_client.v2.model.team_reference_relationships_oncall_users_data_items_type import (
        TeamReferenceRelationshipsOncallUsersDataItemsType,
    )


class TeamReferenceRelationshipsOncallUsersDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_reference_relationships_oncall_users_data_items_type import (
            TeamReferenceRelationshipsOncallUsersDataItemsType,
        )

        return {
            "id": (str,),
            "type": (TeamReferenceRelationshipsOncallUsersDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: TeamReferenceRelationshipsOncallUsersDataItemsType, **kwargs):
        """
        References a user who is on-call within this team, identified by ``id`` and ``type``.

        :param id: The unique identifier of the user.
        :type id: str

        :param type: Users resource type.
        :type type: TeamReferenceRelationshipsOncallUsersDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
