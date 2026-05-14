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
    from datadog_api_client.v2.model.incident_rule_execution_state_rule import IncidentRuleExecutionStateRule


class IncidentBatchUpdateRuleExecutionStatesDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_execution_state_rule import IncidentRuleExecutionStateRule

        return {
            "rules": ([IncidentRuleExecutionStateRule],),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: List[IncidentRuleExecutionStateRule], **kwargs):
        """
        Attributes for batch updating rule execution states.

        :param rules: List of rules to update execution states for.
        :type rules: [IncidentRuleExecutionStateRule]
        """
        super().__init__(kwargs)

        self_.rules = rules
