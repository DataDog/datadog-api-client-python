# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.schedule_target_position import ScheduleTargetPosition


class EscalationPolicyStepTargetConfigSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_target_position import ScheduleTargetPosition

        return {
            "position": (ScheduleTargetPosition,),
        }

    attribute_map = {
        "position": "position",
    }

    def __init__(self_, position: Union[ScheduleTargetPosition, UnsetType] = unset, **kwargs):
        """
        Schedule-specific configuration for an escalation target.

        :param position: Specifies the position of a schedule target (example ``previous`` , ``current`` , or ``next`` ).
        :type position: ScheduleTargetPosition, optional
        """
        if position is not unset:
            kwargs["position"] = position
        super().__init__(kwargs)
