"""
Create a Cloud Workload Security Agent rule returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequestJSON,
)

body = CloudWorkloadSecurityAgentRuleCreateRequestJSON(
    description="Test Agent rule",
    enabled=True,
    expression='exec.file.name == "sh"',
    name="examplecloudworkloadsecurity",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    response = api_instance.create_cloud_workload_security_agent_rule(body=body)

    print(response)
