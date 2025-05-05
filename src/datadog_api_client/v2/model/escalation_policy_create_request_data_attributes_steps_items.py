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
    from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
        EscalationPolicyStepAttributesAssignment,
    )
    from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget


class EscalationPolicyCreateRequestDataAttributesStepsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
            EscalationPolicyStepAttributesAssignment,
        )
        from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget

        return {
            "assignment": (EscalationPolicyStepAttributesAssignment,),
            "escalate_after_seconds": (int,),
            "targets": ([EscalationPolicyStepTarget],),
        }

    attribute_map = {
        "assignment": "assignment",
        "escalate_after_seconds": "escalate_after_seconds",
        "targets": "targets",
    }

    def __init__(
        self_,
        targets: List[EscalationPolicyStepTarget],
        assignment: Union[EscalationPolicyStepAttributesAssignment, UnsetType] = unset,
        escalate_after_seconds: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a single escalation step within an escalation policy creation request. Contains assignment strategy, escalation timeout, and a list of targets.

        :param assignment: Specifies how this escalation step will assign targets (example ``default`` or ``round-robin`` ).
        :type assignment: EscalationPolicyStepAttributesAssignment, optional

        :param escalate_after_seconds: Defines how many seconds to wait before escalating to the next step.
        :type escalate_after_seconds: int, optional

        :param targets: Specifies the collection of escalation targets for this step.
        :type targets: [EscalationPolicyStepTarget]
        """
        if assignment is not unset:
            kwargs["assignment"] = assignment
        if escalate_after_seconds is not unset:
            kwargs["escalate_after_seconds"] = escalate_after_seconds
        super().__init__(kwargs)

        self_.targets = targets
