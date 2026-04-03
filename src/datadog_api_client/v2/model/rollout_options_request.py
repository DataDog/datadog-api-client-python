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
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy

        return {
            "autostart": (bool, none_type),
            "selection_interval_ms": (int,),
            "strategy": (RolloutStrategy,),
        }

    attribute_map = {
        "autostart": "autostart",
        "selection_interval_ms": "selection_interval_ms",
        "strategy": "strategy",
    }

    def __init__(
        self_,
        strategy: RolloutStrategy,
        autostart: Union[bool, none_type, UnsetType] = unset,
        selection_interval_ms: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Rollout options request payload.

        :param autostart: Whether the schedule should begin automatically.
        :type autostart: bool, none_type, optional

        :param selection_interval_ms: Interval in milliseconds for uniform interval strategies.
        :type selection_interval_ms: int, optional

        :param strategy: The progression strategy used by a progressive rollout.
        :type strategy: RolloutStrategy
        """
        if autostart is not unset:
            kwargs["autostart"] = autostart
        if selection_interval_ms is not unset:
            kwargs["selection_interval_ms"] = selection_interval_ms
        super().__init__(kwargs)

        self_.strategy = strategy
