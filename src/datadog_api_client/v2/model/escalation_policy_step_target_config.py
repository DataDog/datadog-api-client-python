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
    from datadog_api_client.v2.model.escalation_policy_step_target_config_schedule import (
        EscalationPolicyStepTargetConfigSchedule,
    )


class EscalationPolicyStepTargetConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_step_target_config_schedule import (
            EscalationPolicyStepTargetConfigSchedule,
        )

        return {
            "schedule": (EscalationPolicyStepTargetConfigSchedule,),
        }

    attribute_map = {
        "schedule": "schedule",
    }

    def __init__(self_, schedule: Union[EscalationPolicyStepTargetConfigSchedule, UnsetType] = unset, **kwargs):
        """
        Configuration for an escalation target, such as schedule position.

        :param schedule: Schedule-specific configuration for an escalation target.
        :type schedule: EscalationPolicyStepTargetConfigSchedule, optional
        """
        if schedule is not unset:
            kwargs["schedule"] = schedule
        super().__init__(kwargs)
