"""
Create a Workload Protection agent rule (US1-FED) returns "OK" response
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
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_kill import CloudWorkloadSecurityAgentRuleKill
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
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
            filters=[],
            monitoring=[],
            name="my_agent_rule",
            policy_id="a8c8e364-6556-434d-b798-a4c23de29c0b",
            product_tags=[],
            silent=False,
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_cloud_workload_security_agent_rule(body=body)

    print(response)
