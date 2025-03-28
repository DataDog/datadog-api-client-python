"""
Batch update CSM Threats Agent policies returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes import (
    CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_attributes_policies_items import (
    CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_data import (
    CloudWorkloadSecurityAgentPolicyBatchUpdateData,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_data_type import (
    CloudWorkloadSecurityAgentPolicyBatchUpdateDataType,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_batch_update_request import (
    CloudWorkloadSecurityAgentPolicyBatchUpdateRequest,
)

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

body = CloudWorkloadSecurityAgentPolicyBatchUpdateRequest(
    data=CloudWorkloadSecurityAgentPolicyBatchUpdateData(
        attributes=CloudWorkloadSecurityAgentPolicyBatchUpdateAttributes(
            policies=[
                CloudWorkloadSecurityAgentPolicyBatchUpdateAttributesPoliciesItems(
                    delete=False,
                    description="Updated agent policy",
                    enabled=True,
                    host_tags=[
                        "env:test",
                    ],
                    id=POLICY_DATA_ID,
                    name="updated_agent_policy",
                    priority=20,
                ),
            ],
        ),
        id="batch_update_req",
        type=CloudWorkloadSecurityAgentPolicyBatchUpdateDataType.POLICIES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.batch_update_csm_threats_agent_policy(body=body)

    print(response)
