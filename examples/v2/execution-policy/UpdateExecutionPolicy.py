"""
Update an execution policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi
from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration
from datadog_api_client.v2.model.execution_policy_type import ExecutionPolicyType
from datadog_api_client.v2.model.execution_policy_update_request import ExecutionPolicyUpdateRequest
from datadog_api_client.v2.model.execution_policy_update_request_data import ExecutionPolicyUpdateRequestData
from datadog_api_client.v2.model.execution_policy_write_attributes import ExecutionPolicyWriteAttributes

# there is a valid "execution_policy" in the system
EXECUTION_POLICY_DATA_ID = environ["EXECUTION_POLICY_DATA_ID"]

body = ExecutionPolicyUpdateRequest(
    data=ExecutionPolicyUpdateRequestData(
        id=EXECUTION_POLICY_DATA_ID,
        type=ExecutionPolicyType.EXECUTION_POLICY,
        attributes=ExecutionPolicyWriteAttributes(
            name="Cassette Execution Policy Updated",
            effect=ExecutionPolicyEffect.ALLOW,
            action_pattern=ExecutionPolicyActionPattern(
                integration=ExecutionPolicyIntegration.INTEGRATION_SCRIPT,
                action_fqns=[
                    "com.datadoghq.script.*",
                ],
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_execution_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.update_execution_policy(policy_id=EXECUTION_POLICY_DATA_ID, body=body)

    print(response)
