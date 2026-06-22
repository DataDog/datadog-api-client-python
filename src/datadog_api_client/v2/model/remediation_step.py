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
    from datadog_api_client.v2.model.remediation_step_approval_state import RemediationStepApprovalState
    from datadog_api_client.v2.model.remediation_risk_level import RemediationRiskLevel


class RemediationStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_step_approval_state import RemediationStepApprovalState
        from datadog_api_client.v2.model.remediation_risk_level import RemediationRiskLevel

        return {
            "action_fqn": (str,),
            "approval_state": (RemediationStepApprovalState,),
            "description": (str,),
            "reversible": (bool,),
            "risk": (RemediationRiskLevel,),
            "step_id": (str,),
        }

    attribute_map = {
        "action_fqn": "action_fqn",
        "approval_state": "approval_state",
        "description": "description",
        "reversible": "reversible",
        "risk": "risk",
        "step_id": "step_id",
    }

    def __init__(
        self_,
        action_fqn: Union[str, UnsetType] = unset,
        approval_state: Union[RemediationStepApprovalState, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        reversible: Union[bool, UnsetType] = unset,
        risk: Union[RemediationRiskLevel, UnsetType] = unset,
        step_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single execution-oriented step in a remediation plan.

        :param action_fqn: Fully qualified action type, for example ecs.update_service_memory.
        :type action_fqn: str, optional

        :param approval_state: Approval state for a remediation step.
        :type approval_state: RemediationStepApprovalState, optional

        :param description: Human-readable description of the step.
        :type description: str, optional

        :param reversible: Whether the step can be reversed after execution.
        :type reversible: bool, optional

        :param risk: Estimated risk of a remediation step or proposed fix.
        :type risk: RemediationRiskLevel, optional

        :param step_id: Unique ID for the step within the plan.
        :type step_id: str, optional
        """
        if action_fqn is not unset:
            kwargs["action_fqn"] = action_fqn
        if approval_state is not unset:
            kwargs["approval_state"] = approval_state
        if description is not unset:
            kwargs["description"] = description
        if reversible is not unset:
            kwargs["reversible"] = reversible
        if risk is not unset:
            kwargs["risk"] = risk
        if step_id is not unset:
            kwargs["step_id"] = step_id
        super().__init__(kwargs)
