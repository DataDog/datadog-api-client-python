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
    from datadog_api_client.v2.model.schedule_member_relationships_user import ScheduleMemberRelationshipsUser


class ScheduleMemberRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_member_relationships_user import ScheduleMemberRelationshipsUser

        return {
            "user": (ScheduleMemberRelationshipsUser,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(self_, user: Union[ScheduleMemberRelationshipsUser, UnsetType] = unset, **kwargs):
        """
        Defines relationships for a schedule member, primarily referencing a single user.

        :param user: Wraps the user data reference for a schedule member.
        :type user: ScheduleMemberRelationshipsUser, optional
        """
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
