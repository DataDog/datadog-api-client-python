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
    from datadog_api_client.v2.model.synthetics_downtime_time_slot_request import SyntheticsDowntimeTimeSlotRequest


class SyntheticsDowntimeDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_time_slot_request import SyntheticsDowntimeTimeSlotRequest

        return {
            "description": (str,),
            "is_enabled": (bool,),
            "name": (str,),
            "tags": ([str],),
            "test_ids": ([str],),
            "time_slots": ([SyntheticsDowntimeTimeSlotRequest],),
        }

    attribute_map = {
        "description": "description",
        "is_enabled": "isEnabled",
        "name": "name",
        "tags": "tags",
        "test_ids": "testIds",
        "time_slots": "timeSlots",
    }

    def __init__(
        self_,
        is_enabled: bool,
        name: str,
        test_ids: List[str],
        time_slots: List[SyntheticsDowntimeTimeSlotRequest],
        description: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a Synthetics downtime.

        :param description: An optional description of the downtime.
        :type description: str, optional

        :param is_enabled: Whether the downtime is enabled.
        :type is_enabled: bool

        :param name: The name of the downtime.
        :type name: str

        :param tags: List of tags associated with a Synthetics downtime.
        :type tags: [str], optional

        :param test_ids: List of Synthetics test public IDs associated with a downtime.
        :type test_ids: [str]

        :param time_slots: List of time slots for a Synthetics downtime create or update request.
        :type time_slots: [SyntheticsDowntimeTimeSlotRequest]
        """
        if description is not unset:
            kwargs["description"] = description
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.is_enabled = is_enabled
        self_.name = name
        self_.test_ids = test_ids
        self_.time_slots = time_slots
