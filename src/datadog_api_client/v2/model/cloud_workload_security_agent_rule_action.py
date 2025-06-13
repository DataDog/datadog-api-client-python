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
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
        CloudWorkloadSecurityAgentRuleActionHash,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import CloudWorkloadSecurityAgentRuleKill
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_metadata import (
        CloudWorkloadSecurityAgentRuleActionMetadata,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
        CloudWorkloadSecurityAgentRuleActionSet,
    )


class CloudWorkloadSecurityAgentRuleAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
            CloudWorkloadSecurityAgentRuleActionHash,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import (
            CloudWorkloadSecurityAgentRuleKill,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_metadata import (
            CloudWorkloadSecurityAgentRuleActionMetadata,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
            CloudWorkloadSecurityAgentRuleActionSet,
        )

        return {
            "filter": (str,),
            "hash": (CloudWorkloadSecurityAgentRuleActionHash,),
            "kill": (CloudWorkloadSecurityAgentRuleKill,),
            "metadata": (CloudWorkloadSecurityAgentRuleActionMetadata,),
            "set": (CloudWorkloadSecurityAgentRuleActionSet,),
        }

    attribute_map = {
        "filter": "filter",
        "hash": "hash",
        "kill": "kill",
        "metadata": "metadata",
        "set": "set",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        hash: Union[CloudWorkloadSecurityAgentRuleActionHash, UnsetType] = unset,
        kill: Union[CloudWorkloadSecurityAgentRuleKill, UnsetType] = unset,
        metadata: Union[CloudWorkloadSecurityAgentRuleActionMetadata, UnsetType] = unset,
        set: Union[CloudWorkloadSecurityAgentRuleActionSet, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action the rule can perform if triggered

        :param filter: SECL expression used to target the container to apply the action on
        :type filter: str, optional

        :param hash: An empty object indicating the hash action
        :type hash: CloudWorkloadSecurityAgentRuleActionHash, optional

        :param kill: Kill system call applied on the container matching the rule
        :type kill: CloudWorkloadSecurityAgentRuleKill, optional

        :param metadata: The metadata action applied on the scope matching the rule
        :type metadata: CloudWorkloadSecurityAgentRuleActionMetadata, optional

        :param set: The set action applied on the scope matching the rule
        :type set: CloudWorkloadSecurityAgentRuleActionSet, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if hash is not unset:
            kwargs["hash"] = hash
        if kill is not unset:
            kwargs["kill"] = kill
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if set is not unset:
            kwargs["set"] = set
        super().__init__(kwargs)
