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
    from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
    from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition
    from datadog_api_client.v2.model.incident_rule_trigger_type import IncidentRuleTriggerType


class IncidentRulePatchDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
        from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition
        from datadog_api_client.v2.model.incident_rule_trigger_type import IncidentRuleTriggerType

        return {
            "condition": (IncidentRuleQueryCondition,),
            "conditions": ([IncidentRuleCondition],),
            "enabled": (bool,),
            "task_payload": (str,),
            "trigger": (IncidentRuleTriggerType,),
        }

    attribute_map = {
        "condition": "condition",
        "conditions": "conditions",
        "enabled": "enabled",
        "task_payload": "task_payload",
        "trigger": "trigger",
    }

    def __init__(
        self_,
        condition: Union[IncidentRuleQueryCondition, UnsetType] = unset,
        conditions: Union[List[IncidentRuleCondition], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        task_payload: Union[str, UnsetType] = unset,
        trigger: Union[IncidentRuleTriggerType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching an incident rule. All fields are optional.

        :param condition: A query-based condition for an incident rule.
        :type condition: IncidentRuleQueryCondition, optional

        :param conditions: List of field-based conditions.
        :type conditions: [IncidentRuleCondition], optional

        :param enabled: Whether the rule is enabled.
        :type enabled: bool, optional

        :param task_payload: The JSON-encoded payload for the task.
        :type task_payload: str, optional

        :param trigger: The trigger event for an incident rule.
        :type trigger: IncidentRuleTriggerType, optional
        """
        if condition is not unset:
            kwargs["condition"] = condition
        if conditions is not unset:
            kwargs["conditions"] = conditions
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if task_payload is not unset:
            kwargs["task_payload"] = task_payload
        if trigger is not unset:
            kwargs["trigger"] = trigger
        super().__init__(kwargs)
