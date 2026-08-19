"""
Delete an execution policy returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi

# there is a valid "execution_policy" in the system
EXECUTION_POLICY_DATA_ID = environ["EXECUTION_POLICY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_execution_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    api_instance.delete_execution_policy(
        policy_id=EXECUTION_POLICY_DATA_ID,
    )
