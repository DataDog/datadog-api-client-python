# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.schedule_on_call_responders_data import ScheduleOnCallRespondersData
    from datadog_api_client.v2.model.schedule_on_call_responders_included import ScheduleOnCallRespondersIncluded
    from datadog_api_client.v2.model.schedule_on_call_responder_data import ScheduleOnCallResponderData
    from datadog_api_client.v2.model.shift_data import ShiftData
    from datadog_api_client.v2.model.schedule_data import ScheduleData
    from datadog_api_client.v2.model.user import User


class ScheduleOnCallResponders(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data import ScheduleOnCallRespondersData
        from datadog_api_client.v2.model.schedule_on_call_responders_included import ScheduleOnCallRespondersIncluded

        return {
            "data": (ScheduleOnCallRespondersData,),
            "included": ([ScheduleOnCallRespondersIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[ScheduleOnCallRespondersData, UnsetType] = unset,
        included: Union[
            List[Union[ScheduleOnCallRespondersIncluded, ScheduleOnCallResponderData, ShiftData, ScheduleData, User]],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Root object representing a schedule's on-call responders, grouped by position (previous, current, next), for a given point in time.

        :param data: The main data object representing a schedule's on-call responders lookup, including relationships and metadata.
        :type data: ScheduleOnCallRespondersData, optional

        :param included: Related resources referenced in the responder groups' relationships, such as shifts, schedules, and users.
        :type included: [ScheduleOnCallRespondersIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
