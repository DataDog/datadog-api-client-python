"""
Update a Workload Protection agent rule (US1-FED) returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action import CloudWorkloadSecurityAgentRuleAction
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_core_dump import (
    CloudWorkloadSecurityAgentRuleActionCoreDump,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_action_hash import (
    CloudWorkloadSecurityAgentRuleActionHash,
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
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import CloudWorkloadSecurityAgentRuleKill
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
    CloudWorkloadSecurityAgentRuleUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_data import (
    CloudWorkloadSecurityAgentRuleUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_request import (
    CloudWorkloadSecurityAgentRuleUpdateRequest,
)

body = CloudWorkloadSecurityAgentRuleUpdateRequest(
    data=CloudWorkloadSecurityAgentRuleUpdateData(
        attributes=CloudWorkloadSecurityAgentRuleUpdateAttributes(
            actions=[
                CloudWorkloadSecurityAgentRuleAction(
                    coredump=CloudWorkloadSecurityAgentRuleActionCoreDump(),
                    disabled=False,
                    hash=CloudWorkloadSecurityAgentRuleActionHash(),
                    kill=CloudWorkloadSecurityAgentRuleKill(),
                    log=CloudWorkloadSecurityAgentRuleActionLog(),
                    metadata=CloudWorkloadSecurityAgentRuleActionMetadata(),
                    network_filter=CloudWorkloadSecurityAgentRuleActionNetworkFilter(),
                    set=CloudWorkloadSecurityAgentRuleActionSet(),
                ),
            ],
            blocking=[],
            description="My Agent rule",
            disabled=[],
            enabled=True,
            expression='exec.file.name == "sh"',
            monitoring=[],
            policy_id="a8c8e364-6556-434d-b798-a4c23de29c0b",
            product_tags=[],
            silent=False,
        ),
        id="3dd-0uc-h1s",
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.update_cloud_workload_security_agent_rule(agent_rule_id="agent_rule_id", body=body)

    print(response)
