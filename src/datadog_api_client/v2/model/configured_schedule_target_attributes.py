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
    from datadog_api_client.v2.model.schedule_target_position import ScheduleTargetPosition


class ConfiguredScheduleTargetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_target_position import ScheduleTargetPosition

        return {
            "position": (ScheduleTargetPosition,),
        }

    attribute_map = {
        "position": "position",
    }

    def __init__(self_, position: ScheduleTargetPosition, **kwargs):
        """
        Attributes for a configured schedule target, including position.

        :param position: Specifies the position of a schedule target (example ``previous`` , ``current`` , or ``next`` ).
        :type position: ScheduleTargetPosition
        """
        super().__init__(kwargs)

        self_.position = position
