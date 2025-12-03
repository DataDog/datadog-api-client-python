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
    from datadog_api_client.v2.model.schedule_target import ScheduleTarget


class ConfiguredScheduleTargetRelationshipsSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_target import ScheduleTarget

        return {
            "data": (ScheduleTarget,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ScheduleTarget, **kwargs):
        """
        Holds the schedule reference for a configured schedule target.

        :param data: Represents a schedule target for an escalation policy step, including its ID and resource type. This is a shortcut for a configured schedule target with position set to 'current'.
        :type data: ScheduleTarget
        """
        super().__init__(kwargs)

        self_.data = data
