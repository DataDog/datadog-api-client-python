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
    from datadog_api_client.v2.model.cloud_workload_security_agent_policy_updater_attributes import (
        CloudWorkloadSecurityAgentPolicyUpdaterAttributes,
    )


class CloudWorkloadSecurityAgentPolicyAttributes(ModelNormal):
    validations = {
        "blocking_rules_count": {
            "inclusive_maximum": 2147483647,
        },
        "disabled_rules_count": {
            "inclusive_maximum": 2147483647,
        },
        "monitoring_rules_count": {
            "inclusive_maximum": 2147483647,
        },
        "rule_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_policy_updater_attributes import (
            CloudWorkloadSecurityAgentPolicyUpdaterAttributes,
        )

        return {
            "blocking_rules_count": (int,),
            "datadog_managed": (bool,),
            "description": (str,),
            "disabled_rules_count": (int,),
            "enabled": (bool,),
            "host_tags": ([str],),
            "host_tags_lists": ([[str]],),
            "monitoring_rules_count": (int,),
            "name": (str,),
            "policy_version": (str,),
            "priority": (int,),
            "rule_count": (int,),
            "update_date": (int,),
            "updated_at": (int,),
            "updater": (CloudWorkloadSecurityAgentPolicyUpdaterAttributes,),
        }

    attribute_map = {
        "blocking_rules_count": "blockingRulesCount",
        "datadog_managed": "datadogManaged",
        "description": "description",
        "disabled_rules_count": "disabledRulesCount",
        "enabled": "enabled",
        "host_tags": "hostTags",
        "host_tags_lists": "hostTagsLists",
        "monitoring_rules_count": "monitoringRulesCount",
        "name": "name",
        "policy_version": "policyVersion",
        "priority": "priority",
        "rule_count": "ruleCount",
        "update_date": "updateDate",
        "updated_at": "updatedAt",
        "updater": "updater",
    }

    def __init__(
        self_,
        blocking_rules_count: Union[int, UnsetType] = unset,
        datadog_managed: Union[bool, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        disabled_rules_count: Union[int, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        host_tags: Union[List[str], UnsetType] = unset,
        host_tags_lists: Union[List[List[str]], UnsetType] = unset,
        monitoring_rules_count: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        policy_version: Union[str, UnsetType] = unset,
        priority: Union[int, UnsetType] = unset,
        rule_count: Union[int, UnsetType] = unset,
        update_date: Union[int, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updater: Union[CloudWorkloadSecurityAgentPolicyUpdaterAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Cloud Workload Security Agent policy returned by the API

        :param blocking_rules_count: The number of rules with the blocking feature in this policy
        :type blocking_rules_count: int, optional

        :param datadog_managed: Whether the policy is managed by Datadog
        :type datadog_managed: bool, optional

        :param description: The description of the policy
        :type description: str, optional

        :param disabled_rules_count: The number of rules that are disabled in this policy
        :type disabled_rules_count: int, optional

        :param enabled: Whether the Agent policy is enabled
        :type enabled: bool, optional

        :param host_tags: The host tags defining where this policy is deployed
        :type host_tags: [str], optional

        :param host_tags_lists: The host tags defining where this policy is deployed, the inner values are linked with AND, the outer values are linked with OR
        :type host_tags_lists: [[str]], optional

        :param monitoring_rules_count: The number of rules in the monitoring state in this policy
        :type monitoring_rules_count: int, optional

        :param name: The name of the policy
        :type name: str, optional

        :param policy_version: The version of the policy
        :type policy_version: str, optional

        :param priority: The priority of the policy
        :type priority: int, optional

        :param rule_count: The number of rules in this policy
        :type rule_count: int, optional

        :param update_date: Timestamp in milliseconds when the policy was last updated
        :type update_date: int, optional

        :param updated_at: When the policy was last updated, timestamp in milliseconds
        :type updated_at: int, optional

        :param updater: The attributes of the user who last updated the policy
        :type updater: CloudWorkloadSecurityAgentPolicyUpdaterAttributes, optional
        """
        if blocking_rules_count is not unset:
            kwargs["blocking_rules_count"] = blocking_rules_count
        if datadog_managed is not unset:
            kwargs["datadog_managed"] = datadog_managed
        if description is not unset:
            kwargs["description"] = description
        if disabled_rules_count is not unset:
            kwargs["disabled_rules_count"] = disabled_rules_count
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if host_tags is not unset:
            kwargs["host_tags"] = host_tags
        if host_tags_lists is not unset:
            kwargs["host_tags_lists"] = host_tags_lists
        if monitoring_rules_count is not unset:
            kwargs["monitoring_rules_count"] = monitoring_rules_count
        if name is not unset:
            kwargs["name"] = name
        if policy_version is not unset:
            kwargs["policy_version"] = policy_version
        if priority is not unset:
            kwargs["priority"] = priority
        if rule_count is not unset:
            kwargs["rule_count"] = rule_count
        if update_date is not unset:
            kwargs["update_date"] = update_date
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updater is not unset:
            kwargs["updater"] = updater
        super().__init__(kwargs)
