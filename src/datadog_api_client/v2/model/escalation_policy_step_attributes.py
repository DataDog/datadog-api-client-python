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
    from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
        EscalationPolicyStepAttributesAssignment,
    )


class EscalationPolicyStepAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
            EscalationPolicyStepAttributesAssignment,
        )

        return {
            "assignment": (EscalationPolicyStepAttributesAssignment,),
            "escalate_after_seconds": (int,),
        }

    attribute_map = {
        "assignment": "assignment",
        "escalate_after_seconds": "escalate_after_seconds",
    }

    def __init__(
        self_,
        assignment: Union[EscalationPolicyStepAttributesAssignment, UnsetType] = unset,
        escalate_after_seconds: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines attributes for an escalation policy step, such as assignment strategy and escalation timeout.

        :param assignment: Specifies how this escalation step will assign targets (example ``default`` or ``round-robin`` ).
        :type assignment: EscalationPolicyStepAttributesAssignment, optional

        :param escalate_after_seconds: Specifies how many seconds to wait before escalating to the next step.
        :type escalate_after_seconds: int, optional
        """
        if assignment is not unset:
            kwargs["assignment"] = assignment
        if escalate_after_seconds is not unset:
            kwargs["escalate_after_seconds"] = escalate_after_seconds
        super().__init__(kwargs)
