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
    from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts_data_items import (
        ScheduleOnCallResponderDataRelationshipsShiftsDataItems,
    )


class ScheduleOnCallResponderDataRelationshipsShifts(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts_data_items import (
            ScheduleOnCallResponderDataRelationshipsShiftsDataItems,
        )

        return {
            "data": ([ScheduleOnCallResponderDataRelationshipsShiftsDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[ScheduleOnCallResponderDataRelationshipsShiftsDataItems], UnsetType] = unset, **kwargs
    ):
        """
        Defines the list of shifts satisfying this responder group's position. Multiple shifts occur when a schedule has multiple concurrent on-call responders at that position.

        :param data: Array of references to the shifts included in the response.
        :type data: [ScheduleOnCallResponderDataRelationshipsShiftsDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
