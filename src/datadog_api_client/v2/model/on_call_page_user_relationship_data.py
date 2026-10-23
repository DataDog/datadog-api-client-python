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
    from datadog_api_client.v2.model.schedule_user_type import ScheduleUserType


class OnCallPageUserRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_user_type import ScheduleUserType

        return {
            "id": (str,),
            "type": (ScheduleUserType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleUserType, **kwargs):
        """
        Reference to a user.

        :param id: The user ID.
        :type id: str

        :param type: Users resource type.
        :type type: ScheduleUserType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
