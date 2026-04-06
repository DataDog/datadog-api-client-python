# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class AllocationExposureRolloutStep(ModelNormal):
    validations = {
        "exposure_ratio": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
        "grouped_step_index": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "allocation_exposure_schedule_id": (UUID,),
            "created_at": (datetime,),
            "exposure_ratio": (float,),
            "grouped_step_index": (int,),
            "id": (UUID,),
            "interval_ms": (int, none_type),
            "is_pause_record": (bool,),
            "order_position": (int,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "allocation_exposure_schedule_id": "allocation_exposure_schedule_id",
        "created_at": "created_at",
        "exposure_ratio": "exposure_ratio",
        "grouped_step_index": "grouped_step_index",
        "id": "id",
        "interval_ms": "interval_ms",
        "is_pause_record": "is_pause_record",
        "order_position": "order_position",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        allocation_exposure_schedule_id: UUID,
        created_at: datetime,
        exposure_ratio: float,
        grouped_step_index: int,
        id: UUID,
        is_pause_record: bool,
        order_position: int,
        updated_at: datetime,
        interval_ms: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Exposure progression step details.

        :param allocation_exposure_schedule_id: The progressive rollout ID this step belongs to.
        :type allocation_exposure_schedule_id: UUID

        :param created_at: The timestamp when the progression step was created.
        :type created_at: datetime

        :param exposure_ratio: The exposure ratio for this step.
        :type exposure_ratio: float

        :param grouped_step_index: Logical index grouping related steps.
        :type grouped_step_index: int

        :param id: The unique identifier of the progression step.
        :type id: UUID

        :param interval_ms: Step duration in milliseconds.
        :type interval_ms: int, none_type, optional

        :param is_pause_record: Whether this step represents a pause record.
        :type is_pause_record: bool

        :param order_position: Sort order for the progression step.
        :type order_position: int

        :param updated_at: The timestamp when the progression step was last updated.
        :type updated_at: datetime
        """
        if interval_ms is not unset:
            kwargs["interval_ms"] = interval_ms
        super().__init__(kwargs)

        self_.allocation_exposure_schedule_id = allocation_exposure_schedule_id
        self_.created_at = created_at
        self_.exposure_ratio = exposure_ratio
        self_.grouped_step_index = grouped_step_index
        self_.id = id
        self_.is_pause_record = is_pause_record
        self_.order_position = order_position
        self_.updated_at = updated_at
