# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set_value import (
        CloudWorkloadSecurityAgentRuleActionSetValue,
    )


class CloudWorkloadSecurityAgentRuleActionSet(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set_value import (
            CloudWorkloadSecurityAgentRuleActionSetValue,
        )

        return {
            "append": (bool,),
            "default_value": (str,),
            "expression": (str,),
            "field": (str,),
            "inherited": (bool,),
            "name": (str,),
            "scope": (str,),
            "size": (int,),
            "ttl": (int,),
            "value": (CloudWorkloadSecurityAgentRuleActionSetValue,),
        }

    attribute_map = {
        "append": "append",
        "default_value": "default_value",
        "expression": "expression",
        "field": "field",
        "inherited": "inherited",
        "name": "name",
        "scope": "scope",
        "size": "size",
        "ttl": "ttl",
        "value": "value",
    }

    def __init__(
        self_,
        append: Union[bool, UnsetType] = unset,
        default_value: Union[str, UnsetType] = unset,
        expression: Union[str, UnsetType] = unset,
        field: Union[str, UnsetType] = unset,
        inherited: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        ttl: Union[int, UnsetType] = unset,
        value: Union[CloudWorkloadSecurityAgentRuleActionSetValue, str, int, bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The set action applied on the scope matching the rule

        :param append: Whether the value should be appended to the field.
        :type append: bool, optional

        :param default_value: The default value of the set action
        :type default_value: str, optional

        :param expression: The expression of the set action.
        :type expression: str, optional

        :param field: The field of the set action
        :type field: str, optional

        :param inherited: Whether the value should be inherited.
        :type inherited: bool, optional

        :param name: The name of the set action
        :type name: str, optional

        :param scope: The scope of the set action.
        :type scope: str, optional

        :param size: The size of the set action.
        :type size: int, optional

        :param ttl: The time to live of the set action.
        :type ttl: int, optional

        :param value: The value of the set action
        :type value: CloudWorkloadSecurityAgentRuleActionSetValue, optional
        """
        if append is not unset:
            kwargs["append"] = append
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if expression is not unset:
            kwargs["expression"] = expression
        if field is not unset:
            kwargs["field"] = field
        if inherited is not unset:
            kwargs["inherited"] = inherited
        if name is not unset:
            kwargs["name"] = name
        if scope is not unset:
            kwargs["scope"] = scope
        if size is not unset:
            kwargs["size"] = size
        if ttl is not unset:
            kwargs["ttl"] = ttl
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
