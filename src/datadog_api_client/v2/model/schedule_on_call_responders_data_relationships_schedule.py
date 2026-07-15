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
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule_data import (
        ScheduleOnCallRespondersDataRelationshipsScheduleData,
    )


class ScheduleOnCallRespondersDataRelationshipsSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_schedule_data import (
            ScheduleOnCallRespondersDataRelationshipsScheduleData,
        )

        return {
            "data": (ScheduleOnCallRespondersDataRelationshipsScheduleData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[ScheduleOnCallRespondersDataRelationshipsScheduleData, UnsetType] = unset, **kwargs
    ):
        """
        Defines the relationship to the schedule this on-call responders lookup was performed for.

        :param data: Represents a reference to the schedule this on-call responders lookup was performed for.
        :type data: ScheduleOnCallRespondersDataRelationshipsScheduleData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
