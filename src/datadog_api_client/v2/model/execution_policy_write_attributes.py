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
    from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
    from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
    from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
    from datadog_api_client.v2.model.execution_policy_target import ExecutionPolicyTarget


class ExecutionPolicyWriteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
        from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
        from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
        from datadog_api_client.v2.model.execution_policy_target import ExecutionPolicyTarget

        return {
            "action_pattern": (ExecutionPolicyActionPattern,),
            "effect": (ExecutionPolicyEffect,),
            "name": (str,),
            "scope": (ExecutionPolicyScope,),
            "targets": ([ExecutionPolicyTarget],),
        }

    attribute_map = {
        "action_pattern": "action_pattern",
        "effect": "effect",
        "name": "name",
        "scope": "scope",
        "targets": "targets",
    }

    def __init__(
        self_,
        action_pattern: ExecutionPolicyActionPattern,
        effect: ExecutionPolicyEffect,
        name: str,
        scope: Union[ExecutionPolicyScope, UnsetType] = unset,
        targets: Union[List[ExecutionPolicyTarget], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create or update an execution policy.

        :param action_pattern: The set of actions this policy applies to.
        :type action_pattern: ExecutionPolicyActionPattern

        :param effect: Whether the policy allows or denies matching actions.
        :type effect: ExecutionPolicyEffect

        :param name: The name of the execution policy.
        :type name: str

        :param scope: Restricts where the policy applies. At most one of ``kubernetes`` , ``scripts`` ,
            or ``remote_action_rshell`` can be set. An empty object means the policy has
            no scope restriction.
        :type scope: ExecutionPolicyScope, optional

        :param targets: The targets this policy applies to.
        :type targets: [ExecutionPolicyTarget], optional
        """
        if scope is not unset:
            kwargs["scope"] = scope
        if targets is not unset:
            kwargs["targets"] = targets
        super().__init__(kwargs)

        self_.action_pattern = action_pattern
        self_.effect = effect
        self_.name = name
