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
    from datadog_api_client.v2.model.schedule_member_relationships_user_data import ScheduleMemberRelationshipsUserData


class ScheduleMemberRelationshipsUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_member_relationships_user_data import (
            ScheduleMemberRelationshipsUserData,
        )

        return {
            "data": (ScheduleMemberRelationshipsUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ScheduleMemberRelationshipsUserData, **kwargs):
        """
        Wraps the user data reference for a schedule member.

        :param data: Points to the user data associated with this schedule member, including an ID and type.
        :type data: ScheduleMemberRelationshipsUserData
        """
        super().__init__(kwargs)

        self_.data = data
