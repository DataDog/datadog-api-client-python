# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
    from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
    from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
    from datadog_api_client.v2.model.execution_policy_target import ExecutionPolicyTarget


class ExecutionPolicyAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
        from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
        from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
        from datadog_api_client.v2.model.execution_policy_target import ExecutionPolicyTarget

        return {
            "action_pattern": (ExecutionPolicyActionPattern,),
            "created_at": (datetime,),
            "created_by": (str,),
            "effect": (ExecutionPolicyEffect,),
            "name": (str,),
            "scope": (ExecutionPolicyScope,),
            "targets": ([ExecutionPolicyTarget],),
            "updated_at": (datetime,),
            "updated_by": (str,),
            "version": (int,),
        }

    attribute_map = {
        "action_pattern": "action_pattern",
        "created_at": "created_at",
        "created_by": "created_by",
        "effect": "effect",
        "name": "name",
        "scope": "scope",
        "targets": "targets",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
        "version": "version",
    }

    def __init__(
        self_,
        action_pattern: ExecutionPolicyActionPattern,
        created_at: datetime,
        created_by: str,
        effect: ExecutionPolicyEffect,
        name: str,
        targets: List[ExecutionPolicyTarget],
        updated_at: datetime,
        updated_by: str,
        version: int,
        scope: Union[ExecutionPolicyScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        An execution policy.

        :param action_pattern: The set of actions this policy applies to.
        :type action_pattern: ExecutionPolicyActionPattern

        :param created_at: The date and time the execution policy was created.
        :type created_at: datetime

        :param created_by: The ID of the user who created the execution policy.
        :type created_by: str

        :param effect: Whether the policy allows or denies matching actions.
        :type effect: ExecutionPolicyEffect

        :param name: The name of the execution policy.
        :type name: str

        :param scope: Restricts where the policy applies. At most one of ``kubernetes`` , ``scripts`` ,
            or ``remote_action_rshell`` can be set. An empty object means the policy has
            no scope restriction.
        :type scope: ExecutionPolicyScope, optional

        :param targets: The targets this policy applies to.
        :type targets: [ExecutionPolicyTarget]

        :param updated_at: The date and time the execution policy was last updated.
        :type updated_at: datetime

        :param updated_by: The ID of the user who last updated the execution policy.
        :type updated_by: str

        :param version: The version of the execution policy. Incremented on every update.
        :type version: int
        """
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.action_pattern = action_pattern
        self_.created_at = created_at
        self_.created_by = created_by
        self_.effect = effect
        self_.name = name
        self_.targets = targets
        self_.updated_at = updated_at
        self_.updated_by = updated_by
        self_.version = version
