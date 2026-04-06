# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ExposureRolloutStepRequest(ModelNormal):
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
            "exposure_ratio": (float,),
            "grouped_step_index": (int,),
            "id": (UUID,),
            "interval_ms": (int, none_type),
            "is_pause_record": (bool,),
        }

    attribute_map = {
        "exposure_ratio": "exposure_ratio",
        "grouped_step_index": "grouped_step_index",
        "id": "id",
        "interval_ms": "interval_ms",
        "is_pause_record": "is_pause_record",
    }

    def __init__(
        self_,
        exposure_ratio: float,
        grouped_step_index: int,
        is_pause_record: bool,
        id: Union[UUID, UnsetType] = unset,
        interval_ms: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Rollout step request payload.

        :param exposure_ratio: The exposure ratio for this step.
        :type exposure_ratio: float

        :param grouped_step_index: Logical index grouping related steps.
        :type grouped_step_index: int

        :param id: The unique identifier of the progression step.
        :type id: UUID, optional

        :param interval_ms: Step duration in milliseconds.
        :type interval_ms: int, none_type, optional

        :param is_pause_record: Whether this step represents a pause record.
        :type is_pause_record: bool
        """
        if id is not unset:
            kwargs["id"] = id
        if interval_ms is not unset:
            kwargs["interval_ms"] = interval_ms
        super().__init__(kwargs)

        self_.exposure_ratio = exposure_ratio
        self_.grouped_step_index = grouped_step_index
        self_.is_pause_record = is_pause_record
