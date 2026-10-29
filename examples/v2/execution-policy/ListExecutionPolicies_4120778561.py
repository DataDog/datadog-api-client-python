"""
List execution policies filtered by Slack returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_execution_policies"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.list_execution_policies(
        filter_integration=[
            ExecutionPolicyIntegration.INTEGRATION_SLACK,
        ],
    )

    print(response)
