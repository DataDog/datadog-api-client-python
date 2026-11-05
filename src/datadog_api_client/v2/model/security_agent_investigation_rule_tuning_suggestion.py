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
    from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_condition import (
        SecurityAgentInvestigationRuleTuningCondition,
    )


class SecurityAgentInvestigationRuleTuningSuggestion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_rule_tuning_condition import (
            SecurityAgentInvestigationRuleTuningCondition,
        )

        return {
            "action_type": (str,),
            "conditions": ([SecurityAgentInvestigationRuleTuningCondition],),
            "description": (str,),
            "estimated_silenced_count": (int,),
            "id": (str,),
            "match_logic": (str,),
            "recommended": (bool,),
            "rule_id": (str,),
            "title": (str,),
            "warning": (str,),
            "why": (str,),
        }

    attribute_map = {
        "action_type": "action_type",
        "conditions": "conditions",
        "description": "description",
        "estimated_silenced_count": "estimated_silenced_count",
        "id": "id",
        "match_logic": "match_logic",
        "recommended": "recommended",
        "rule_id": "rule_id",
        "title": "title",
        "warning": "warning",
        "why": "why",
    }

    def __init__(
        self_,
        action_type: str,
        conditions: List[SecurityAgentInvestigationRuleTuningCondition],
        description: str,
        id: str,
        match_logic: str,
        recommended: bool,
        rule_id: str,
        title: str,
        warning: str,
        why: str,
        estimated_silenced_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A suggestion to tune the detection rule.

        :param action_type: Kind of change the suggestion makes to the rule.
        :type action_type: str

        :param conditions: The conditions the change applies to.
        :type conditions: [SecurityAgentInvestigationRuleTuningCondition]

        :param description: What the suggestion changes.
        :type description: str

        :param estimated_silenced_count: Estimated number of signals the change would have silenced in the window.
        :type estimated_silenced_count: int, optional

        :param id: ID of the suggestion.
        :type id: str

        :param match_logic: How the conditions combine, such as AND or OR.
        :type match_logic: str

        :param recommended: Whether the suggestion is recommended.
        :type recommended: bool

        :param rule_id: ID of the detection rule.
        :type rule_id: str

        :param title: Title of the suggestion.
        :type title: str

        :param warning: What the change could hide. It can be empty.
        :type warning: str

        :param why: Why the suggestion is made.
        :type why: str
        """
        if estimated_silenced_count is not unset:
            kwargs["estimated_silenced_count"] = estimated_silenced_count
        super().__init__(kwargs)

        self_.action_type = action_type
        self_.conditions = conditions
        self_.description = description
        self_.id = id
        self_.match_logic = match_logic
        self_.recommended = recommended
        self_.rule_id = rule_id
        self_.title = title
        self_.warning = warning
        self_.why = why
