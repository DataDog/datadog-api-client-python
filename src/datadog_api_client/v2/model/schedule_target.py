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
    from datadog_api_client.v2.model.schedule_target_type import ScheduleTargetType


class ScheduleTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_target_type import ScheduleTargetType

        return {
            "id": (str,),
            "type": (ScheduleTargetType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleTargetType, **kwargs):
        """
        Represents a schedule target for an escalation policy step, including its ID and resource type.

        :param id: Specifies the unique identifier of the schedule resource.
        :type id: str

        :param type: Indicates that the resource is of type ``schedules``.
        :type type: ScheduleTargetType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
