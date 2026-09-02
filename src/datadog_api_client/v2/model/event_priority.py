# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventPriority(ModelSimple):
    """
    The priority of the event alert. Legacy events use `normal` or `low`.
        Alert events use `1` (highest priority) through `5` (lowest priority).

    :param value: Must be one of ["normal", "low", "1", "2", "3", "4", "5"].
    :type value: str
    """

    allowed_values = {
        "normal",
        "low",
        "1",
        "2",
        "3",
        "4",
        "5",
    }
    NORMAL: ClassVar["EventPriority"]
    LOW: ClassVar["EventPriority"]
    PRIORITY_ONE: ClassVar["EventPriority"]
    PRIORITY_TWO: ClassVar["EventPriority"]
    PRIORITY_THREE: ClassVar["EventPriority"]
    PRIORITY_FOUR: ClassVar["EventPriority"]
    PRIORITY_FIVE: ClassVar["EventPriority"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventPriority.NORMAL = EventPriority("normal")
EventPriority.LOW = EventPriority("low")
EventPriority.PRIORITY_ONE = EventPriority("1")
EventPriority.PRIORITY_TWO = EventPriority("2")
EventPriority.PRIORITY_THREE = EventPriority("3")
EventPriority.PRIORITY_FOUR = EventPriority("4")
EventPriority.PRIORITY_FIVE = EventPriority("5")
