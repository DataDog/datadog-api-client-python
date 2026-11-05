# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_investigation_signal import SecurityAgentInvestigationSignal
    from datadog_api_client.v2.model.security_agent_investigation_state import SecurityAgentInvestigationState
    from datadog_api_client.v2.model.security_agent_investigation_verdict import SecurityAgentInvestigationVerdict


class SecurityAgentInvestigationListItemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_signal import SecurityAgentInvestigationSignal
        from datadog_api_client.v2.model.security_agent_investigation_state import SecurityAgentInvestigationState
        from datadog_api_client.v2.model.security_agent_investigation_verdict import SecurityAgentInvestigationVerdict

        return {
            "created_at": (datetime,),
            "is_latest": (bool,),
            "rule_id": (str,),
            "signal": (SecurityAgentInvestigationSignal,),
            "signal_id": (str,),
            "state": (SecurityAgentInvestigationState,),
            "updated_at": (datetime,),
            "verdict": (SecurityAgentInvestigationVerdict,),
        }

    attribute_map = {
        "created_at": "created_at",
        "is_latest": "is_latest",
        "rule_id": "rule_id",
        "signal": "signal",
        "signal_id": "signal_id",
        "state": "state",
        "updated_at": "updated_at",
        "verdict": "verdict",
    }

    def __init__(
        self_,
        is_latest: bool,
        rule_id: str,
        signal_id: str,
        state: SecurityAgentInvestigationState,
        created_at: Union[datetime, UnsetType] = unset,
        signal: Union[SecurityAgentInvestigationSignal, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        verdict: Union[SecurityAgentInvestigationVerdict, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an investigation in a list. To get an investigation's full content, use the get investigation
        endpoint.

        :param created_at: When the investigation started.
        :type created_at: datetime, optional

        :param is_latest: Whether this is the latest investigation of the signal. Always true when ``filter[signal_id]`` isn't set.
        :type is_latest: bool

        :param rule_id: ID of the detection rule that generated the signal. It can be empty while the investigation runs.
        :type rule_id: str

        :param signal: Summary of the signal the investigation is about.
        :type signal: SecurityAgentInvestigationSignal, optional

        :param signal_id: ID of the signal, in its V1 form.
        :type signal_id: str

        :param state: State of the investigation: ``investigating`` while it runs, ``completed`` after it has a result, or ``failed``
            when it produced no result before its timeout.
        :type state: SecurityAgentInvestigationState

        :param updated_at: When the investigation last changed.
        :type updated_at: datetime, optional

        :param verdict: Verdict of the investigation. Only completed investigations have one.
        :type verdict: SecurityAgentInvestigationVerdict, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if signal is not unset:
            kwargs["signal"] = signal
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if verdict is not unset:
            kwargs["verdict"] = verdict
        super().__init__(kwargs)

        self_.is_latest = is_latest
        self_.rule_id = rule_id
        self_.signal_id = signal_id
        self_.state = state
