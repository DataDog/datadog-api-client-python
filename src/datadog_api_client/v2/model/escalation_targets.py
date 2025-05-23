# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.escalation_target import EscalationTarget
    from datadog_api_client.v2.model.team_target import TeamTarget
    from datadog_api_client.v2.model.user_target import UserTarget
    from datadog_api_client.v2.model.schedule_target import ScheduleTarget


class EscalationTargets(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_target import EscalationTarget

        return {
            "data": ([EscalationTarget],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: Union[List[Union[EscalationTarget, TeamTarget, UserTarget, ScheduleTarget]], UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of escalation targets for a step

        :param data: The ``EscalationTargets`` ``data``.
        :type data: [EscalationTarget], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
