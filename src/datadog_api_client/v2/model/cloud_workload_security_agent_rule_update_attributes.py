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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action import (
        CloudWorkloadSecurityAgentRuleAction,
    )


class CloudWorkloadSecurityAgentRuleUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action import (
            CloudWorkloadSecurityAgentRuleAction,
        )

        return {
            "actions": ([CloudWorkloadSecurityAgentRuleAction],),
            "blocking": ([str],),
            "description": (str,),
            "disabled": ([str],),
            "enabled": (bool,),
            "expression": (str,),
            "monitoring": ([str],),
            "policy_id": (str,),
            "product_tags": ([str],),
        }

    attribute_map = {
        "actions": "actions",
        "blocking": "blocking",
        "description": "description",
        "disabled": "disabled",
        "enabled": "enabled",
        "expression": "expression",
        "monitoring": "monitoring",
        "policy_id": "policy_id",
        "product_tags": "product_tags",
    }

    def __init__(
        self_,
        actions: Union[List[CloudWorkloadSecurityAgentRuleAction], none_type, UnsetType] = unset,
        blocking: Union[List[str], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        disabled: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        expression: Union[str, UnsetType] = unset,
        monitoring: Union[List[str], UnsetType] = unset,
        policy_id: Union[str, UnsetType] = unset,
        product_tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Update an existing Cloud Workload Security Agent rule

        :param actions: The array of actions the rule can perform if triggered
        :type actions: [CloudWorkloadSecurityAgentRuleAction], none_type, optional

        :param blocking: The blocking policies that the rule belongs to
        :type blocking: [str], optional

        :param description: The description of the Agent rule
        :type description: str, optional

        :param disabled: The disabled policies that the rule belongs to
        :type disabled: [str], optional

        :param enabled: Whether the Agent rule is enabled
        :type enabled: bool, optional

        :param expression: The SECL expression of the Agent rule
        :type expression: str, optional

        :param monitoring: The monitoring policies that the rule belongs to
        :type monitoring: [str], optional

        :param policy_id: The ID of the policy where the Agent rule is saved
        :type policy_id: str, optional

        :param product_tags: The list of product tags associated with the rule
        :type product_tags: [str], optional
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if blocking is not unset:
            kwargs["blocking"] = blocking
        if description is not unset:
            kwargs["description"] = description
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if expression is not unset:
            kwargs["expression"] = expression
        if monitoring is not unset:
            kwargs["monitoring"] = monitoring
        if policy_id is not unset:
            kwargs["policy_id"] = policy_id
        if product_tags is not unset:
            kwargs["product_tags"] = product_tags
        super().__init__(kwargs)
