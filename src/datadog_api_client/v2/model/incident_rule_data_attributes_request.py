# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
    from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition
    from datadog_api_client.v2.model.incident_rule_execution_type import IncidentRuleExecutionType
    from datadog_api_client.v2.model.incident_rule_task_id_type import IncidentRuleTaskIDType
    from datadog_api_client.v2.model.incident_rule_trigger_type import IncidentRuleTriggerType


class IncidentRuleDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
        from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition
        from datadog_api_client.v2.model.incident_rule_execution_type import IncidentRuleExecutionType
        from datadog_api_client.v2.model.incident_rule_task_id_type import IncidentRuleTaskIDType
        from datadog_api_client.v2.model.incident_rule_trigger_type import IncidentRuleTriggerType

        return {
            "condition": (IncidentRuleQueryCondition,),
            "condition_table_type": (int,),
            "conditions": ([IncidentRuleCondition],),
            "enabled": (bool,),
            "execution_type": (IncidentRuleExecutionType,),
            "incident_type_uuid": (UUID, none_type),
            "match_any_condition": (bool,),
            "task_id": (IncidentRuleTaskIDType,),
            "task_payload": (str,),
            "trigger": (IncidentRuleTriggerType,),
        }

    attribute_map = {
        "condition": "condition",
        "condition_table_type": "condition_table_type",
        "conditions": "conditions",
        "enabled": "enabled",
        "execution_type": "execution_type",
        "incident_type_uuid": "incident_type_uuid",
        "match_any_condition": "match_any_condition",
        "task_id": "task_id",
        "task_payload": "task_payload",
        "trigger": "trigger",
    }

    def __init__(
        self_,
        condition: IncidentRuleQueryCondition,
        condition_table_type: int,
        enabled: bool,
        execution_type: IncidentRuleExecutionType,
        task_id: IncidentRuleTaskIDType,
        task_payload: str,
        conditions: Union[List[IncidentRuleCondition], UnsetType] = unset,
        incident_type_uuid: Union[UUID, none_type, UnsetType] = unset,
        match_any_condition: Union[bool, UnsetType] = unset,
        trigger: Union[IncidentRuleTriggerType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an incident rule.

        :param condition: A query-based condition for an incident rule.
        :type condition: IncidentRuleQueryCondition

        :param condition_table_type: The condition table type. 1 = raw query.
        :type condition_table_type: int

        :param conditions: List of field-based conditions.
        :type conditions: [IncidentRuleCondition], optional

        :param enabled: Whether the rule is enabled.
        :type enabled: bool

        :param execution_type: The execution type of an incident rule.
        :type execution_type: IncidentRuleExecutionType

        :param incident_type_uuid: The UUID of the incident type this rule applies to.
        :type incident_type_uuid: UUID, none_type, optional

        :param match_any_condition: Whether any condition (OR logic) should match instead of all (AND logic).
        :type match_any_condition: bool, optional

        :param task_id: The task ID for an incident rule.
        :type task_id: IncidentRuleTaskIDType

        :param task_payload: The JSON-encoded payload for the task.
        :type task_payload: str

        :param trigger: The trigger event for an incident rule.
        :type trigger: IncidentRuleTriggerType, optional
        """
        if conditions is not unset:
            kwargs["conditions"] = conditions
        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid
        if match_any_condition is not unset:
            kwargs["match_any_condition"] = match_any_condition
        if trigger is not unset:
            kwargs["trigger"] = trigger
        super().__init__(kwargs)

        self_.condition = condition
        self_.condition_table_type = condition_table_type
        self_.enabled = enabled
        self_.execution_type = execution_type
        self_.task_id = task_id
        self_.task_payload = task_payload
