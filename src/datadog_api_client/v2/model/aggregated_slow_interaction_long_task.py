# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class AggregatedSlowInteractionLongTask(ModelNormal):
    validations = {
        "instance_count": {
            "inclusive_maximum": 2147483647,
        },
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "action_type": (str,),
            "avg_blocking_duration": (int,),
            "avg_duration": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "instance_count": (int,),
            "selector": (str, none_type),
            "selector_normalized": (str, none_type),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "action_type": "action_type",
        "avg_blocking_duration": "avg_blocking_duration",
        "avg_duration": "avg_duration",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "instance_count": "instance_count",
        "selector": "selector",
        "selector_normalized": "selector_normalized",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        action_type: str,
        avg_blocking_duration: int,
        avg_duration: int,
        fingerprint: str,
        impact_score: float,
        instance_count: int,
        selector: Union[str, none_type],
        selector_normalized: Union[str, none_type],
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated slow interaction with long task detection grouped by action and selector.

        :param action_type: Type of user interaction that triggered the slow response.
        :type action_type: str

        :param avg_blocking_duration: Average long task blocking duration in nanoseconds.
        :type avg_blocking_duration: int

        :param avg_duration: Average total interaction duration in nanoseconds.
        :type avg_duration: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score combining view frequency and blocking severity.
        :type impact_score: float

        :param instance_count: Total number of detection instances across sampled views.
        :type instance_count: int

        :param selector: CSS selector of the element that was interacted with.
        :type selector: str, none_type

        :param selector_normalized: Normalized CSS selector with dynamic parts replaced.
        :type selector_normalized: str, none_type

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.action_type = action_type
        self_.avg_blocking_duration = avg_blocking_duration
        self_.avg_duration = avg_duration
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.instance_count = instance_count
        self_.selector = selector
        self_.selector_normalized = selector_normalized
        self_.view_occurrences = view_occurrences
