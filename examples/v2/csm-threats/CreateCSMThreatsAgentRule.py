"""
Create a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
    CloudWorkloadSecurityAgentRuleCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
    CloudWorkloadSecurityAgentRuleCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleCreateRequest(
    data=CloudWorkloadSecurityAgentRuleCreateData(
        attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
            description="My Agent rule",
            enabled=True,
            expression='exec.file.name == "sh"',
            filters=[],
            name="examplecsmthreat",
            policy_id=POLICY_DATA_ID,
            product_tags=[],
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_rule(body=body)

    print(response)
