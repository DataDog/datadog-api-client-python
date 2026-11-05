# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_suggestion import (
        SecurityAgentInvestigationRuleTuningSuggestion,
    )


class SecurityAgentInvestigationRuleTuningSuggestions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_suggestion import (
            SecurityAgentInvestigationRuleTuningSuggestion,
        )

        return {
            "occurrence_window_days": (int,),
            "reasoning": (str,),
            "rule_id": (str,),
            "rule_name": (str,),
            "rule_signal_total": (int,),
            "suggestions": ([SecurityAgentInvestigationRuleTuningSuggestion],),
            "summary": (str,),
        }

    attribute_map = {
        "occurrence_window_days": "occurrence_window_days",
        "reasoning": "reasoning",
        "rule_id": "rule_id",
        "rule_name": "rule_name",
        "rule_signal_total": "rule_signal_total",
        "suggestions": "suggestions",
        "summary": "summary",
    }

    def __init__(
        self_,
        occurrence_window_days: int,
        reasoning: str,
        rule_id: str,
        rule_name: str,
        rule_signal_total: int,
        suggestions: List[SecurityAgentInvestigationRuleTuningSuggestion],
        summary: str,
        **kwargs,
    ):
        """
        Suggestions to tune the detection rule that generated the signal.

        :param occurrence_window_days: Length of the window, in days.
        :type occurrence_window_days: int

        :param reasoning: Why tuning the rule is suggested.
        :type reasoning: str

        :param rule_id: ID of the detection rule.
        :type rule_id: str

        :param rule_name: Name of the detection rule.
        :type rule_name: str

        :param rule_signal_total: Number of signals the rule generated in the window.
        :type rule_signal_total: int

        :param suggestions: The tuning suggestions.
        :type suggestions: [SecurityAgentInvestigationRuleTuningSuggestion]

        :param summary: Summary of the suggestions.
        :type summary: str
        """
        super().__init__(kwargs)

        self_.occurrence_window_days = occurrence_window_days
        self_.reasoning = reasoning
        self_.rule_id = rule_id
        self_.rule_name = rule_name
        self_.rule_signal_total = rule_signal_total
        self_.suggestions = suggestions
        self_.summary = summary
