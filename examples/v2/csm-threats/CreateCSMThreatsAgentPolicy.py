"""
Create a Workload Protection policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_attributes import (
    CloudWorkloadSecurityAgentPolicyCreateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_data import (
    CloudWorkloadSecurityAgentPolicyCreateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_request import (
    CloudWorkloadSecurityAgentPolicyCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import CloudWorkloadSecurityAgentPolicyType

body = CloudWorkloadSecurityAgentPolicyCreateRequest(
    data=CloudWorkloadSecurityAgentPolicyCreateData(
        attributes=CloudWorkloadSecurityAgentPolicyCreateAttributes(
            description="My agent policy",
            enabled=True,
            host_tags_lists=[
                [
                    "env:test",
                ],
            ],
            name="my_agent_policy",
        ),
        type=CloudWorkloadSecurityAgentPolicyType.POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.create_csm_threats_agent_policy(body=body)

    print(response)
