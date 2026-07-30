# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
    from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition


class IncidentRuleDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rule_query_condition import IncidentRuleQueryCondition
        from datadog_api_client.v2.model.incident_rule_condition import IncidentRuleCondition

        return {
            "condition": (IncidentRuleQueryCondition,),
            "condition_table_type": (int,),
            "conditions": ([IncidentRuleCondition],),
            "created": (datetime,),
            "created_by_uuid": (UUID,),
            "deleted": (datetime, none_type),
            "enabled": (bool,),
            "execution_type": (int,),
            "incident_settings_association_uuid": (UUID, none_type),
            "match_any_condition": (bool,),
            "modified": (datetime,),
            "modified_by_uuid": (UUID,),
            "org_id": (int,),
            "task_id": (str, none_type),
            "task_payload": (str, none_type),
            "trigger": (str,),
        }

    attribute_map = {
        "condition": "condition",
        "condition_table_type": "condition_table_type",
        "conditions": "conditions",
        "created": "created",
        "created_by_uuid": "created_by_uuid",
        "deleted": "deleted",
        "enabled": "enabled",
        "execution_type": "execution_type",
        "incident_settings_association_uuid": "incident_settings_association_uuid",
        "match_any_condition": "match_any_condition",
        "modified": "modified",
        "modified_by_uuid": "modified_by_uuid",
        "org_id": "org_id",
        "task_id": "task_id",
        "task_payload": "task_payload",
        "trigger": "trigger",
    }

    def __init__(
        self_,
        condition: Union[IncidentRuleQueryCondition, UnsetType] = unset,
        condition_table_type: Union[int, UnsetType] = unset,
        conditions: Union[List[IncidentRuleCondition], UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        created_by_uuid: Union[UUID, UnsetType] = unset,
        deleted: Union[datetime, none_type, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        execution_type: Union[int, UnsetType] = unset,
        incident_settings_association_uuid: Union[UUID, none_type, UnsetType] = unset,
        match_any_condition: Union[bool, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        modified_by_uuid: Union[UUID, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        task_id: Union[str, none_type, UnsetType] = unset,
        task_payload: Union[str, none_type, UnsetType] = unset,
        trigger: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident rule in a response.

        :param condition: A query-based condition for an incident rule.
        :type condition: IncidentRuleQueryCondition, optional

        :param condition_table_type: The condition table type.
        :type condition_table_type: int, optional

        :param conditions: List of field-based conditions.
        :type conditions: [IncidentRuleCondition], optional

        :param created: Timestamp when the rule was created.
        :type created: datetime, optional

        :param created_by_uuid: UUID of the user who created the rule.
        :type created_by_uuid: UUID, optional

        :param deleted: Timestamp when the rule was deleted.
        :type deleted: datetime, none_type, optional

        :param enabled: Whether the rule is enabled.
        :type enabled: bool, optional

        :param execution_type: The execution type of the rule.
        :type execution_type: int, optional

        :param incident_settings_association_uuid: The incident settings association UUID.
        :type incident_settings_association_uuid: UUID, none_type, optional

        :param match_any_condition: Whether any condition should match.
        :type match_any_condition: bool, optional

        :param modified: Timestamp when the rule was last modified.
        :type modified: datetime, optional

        :param modified_by_uuid: UUID of the user who last modified the rule.
        :type modified_by_uuid: UUID, optional

        :param org_id: The organization ID.
        :type org_id: int, optional

        :param task_id: The task ID.
        :type task_id: str, none_type, optional

        :param task_payload: The JSON-encoded task payload.
        :type task_payload: str, none_type, optional

        :param trigger: The trigger event for the rule.
        :type trigger: str, optional
        """
        if condition is not unset:
            kwargs["condition"] = condition
        if condition_table_type is not unset:
            kwargs["condition_table_type"] = condition_table_type
        if conditions is not unset:
            kwargs["conditions"] = conditions
        if created is not unset:
            kwargs["created"] = created
        if created_by_uuid is not unset:
            kwargs["created_by_uuid"] = created_by_uuid
        if deleted is not unset:
            kwargs["deleted"] = deleted
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if execution_type is not unset:
            kwargs["execution_type"] = execution_type
        if incident_settings_association_uuid is not unset:
            kwargs["incident_settings_association_uuid"] = incident_settings_association_uuid
        if match_any_condition is not unset:
            kwargs["match_any_condition"] = match_any_condition
        if modified is not unset:
            kwargs["modified"] = modified
        if modified_by_uuid is not unset:
            kwargs["modified_by_uuid"] = modified_by_uuid
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if task_id is not unset:
            kwargs["task_id"] = task_id
        if task_payload is not unset:
            kwargs["task_payload"] = task_payload
        if trigger is not unset:
            kwargs["trigger"] = trigger
        super().__init__(kwargs)
