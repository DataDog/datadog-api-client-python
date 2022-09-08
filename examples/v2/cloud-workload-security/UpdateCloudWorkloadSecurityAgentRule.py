"""
Update a Cloud Workload Security Agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi
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

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleUpdateRequest(
    data=CloudWorkloadSecurityAgentRuleUpdateData(
        attributes=CloudWorkloadSecurityAgentRuleUpdateAttributes(
            description="Test Agent rule",
            enabled=True,
            expression='exec.file.name == "sh"',
        ),
        type=CloudWorkloadSecurityAgentRuleType.AGENT_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    response = api_instance.update_cloud_workload_security_agent_rule(agent_rule_id=AGENT_RULE_DATA_ID, body=body)

    print(response)
