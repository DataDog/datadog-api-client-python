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
    from datadog_api_client.v2.model.configured_schedule_target_relationships_schedule import (
        ConfiguredScheduleTargetRelationshipsSchedule,
    )


class ConfiguredScheduleTargetRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.configured_schedule_target_relationships_schedule import (
            ConfiguredScheduleTargetRelationshipsSchedule,
        )

        return {
            "schedule": (ConfiguredScheduleTargetRelationshipsSchedule,),
        }

    attribute_map = {
        "schedule": "schedule",
    }

    def __init__(self_, schedule: ConfiguredScheduleTargetRelationshipsSchedule, **kwargs):
        """
        Represents the relationships of a configured schedule target.

        :param schedule: Holds the schedule reference for a configured schedule target.
        :type schedule: ConfiguredScheduleTargetRelationshipsSchedule
        """
        super().__init__(kwargs)

        self_.schedule = schedule
