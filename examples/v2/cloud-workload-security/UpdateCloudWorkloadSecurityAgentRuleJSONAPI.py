"""
Update a Cloud Workload Security Agent rule returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_request import (
    CloudWorkloadSecurityAgentRuleUpdateRequestJSON,
)

# there is a valid "agent_rule" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

body = CloudWorkloadSecurityAgentRuleUpdateRequestJSON(
    description="Test Agent rule",
    enabled=True,
    expression='exec.file.name == "sh"',
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    response = api_instance.update_cloud_workload_security_agent_rule(agent_rule_id=AGENT_RULE_DATA_ID, body=body)

    print(response)
