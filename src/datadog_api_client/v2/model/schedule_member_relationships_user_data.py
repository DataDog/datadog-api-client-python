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
    from datadog_api_client.v2.model.schedule_member_relationships_user_data_type import (
        ScheduleMemberRelationshipsUserDataType,
    )


class ScheduleMemberRelationshipsUserData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_member_relationships_user_data_type import (
            ScheduleMemberRelationshipsUserDataType,
        )

        return {
            "id": (str,),
            "type": (ScheduleMemberRelationshipsUserDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleMemberRelationshipsUserDataType, **kwargs):
        """
        Points to the user data associated with this schedule member, including an ID and type.

        :param id: The user's unique identifier.
        :type id: str

        :param type: Users resource type.
        :type type: ScheduleMemberRelationshipsUserDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
