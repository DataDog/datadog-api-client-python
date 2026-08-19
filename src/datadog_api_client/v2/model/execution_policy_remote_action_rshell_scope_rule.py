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
    from datadog_api_client.v2.model.execution_policy_remote_action_rshell_access import (
        ExecutionPolicyRemoteActionRshellAccess,
    )


class ExecutionPolicyRemoteActionRshellScopeRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_remote_action_rshell_access import (
            ExecutionPolicyRemoteActionRshellAccess,
        )

        return {
            "access": (ExecutionPolicyRemoteActionRshellAccess,),
            "target_paths": ([str],),
        }

    attribute_map = {
        "access": "access",
        "target_paths": "target_paths",
    }

    def __init__(self_, access: ExecutionPolicyRemoteActionRshellAccess, target_paths: List[str], **kwargs):
        """
        A rule restricting remote shell access to specific paths.

        :param access: The level of remote shell access granted for the target paths.
        :type access: ExecutionPolicyRemoteActionRshellAccess

        :param target_paths: The file system paths this rule applies to.
        :type target_paths: [str]
        """
        super().__init__(kwargs)

        self_.access = access
        self_.target_paths = target_paths
