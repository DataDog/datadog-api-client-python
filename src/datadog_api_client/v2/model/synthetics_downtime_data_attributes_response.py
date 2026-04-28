# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_response import SyntheticsDowntimeTimeSlotResponse


class SyntheticsDowntimeDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_response import (
            SyntheticsDowntimeTimeSlotResponse,
        )

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "created_by_name": (str,),
            "description": (str,),
            "is_enabled": (bool,),
            "name": (str,),
            "tags": ([str],),
            "test_ids": ([str],),
            "time_slots": ([SyntheticsDowntimeTimeSlotResponse],),
            "updated_at": (datetime,),
            "updated_by": (str,),
            "updated_by_name": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "created_by_name": "createdByName",
        "description": "description",
        "is_enabled": "isEnabled",
        "name": "name",
        "tags": "tags",
        "test_ids": "testIds",
        "time_slots": "timeSlots",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
        "updated_by_name": "updatedByName",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        created_by_name: str,
        description: str,
        is_enabled: bool,
        name: str,
        tags: List[str],
        test_ids: List[str],
        time_slots: List[SyntheticsDowntimeTimeSlotResponse],
        updated_at: datetime,
        updated_by: str,
        updated_by_name: str,
        **kwargs,
    ):
        """
        Attributes of a Synthetics downtime response object.

        :param created_at: The timestamp when the downtime was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the downtime.
        :type created_by: str

        :param created_by_name: The display name of the user who created the downtime.
        :type created_by_name: str

        :param description: The description of the downtime.
        :type description: str

        :param is_enabled: Whether the downtime is enabled.
        :type is_enabled: bool

        :param name: The name of the downtime.
        :type name: str

        :param tags: List of tags associated with a Synthetics downtime.
        :type tags: [str]

        :param test_ids: List of Synthetics test public IDs associated with a downtime.
        :type test_ids: [str]

        :param time_slots: List of time slots in a Synthetics downtime response.
        :type time_slots: [SyntheticsDowntimeTimeSlotResponse]

        :param updated_at: The timestamp when the downtime was last updated.
        :type updated_at: datetime

        :param updated_by: The UUID of the user who last updated the downtime.
        :type updated_by: str

        :param updated_by_name: The display name of the user who last updated the downtime.
        :type updated_by_name: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.created_by_name = created_by_name
        self_.description = description
        self_.is_enabled = is_enabled
        self_.name = name
        self_.tags = tags
        self_.test_ids = test_ids
        self_.time_slots = time_slots
        self_.updated_at = updated_at
        self_.updated_by = updated_by
        self_.updated_by_name = updated_by_name
