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
    from datadog_api_client.v2.model.remediation_confidence import RemediationConfidence
    from datadog_api_client.v2.model.remediation_guardrail_decision import RemediationGuardrailDecision
    from datadog_api_client.v2.model.remediation_plan_source import RemediationPlanSource
    from datadog_api_client.v2.model.remediation_proposed_fix import RemediationProposedFix
    from datadog_api_client.v2.model.remediation_plan_status import RemediationPlanStatus
    from datadog_api_client.v2.model.remediation_step import RemediationStep


class RemediationPlan(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_confidence import RemediationConfidence
        from datadog_api_client.v2.model.remediation_guardrail_decision import RemediationGuardrailDecision
        from datadog_api_client.v2.model.remediation_plan_source import RemediationPlanSource
        from datadog_api_client.v2.model.remediation_proposed_fix import RemediationProposedFix
        from datadog_api_client.v2.model.remediation_plan_status import RemediationPlanStatus
        from datadog_api_client.v2.model.remediation_step import RemediationStep

        return {
            "confidence": (RemediationConfidence,),
            "evidence": (str,),
            "explanation": (str,),
            "guardrail_decision": (RemediationGuardrailDecision,),
            "plan_source": (RemediationPlanSource,),
            "proposed_fix": ([RemediationProposedFix],),
            "status": (RemediationPlanStatus,),
            "steps": ([RemediationStep],),
        }

    attribute_map = {
        "confidence": "confidence",
        "evidence": "evidence",
        "explanation": "explanation",
        "guardrail_decision": "guardrail_decision",
        "plan_source": "plan_source",
        "proposed_fix": "proposed_fix",
        "status": "status",
        "steps": "steps",
    }

    def __init__(
        self_,
        confidence: Union[RemediationConfidence, UnsetType] = unset,
        evidence: Union[str, UnsetType] = unset,
        explanation: Union[str, UnsetType] = unset,
        guardrail_decision: Union[RemediationGuardrailDecision, UnsetType] = unset,
        plan_source: Union[RemediationPlanSource, UnsetType] = unset,
        proposed_fix: Union[List[RemediationProposedFix], UnsetType] = unset,
        status: Union[RemediationPlanStatus, UnsetType] = unset,
        steps: Union[List[RemediationStep], UnsetType] = unset,
        **kwargs,
    ):
        """
        The remediation plan proposed by the ECS remediation agent.

        :param confidence: The agent's self-rated confidence in a plan.
        :type confidence: RemediationConfidence, optional

        :param evidence: Evidence supporting the diagnosis. Treat as user-provided content and escape before display.
        :type evidence: str, optional

        :param explanation: Human-readable summary of why the plan was proposed. Treat as user-provided content and escape before display.
        :type explanation: str, optional

        :param guardrail_decision: The guardrail decision applied to a plan or investigation.
        :type guardrail_decision: RemediationGuardrailDecision, optional

        :param plan_source: How the plan was produced.
        :type plan_source: RemediationPlanSource, optional

        :param proposed_fix: Recommendation-oriented view of the candidate remediations, distinct from the execution-oriented steps.
        :type proposed_fix: [RemediationProposedFix], optional

        :param status: Plan status.
        :type status: RemediationPlanStatus, optional

        :param steps: Execution-oriented steps that make up the plan.
        :type steps: [RemediationStep], optional
        """
        if confidence is not unset:
            kwargs["confidence"] = confidence
        if evidence is not unset:
            kwargs["evidence"] = evidence
        if explanation is not unset:
            kwargs["explanation"] = explanation
        if guardrail_decision is not unset:
            kwargs["guardrail_decision"] = guardrail_decision
        if plan_source is not unset:
            kwargs["plan_source"] = plan_source
        if proposed_fix is not unset:
            kwargs["proposed_fix"] = proposed_fix
        if status is not unset:
            kwargs["status"] = status
        if steps is not unset:
            kwargs["steps"] = steps
        super().__init__(kwargs)
