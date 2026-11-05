# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_investigation_key_entities import (
        SecurityAgentInvestigationKeyEntities,
    )
    from datadog_api_client.v2.model.security_agent_investigation_key_evidence import (
        SecurityAgentInvestigationKeyEvidence,
    )
    from datadog_api_client.v2.model.security_agent_investigation_response_suggestions import (
        SecurityAgentInvestigationResponseSuggestions,
    )
    from datadog_api_client.v2.model.security_agent_investigation_signal import SecurityAgentInvestigationSignal
    from datadog_api_client.v2.model.security_agent_investigation_state import SecurityAgentInvestigationState
    from datadog_api_client.v2.model.security_agent_investigation_step import SecurityAgentInvestigationStep
    from datadog_api_client.v2.model.security_agent_investigation_verdict import SecurityAgentInvestigationVerdict


class SecurityAgentInvestigationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_key_entities import (
            SecurityAgentInvestigationKeyEntities,
        )
        from datadog_api_client.v2.model.security_agent_investigation_key_evidence import (
            SecurityAgentInvestigationKeyEvidence,
        )
        from datadog_api_client.v2.model.security_agent_investigation_response_suggestions import (
            SecurityAgentInvestigationResponseSuggestions,
        )
        from datadog_api_client.v2.model.security_agent_investigation_signal import SecurityAgentInvestigationSignal
        from datadog_api_client.v2.model.security_agent_investigation_state import SecurityAgentInvestigationState
        from datadog_api_client.v2.model.security_agent_investigation_step import SecurityAgentInvestigationStep
        from datadog_api_client.v2.model.security_agent_investigation_verdict import SecurityAgentInvestigationVerdict

        return {
            "conclusion": (str,),
            "created_at": (datetime,),
            "key_entities": (SecurityAgentInvestigationKeyEntities,),
            "key_evidence": ([SecurityAgentInvestigationKeyEvidence],),
            "response_suggestions": (SecurityAgentInvestigationResponseSuggestions,),
            "rule_id": (str,),
            "signal": (SecurityAgentInvestigationSignal,),
            "signal_id": (str,),
            "state": (SecurityAgentInvestigationState,),
            "steps": ([SecurityAgentInvestigationStep],),
            "updated_at": (datetime,),
            "verdict": (SecurityAgentInvestigationVerdict,),
        }

    attribute_map = {
        "conclusion": "conclusion",
        "created_at": "created_at",
        "key_entities": "key_entities",
        "key_evidence": "key_evidence",
        "response_suggestions": "response_suggestions",
        "rule_id": "rule_id",
        "signal": "signal",
        "signal_id": "signal_id",
        "state": "state",
        "steps": "steps",
        "updated_at": "updated_at",
        "verdict": "verdict",
    }

    def __init__(
        self_,
        conclusion: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        key_entities: Union[SecurityAgentInvestigationKeyEntities, UnsetType] = unset,
        key_evidence: Union[List[SecurityAgentInvestigationKeyEvidence], UnsetType] = unset,
        response_suggestions: Union[SecurityAgentInvestigationResponseSuggestions, UnsetType] = unset,
        rule_id: Union[str, UnsetType] = unset,
        signal: Union[SecurityAgentInvestigationSignal, UnsetType] = unset,
        signal_id: Union[str, UnsetType] = unset,
        state: Union[SecurityAgentInvestigationState, UnsetType] = unset,
        steps: Union[List[SecurityAgentInvestigationStep], UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        verdict: Union[SecurityAgentInvestigationVerdict, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an investigation. When ``fields[investigations]`` is set, only listed attributes are returned.
        Attributes the investigation doesn't have yet are absent.

        :param conclusion: Summary of the investigation's findings.
        :type conclusion: str, optional

        :param created_at: When the investigation started.
        :type created_at: datetime, optional

        :param key_entities: The entities the investigation found, by role.
        :type key_entities: SecurityAgentInvestigationKeyEntities, optional

        :param key_evidence: The evidence the verdict rests on.
        :type key_evidence: [SecurityAgentInvestigationKeyEvidence], optional

        :param response_suggestions: Suggested responses to the signal.
        :type response_suggestions: SecurityAgentInvestigationResponseSuggestions, optional

        :param rule_id: ID of the detection rule that generated the signal.
        :type rule_id: str, optional

        :param signal: Summary of the signal the investigation is about.
        :type signal: SecurityAgentInvestigationSignal, optional

        :param signal_id: ID of the signal, in its V1 form.
        :type signal_id: str, optional

        :param state: State of the investigation: ``investigating`` while it runs, ``completed`` after it has a result, or ``failed``
            when it produced no result before its timeout.
        :type state: SecurityAgentInvestigationState, optional

        :param steps: The steps of the investigation, in order.
        :type steps: [SecurityAgentInvestigationStep], optional

        :param updated_at: When the investigation last changed.
        :type updated_at: datetime, optional

        :param verdict: Verdict of the investigation. Only completed investigations have one.
        :type verdict: SecurityAgentInvestigationVerdict, optional
        """
        if conclusion is not unset:
            kwargs["conclusion"] = conclusion
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if key_entities is not unset:
            kwargs["key_entities"] = key_entities
        if key_evidence is not unset:
            kwargs["key_evidence"] = key_evidence
        if response_suggestions is not unset:
            kwargs["response_suggestions"] = response_suggestions
        if rule_id is not unset:
            kwargs["rule_id"] = rule_id
        if signal is not unset:
            kwargs["signal"] = signal
        if signal_id is not unset:
            kwargs["signal_id"] = signal_id
        if state is not unset:
            kwargs["state"] = state
        if steps is not unset:
            kwargs["steps"] = steps
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if verdict is not unset:
            kwargs["verdict"] = verdict
        super().__init__(kwargs)
