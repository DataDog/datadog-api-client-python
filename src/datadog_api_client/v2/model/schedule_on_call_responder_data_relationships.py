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
    from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts import (
        ScheduleOnCallResponderDataRelationshipsShifts,
    )


class ScheduleOnCallResponderDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts import (
            ScheduleOnCallResponderDataRelationshipsShifts,
        )

        return {
            "shifts": (ScheduleOnCallResponderDataRelationshipsShifts,),
        }

    attribute_map = {
        "shifts": "shifts",
    }

    def __init__(self_, shifts: Union[ScheduleOnCallResponderDataRelationshipsShifts, UnsetType] = unset, **kwargs):
        """
        Relationships for a single position's (previous, current, or next) responder group.

        :param shifts: Defines the list of shifts satisfying this responder group's position. Multiple shifts occur when a schedule has multiple concurrent on-call responders at that position.
        :type shifts: ScheduleOnCallResponderDataRelationshipsShifts, optional
        """
        if shifts is not unset:
            kwargs["shifts"] = shifts
        super().__init__(kwargs)
