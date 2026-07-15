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
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_responders import (
        ScheduleOnCallRespondersDataRelationshipsResponders,
    )
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule import (
        ScheduleOnCallRespondersDataRelationshipsSchedule,
    )


class ScheduleOnCallRespondersDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_responders import (
            ScheduleOnCallRespondersDataRelationshipsResponders,
        )
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule import (
            ScheduleOnCallRespondersDataRelationshipsSchedule,
        )

        return {
            "responders": (ScheduleOnCallRespondersDataRelationshipsResponders,),
            "schedule": (ScheduleOnCallRespondersDataRelationshipsSchedule,),
        }

    attribute_map = {
        "responders": "responders",
        "schedule": "schedule",
    }

    def __init__(
        self_,
        responders: Union[ScheduleOnCallRespondersDataRelationshipsResponders, UnsetType] = unset,
        schedule: Union[ScheduleOnCallRespondersDataRelationshipsSchedule, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships for a schedule's on-call responders lookup, including the schedule and its responder groups.

        :param responders: Defines the list of per-position (previous, current, next) responder groups for the schedule.
        :type responders: ScheduleOnCallRespondersDataRelationshipsResponders, optional

        :param schedule: Defines the relationship to the schedule this on-call responders lookup was performed for.
        :type schedule: ScheduleOnCallRespondersDataRelationshipsSchedule, optional
        """
        if responders is not unset:
            kwargs["responders"] = responders
        if schedule is not unset:
            kwargs["schedule"] = schedule
        super().__init__(kwargs)
