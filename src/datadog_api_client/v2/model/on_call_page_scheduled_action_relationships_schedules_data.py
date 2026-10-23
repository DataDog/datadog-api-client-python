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
    from datadog_api_client.v2.model.schedule_data_type import ScheduleDataType


class OnCallPageScheduledActionRelationshipsSchedulesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data_type import ScheduleDataType

        return {
            "id": (str,),
            "type": (ScheduleDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleDataType, **kwargs):
        """
        Reference to a schedule.

        :param id: The schedule ID.
        :type id: str

        :param type: Schedules resource type.
        :type type: ScheduleDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
