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
    from datadog_api_client.v2.model.downtime_schedule_recurrence_create_update_request import (
        DowntimeScheduleRecurrenceCreateUpdateRequest,
    )


class DowntimeScheduleRecurrencesCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_schedule_recurrence_create_update_request import (
            DowntimeScheduleRecurrenceCreateUpdateRequest,
        )

        return {
            "recurrences": ([DowntimeScheduleRecurrenceCreateUpdateRequest],),
            "timezone": (str,),
        }

    attribute_map = {
        "recurrences": "recurrences",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        recurrences: List[DowntimeScheduleRecurrenceCreateUpdateRequest],
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A recurring downtime schedule definition.

        :param recurrences: A list of downtime recurrences.
        :type recurrences: [DowntimeScheduleRecurrenceCreateUpdateRequest]

        :param timezone: The timezone in which to schedule the downtime.
        :type timezone: str, optional
        """
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.recurrences = recurrences
