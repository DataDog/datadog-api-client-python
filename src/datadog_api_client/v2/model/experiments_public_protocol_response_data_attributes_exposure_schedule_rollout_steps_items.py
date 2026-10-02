# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exposure_ratio": (float,),
            "grouped_step_index": (int,),
            "interval_ms": (int,),
            "is_pause_record": (bool,),
            "order_position": (int,),
        }

    attribute_map = {
        "exposure_ratio": "exposure_ratio",
        "grouped_step_index": "grouped_step_index",
        "interval_ms": "interval_ms",
        "is_pause_record": "is_pause_record",
        "order_position": "order_position",
    }

    def __init__(
        self_,
        exposure_ratio: Union[float, UnsetType] = unset,
        grouped_step_index: Union[int, UnsetType] = unset,
        interval_ms: Union[int, UnsetType] = unset,
        is_pause_record: Union[bool, UnsetType] = unset,
        order_position: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        One step in the protocol's traffic exposure schedule.

        :param exposure_ratio: Fraction of traffic exposed during this rollout step.
        :type exposure_ratio: float, optional

        :param grouped_step_index: Index of the group that contains this rollout step.
        :type grouped_step_index: int, optional

        :param interval_ms: Duration of this rollout step, in milliseconds.
        :type interval_ms: int, optional

        :param is_pause_record: Whether this schedule entry represents a pause.
        :type is_pause_record: bool, optional

        :param order_position: Position of this entry in the ordered configuration.
        :type order_position: int, optional
        """
        if exposure_ratio is not unset:
            kwargs["exposure_ratio"] = exposure_ratio
        if grouped_step_index is not unset:
            kwargs["grouped_step_index"] = grouped_step_index
        if interval_ms is not unset:
            kwargs["interval_ms"] = interval_ms
        if is_pause_record is not unset:
            kwargs["is_pause_record"] = is_pause_record
        if order_position is not unset:
            kwargs["order_position"] = order_position
        super().__init__(kwargs)
