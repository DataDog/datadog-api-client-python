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
    from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts_data_items_type import (
        ScheduleOnCallResponderDataRelationshipsShiftsDataItemsType,
    )


class ScheduleOnCallResponderDataRelationshipsShiftsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responder_data_relationships_shifts_data_items_type import (
            ScheduleOnCallResponderDataRelationshipsShiftsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (ScheduleOnCallResponderDataRelationshipsShiftsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleOnCallResponderDataRelationshipsShiftsDataItemsType, **kwargs):
        """
        Represents a reference to one of the shifts satisfying this responder group's position.

        :param id: Unique identifier of the shift.
        :type id: str

        :param type: Indicates that the related resource is of type ``shifts``.
        :type type: ScheduleOnCallResponderDataRelationshipsShiftsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
