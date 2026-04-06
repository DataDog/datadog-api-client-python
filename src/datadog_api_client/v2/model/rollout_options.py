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
    from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy


class RolloutOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy

        return {
            "autostart": (bool,),
            "selection_interval_ms": (int,),
            "strategy": (RolloutStrategy,),
        }

    attribute_map = {
        "autostart": "autostart",
        "selection_interval_ms": "selection_interval_ms",
        "strategy": "strategy",
    }

    def __init__(self_, autostart: bool, selection_interval_ms: int, strategy: RolloutStrategy, **kwargs):
        """
        Applied progression options for a progressive rollout.

        :param autostart: Whether the schedule starts automatically.
        :type autostart: bool

        :param selection_interval_ms: Interval in milliseconds for uniform interval strategies.
        :type selection_interval_ms: int

        :param strategy: The progression strategy used by a progressive rollout.
        :type strategy: RolloutStrategy
        """
        super().__init__(kwargs)

        self_.autostart = autostart
        self_.selection_interval_ms = selection_interval_ms
        self_.strategy = strategy
