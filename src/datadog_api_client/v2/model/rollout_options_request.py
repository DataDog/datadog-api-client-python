# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy


class RolloutOptionsRequest(ModelNormal):
    validations = {
        "scheduled_start": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy

        return {
            "autostart": (bool, none_type),
            "scheduled_start": (str,),
            "selection_interval_ms": (int,),
            "strategy": (RolloutStrategy,),
        }

    attribute_map = {
        "autostart": "autostart",
        "scheduled_start": "scheduled_start",
        "selection_interval_ms": "selection_interval_ms",
        "strategy": "strategy",
    }

    def __init__(
        self_,
        strategy: RolloutStrategy,
        autostart: Union[bool, none_type, UnsetType] = unset,
        scheduled_start: Union[str, UnsetType] = unset,
        selection_interval_ms: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Rollout options request payload.

        :param autostart: Whether the schedule should begin automatically. Deprecated in favor of
            ``scheduled_start`` , which takes precedence when both are set. **Deprecated**.
        :type autostart: bool, none_type, optional

        :param scheduled_start: Controls when the schedule starts. Supersedes ``autostart``. One of:

            * ``none`` : create the schedule without starting it.
            * ``now`` : start the schedule immediately.
            * `relative:<duration>`: start after a duration (for example `relative:2h`).
            * `absolute:<RFC3339 timestamp>`: start at a specific time (for example `absolute:2025-06-13T12:00:00Z`).

            An ``absolute`` timestamp in the past or present is treated as ``now``. A future start time
            is not supported for allocations linked to a standard experiment.
        :type scheduled_start: str, optional

        :param selection_interval_ms: Interval in milliseconds for uniform interval strategies.
        :type selection_interval_ms: int, optional

        :param strategy: The progression strategy used by a progressive rollout.
        :type strategy: RolloutStrategy
        """
        if autostart is not unset:
            kwargs["autostart"] = autostart
        if scheduled_start is not unset:
            kwargs["scheduled_start"] = scheduled_start
        if selection_interval_ms is not unset:
            kwargs["selection_interval_ms"] = selection_interval_ms
        super().__init__(kwargs)

        self_.strategy = strategy
