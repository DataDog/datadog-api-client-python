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
    from datadog_api_client.v2.model.team_reference_relationships_oncall_users_data_items import (
        TeamReferenceRelationshipsOncallUsersDataItems,
    )


class TeamReferenceRelationshipsOncallUsers(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_reference_relationships_oncall_users_data_items import (
            TeamReferenceRelationshipsOncallUsersDataItems,
        )

        return {
            "data": ([TeamReferenceRelationshipsOncallUsersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[TeamReferenceRelationshipsOncallUsersDataItems], UnsetType] = unset, **kwargs):
        """
        Defines which users are on-call within a team, stored as an array of references.

        :param data: The list of user references who are on-call for this team.
        :type data: [TeamReferenceRelationshipsOncallUsersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
