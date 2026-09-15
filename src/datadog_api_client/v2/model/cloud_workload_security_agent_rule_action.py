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
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_core_dump import (
        CloudWorkloadSecurityAgentRuleActionCoreDump,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
        CloudWorkloadSecurityAgentRuleActionHash,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import CloudWorkloadSecurityAgentRuleKill
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_log import (
        CloudWorkloadSecurityAgentRuleActionLog,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_metadata import (
        CloudWorkloadSecurityAgentRuleActionMetadata,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_network_filter import (
        CloudWorkloadSecurityAgentRuleActionNetworkFilter,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
        CloudWorkloadSecurityAgentRuleActionSet,
    )


class CloudWorkloadSecurityAgentRuleAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_core_dump import (
            CloudWorkloadSecurityAgentRuleActionCoreDump,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
            CloudWorkloadSecurityAgentRuleActionHash,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import (
            CloudWorkloadSecurityAgentRuleKill,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_log import (
            CloudWorkloadSecurityAgentRuleActionLog,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_metadata import (
            CloudWorkloadSecurityAgentRuleActionMetadata,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_network_filter import (
            CloudWorkloadSecurityAgentRuleActionNetworkFilter,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_set import (
            CloudWorkloadSecurityAgentRuleActionSet,
        )

        return {
            "coredump": (CloudWorkloadSecurityAgentRuleActionCoreDump,),
            "disabled": (bool,),
            "filter": (str,),
            "hash": (CloudWorkloadSecurityAgentRuleActionHash,),
            "kill": (CloudWorkloadSecurityAgentRuleKill,),
            "log": (CloudWorkloadSecurityAgentRuleActionLog,),
            "metadata": (CloudWorkloadSecurityAgentRuleActionMetadata,),
            "network_filter": (CloudWorkloadSecurityAgentRuleActionNetworkFilter,),
            "set": (CloudWorkloadSecurityAgentRuleActionSet,),
        }

    attribute_map = {
        "coredump": "coredump",
        "disabled": "disabled",
        "filter": "filter",
        "hash": "hash",
        "kill": "kill",
        "log": "log",
        "metadata": "metadata",
        "network_filter": "network_filter",
        "set": "set",
    }

    def __init__(
        self_,
        coredump: Union[CloudWorkloadSecurityAgentRuleActionCoreDump, UnsetType] = unset,
        disabled: Union[bool, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        hash: Union[CloudWorkloadSecurityAgentRuleActionHash, UnsetType] = unset,
        kill: Union[CloudWorkloadSecurityAgentRuleKill, UnsetType] = unset,
        log: Union[CloudWorkloadSecurityAgentRuleActionLog, UnsetType] = unset,
        metadata: Union[CloudWorkloadSecurityAgentRuleActionMetadata, UnsetType] = unset,
        network_filter: Union[CloudWorkloadSecurityAgentRuleActionNetworkFilter, UnsetType] = unset,
        set: Union[CloudWorkloadSecurityAgentRuleActionSet, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action the rule can perform if triggered

        :param coredump: The core dump action applied on the process matching the rule.
        :type coredump: CloudWorkloadSecurityAgentRuleActionCoreDump, optional

        :param disabled: Whether the action is disabled
        :type disabled: bool, optional

        :param filter: SECL expression used to target the container to apply the action on
        :type filter: str, optional

        :param hash: Hash file specified by the field attribute
        :type hash: CloudWorkloadSecurityAgentRuleActionHash, optional

        :param kill: Kill system call applied on the container matching the rule
        :type kill: CloudWorkloadSecurityAgentRuleKill, optional

        :param log: The log action applied when the rule is triggered.
        :type log: CloudWorkloadSecurityAgentRuleActionLog, optional

        :param metadata: The metadata action applied on the scope matching the rule
        :type metadata: CloudWorkloadSecurityAgentRuleActionMetadata, optional

        :param network_filter: The network filter action applied on the network traffic matching the rule.
        :type network_filter: CloudWorkloadSecurityAgentRuleActionNetworkFilter, optional

        :param set: The set action applied on the scope matching the rule
        :type set: CloudWorkloadSecurityAgentRuleActionSet, optional
        """
        if coredump is not unset:
            kwargs["coredump"] = coredump
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if filter is not unset:
            kwargs["filter"] = filter
        if hash is not unset:
            kwargs["hash"] = hash
        if kill is not unset:
            kwargs["kill"] = kill
        if log is not unset:
            kwargs["log"] = log
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if network_filter is not unset:
            kwargs["network_filter"] = network_filter
        if set is not unset:
            kwargs["set"] = set
        super().__init__(kwargs)
