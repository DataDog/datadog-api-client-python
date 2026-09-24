"""
List execution policies returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_execution_policies"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.list_execution_policies()

    print(response)
