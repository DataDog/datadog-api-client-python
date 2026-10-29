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
    from datadog_api_client.v2.model.execution_policy_kubernetes_scope import ExecutionPolicyKubernetesScope
    from datadog_api_client.v2.model.execution_policy_remote_action_rshell_scope import (
        ExecutionPolicyRemoteActionRshellScope,
    )
    from datadog_api_client.v2.model.execution_policy_script_scope import ExecutionPolicyScriptScope
    from datadog_api_client.v2.model.execution_policy_slack_scope import ExecutionPolicySlackScope


class ExecutionPolicyScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_kubernetes_scope import ExecutionPolicyKubernetesScope
        from datadog_api_client.v2.model.execution_policy_remote_action_rshell_scope import (
            ExecutionPolicyRemoteActionRshellScope,
        )
        from datadog_api_client.v2.model.execution_policy_script_scope import ExecutionPolicyScriptScope
        from datadog_api_client.v2.model.execution_policy_slack_scope import ExecutionPolicySlackScope

        return {
            "kubernetes": (ExecutionPolicyKubernetesScope,),
            "remote_action_rshell": (ExecutionPolicyRemoteActionRshellScope,),
            "scripts": (ExecutionPolicyScriptScope,),
            "slack": (ExecutionPolicySlackScope,),
        }

    attribute_map = {
        "kubernetes": "kubernetes",
        "remote_action_rshell": "remote_action_rshell",
        "scripts": "scripts",
        "slack": "slack",
    }

    def __init__(
        self_,
        kubernetes: Union[ExecutionPolicyKubernetesScope, UnsetType] = unset,
        remote_action_rshell: Union[ExecutionPolicyRemoteActionRshellScope, UnsetType] = unset,
        scripts: Union[ExecutionPolicyScriptScope, UnsetType] = unset,
        slack: Union[ExecutionPolicySlackScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        Restricts where the policy applies. At most one scope type can be set,
        and it must match the action pattern's integration. An empty object means
        the policy has no scope restriction.

        :param kubernetes: Restricts the policy to specific Kubernetes namespaces.
        :type kubernetes: ExecutionPolicyKubernetesScope, optional

        :param remote_action_rshell: Restricts the policy to specific remote shell paths.
        :type remote_action_rshell: ExecutionPolicyRemoteActionRshellScope, optional

        :param scripts: Restricts the policy to specific scripts.
        :type scripts: ExecutionPolicyScriptScope, optional

        :param slack: Restricts the policy to specific Slack private channel names.
        :type slack: ExecutionPolicySlackScope, optional
        """
        if kubernetes is not unset:
            kwargs["kubernetes"] = kubernetes
        if remote_action_rshell is not unset:
            kwargs["remote_action_rshell"] = remote_action_rshell
        if scripts is not unset:
            kwargs["scripts"] = scripts
        if slack is not unset:
            kwargs["slack"] = slack
        super().__init__(kwargs)
