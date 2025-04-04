# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_reference_relationships_oncall_users import (
        TeamReferenceRelationshipsOncallUsers,
    )


class TeamReferenceRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_reference_relationships_oncall_users import (
            TeamReferenceRelationshipsOncallUsers,
        )

        return {
            "oncall_users": (TeamReferenceRelationshipsOncallUsers,),
        }

    attribute_map = {
        "oncall_users": "oncall_users",
    }

    def __init__(self_, oncall_users: Union[TeamReferenceRelationshipsOncallUsers, UnsetType] = unset, **kwargs):
        """
        Collects the key relationship fields for a team reference, specifically on-call users.

        :param oncall_users: Defines which users are on-call within a team, stored as an array of references.
        :type oncall_users: TeamReferenceRelationshipsOncallUsers, optional
        """
        if oncall_users is not unset:
            kwargs["oncall_users"] = oncall_users
        super().__init__(kwargs)
