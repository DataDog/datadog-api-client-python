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
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule_data_type import (
        ScheduleOnCallRespondersDataRelationshipsScheduleDataType,
    )


class ScheduleOnCallRespondersDataRelationshipsScheduleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule_data_type import (
            ScheduleOnCallRespondersDataRelationshipsScheduleDataType,
        )

        return {
            "id": (str,),
            "type": (ScheduleOnCallRespondersDataRelationshipsScheduleDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleOnCallRespondersDataRelationshipsScheduleDataType, **kwargs):
        """
        Represents a reference to the schedule this on-call responders lookup was performed for.

        :param id: Unique identifier of the schedule.
        :type id: str

        :param type: Identifies the resource type for the schedule associated with this on-call responders lookup.
        :type type: ScheduleOnCallRespondersDataRelationshipsScheduleDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
