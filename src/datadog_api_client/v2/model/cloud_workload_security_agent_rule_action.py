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
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import CloudWorkloadSecurityAgentRuleKill


class CloudWorkloadSecurityAgentRuleAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import (
            CloudWorkloadSecurityAgentRuleKill,
        )

        return {
            "filter": (str,),
            "kill": (CloudWorkloadSecurityAgentRuleKill,),
        }

    attribute_map = {
        "filter": "filter",
        "kill": "kill",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        kill: Union[CloudWorkloadSecurityAgentRuleKill, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action the rule can perform if triggered.

        :param filter: SECL expression used to target the container to apply the action on
        :type filter: str, optional

        :param kill: Kill system call applied on the container matching the rule
        :type kill: CloudWorkloadSecurityAgentRuleKill, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if kill is not unset:
            kwargs["kill"] = kill
        super().__init__(kwargs)
