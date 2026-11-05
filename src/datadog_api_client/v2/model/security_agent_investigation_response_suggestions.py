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
    from datadog_api_client.v2.model.security_agent_investigation_mitigation_suggestion import (
        SecurityAgentInvestigationMitigationSuggestion,
    )
    from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_suggestions import (
        SecurityAgentInvestigationRuleTuningSuggestions,
    )


class SecurityAgentInvestigationResponseSuggestions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_mitigation_suggestion import (
            SecurityAgentInvestigationMitigationSuggestion,
        )
        from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_suggestions import (
            SecurityAgentInvestigationRuleTuningSuggestions,
        )

        return {
            "mitigation_suggestions": ([SecurityAgentInvestigationMitigationSuggestion],),
            "rule_tuning_suggestions": (SecurityAgentInvestigationRuleTuningSuggestions,),
        }

    attribute_map = {
        "mitigation_suggestions": "mitigation_suggestions",
        "rule_tuning_suggestions": "rule_tuning_suggestions",
    }

    def __init__(
        self_,
        mitigation_suggestions: Union[List[SecurityAgentInvestigationMitigationSuggestion], UnsetType] = unset,
        rule_tuning_suggestions: Union[SecurityAgentInvestigationRuleTuningSuggestions, UnsetType] = unset,
        **kwargs,
    ):
        """
        Suggested responses to the signal.

        :param mitigation_suggestions: Suggested mitigations, in the order to apply them.
        :type mitigation_suggestions: [SecurityAgentInvestigationMitigationSuggestion], optional

        :param rule_tuning_suggestions: Suggestions to tune the detection rule that generated the signal.
        :type rule_tuning_suggestions: SecurityAgentInvestigationRuleTuningSuggestions, optional
        """
        if mitigation_suggestions is not unset:
            kwargs["mitigation_suggestions"] = mitigation_suggestions
        if rule_tuning_suggestions is not unset:
            kwargs["rule_tuning_suggestions"] = rule_tuning_suggestions
        super().__init__(kwargs)
