"""
Update a Workload Protection policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_type import CloudWorkloadSecurityAgentPolicyType
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_attributes import (
    CloudWorkloadSecurityAgentPolicyUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_data import (
    CloudWorkloadSecurityAgentPolicyUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_request import (
    CloudWorkloadSecurityAgentPolicyUpdateRequest,
)

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentPolicyUpdateRequest(
    data=CloudWorkloadSecurityAgentPolicyUpdateData(
        attributes=CloudWorkloadSecurityAgentPolicyUpdateAttributes(
            description="Updated agent policy",
            enabled=True,
            host_tags_lists=[
                [
                    "env:test",
                ],
            ],
            name="updated_agent_policy",
        ),
        id=POLICY_DATA_ID,
        type=CloudWorkloadSecurityAgentPolicyType.POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.update_csm_threats_agent_policy(policy_id=POLICY_DATA_ID, body=body)

    print(response)
