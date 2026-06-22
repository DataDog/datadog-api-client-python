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
    from datadog_api_client.v2.model.remediation_code_session import RemediationCodeSession
    from datadog_api_client.v2.model.remediation_guardrail_decision import RemediationGuardrailDecision
    from datadog_api_client.v2.model.remediation_history_event import RemediationHistoryEvent
    from datadog_api_client.v2.model.remediation_ecs_metadata import RemediationEcsMetadata
    from datadog_api_client.v2.model.remediation_plan import RemediationPlan
    from datadog_api_client.v2.model.remediation_investigation_status import RemediationInvestigationStatus


class RemediationInvestigation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_code_session import RemediationCodeSession
        from datadog_api_client.v2.model.remediation_guardrail_decision import RemediationGuardrailDecision
        from datadog_api_client.v2.model.remediation_history_event import RemediationHistoryEvent
        from datadog_api_client.v2.model.remediation_ecs_metadata import RemediationEcsMetadata
        from datadog_api_client.v2.model.remediation_plan import RemediationPlan
        from datadog_api_client.v2.model.remediation_investigation_status import RemediationInvestigationStatus

        return {
            "code_session": (RemediationCodeSession,),
            "created_at_ms": (str,),
            "guardrail_decision": (RemediationGuardrailDecision,),
            "history": ([RemediationHistoryEvent],),
            "id": (str,),
            "issue_type": (str,),
            "last_action_at_ms": (str,),
            "metadata": (RemediationEcsMetadata,),
            "org_id": (str,),
            "plan": (RemediationPlan,),
            "resource_arn": (str,),
            "status": (RemediationInvestigationStatus,),
            "updated_at_ms": (str,),
        }

    attribute_map = {
        "code_session": "code_session",
        "created_at_ms": "created_at_ms",
        "guardrail_decision": "guardrail_decision",
        "history": "history",
        "id": "id",
        "issue_type": "issue_type",
        "last_action_at_ms": "last_action_at_ms",
        "metadata": "metadata",
        "org_id": "org_id",
        "plan": "plan",
        "resource_arn": "resource_arn",
        "status": "status",
        "updated_at_ms": "updated_at_ms",
    }

    def __init__(
        self_,
        code_session: Union[RemediationCodeSession, UnsetType] = unset,
        created_at_ms: Union[str, UnsetType] = unset,
        guardrail_decision: Union[RemediationGuardrailDecision, UnsetType] = unset,
        history: Union[List[RemediationHistoryEvent], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        issue_type: Union[str, UnsetType] = unset,
        last_action_at_ms: Union[str, UnsetType] = unset,
        metadata: Union[RemediationEcsMetadata, UnsetType] = unset,
        org_id: Union[str, UnsetType] = unset,
        plan: Union[RemediationPlan, UnsetType] = unset,
        resource_arn: Union[str, UnsetType] = unset,
        status: Union[RemediationInvestigationStatus, UnsetType] = unset,
        updated_at_ms: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single ECS remediation investigation: a detected issue together with its proposed plan, history, and ECS workload metadata.

        :param code_session: A linked code session (for example, a pull request) for the investigation.
        :type code_session: RemediationCodeSession, optional

        :param created_at_ms: Creation time in epoch milliseconds (64-bit integer encoded as a string).
        :type created_at_ms: str, optional

        :param guardrail_decision: The guardrail decision applied to a plan or investigation.
        :type guardrail_decision: RemediationGuardrailDecision, optional

        :param history: Ordered list of history events for the investigation.
        :type history: [RemediationHistoryEvent], optional

        :param id: Unique investigation ID.
        :type id: str, optional

        :param issue_type: The detected issue type.
        :type issue_type: str, optional

        :param last_action_at_ms: Time of the last action in epoch milliseconds (64-bit integer encoded as a string).
        :type last_action_at_ms: str, optional

        :param metadata: ECS-specific context for the investigation.
        :type metadata: RemediationEcsMetadata, optional

        :param org_id: Datadog organization ID that owns the investigation (64-bit integer encoded as a string).
        :type org_id: str, optional

        :param plan: The remediation plan proposed by the ECS remediation agent.
        :type plan: RemediationPlan, optional

        :param resource_arn: ARN of the ECS resource the investigation is about.
        :type resource_arn: str, optional

        :param status: Investigation status.
        :type status: RemediationInvestigationStatus, optional

        :param updated_at_ms: Last update time in epoch milliseconds (64-bit integer encoded as a string).
        :type updated_at_ms: str, optional
        """
        if code_session is not unset:
            kwargs["code_session"] = code_session
        if created_at_ms is not unset:
            kwargs["created_at_ms"] = created_at_ms
        if guardrail_decision is not unset:
            kwargs["guardrail_decision"] = guardrail_decision
        if history is not unset:
            kwargs["history"] = history
        if id is not unset:
            kwargs["id"] = id
        if issue_type is not unset:
            kwargs["issue_type"] = issue_type
        if last_action_at_ms is not unset:
            kwargs["last_action_at_ms"] = last_action_at_ms
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if plan is not unset:
            kwargs["plan"] = plan
        if resource_arn is not unset:
            kwargs["resource_arn"] = resource_arn
        if status is not unset:
            kwargs["status"] = status
        if updated_at_ms is not unset:
            kwargs["updated_at_ms"] = updated_at_ms
        super().__init__(kwargs)
