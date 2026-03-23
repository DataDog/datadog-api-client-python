"""
Get all deployment gates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

configuration = Configuration()
configuration.unstable_operations["list_deployment_gates"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.list_deployment_gates()

    print(response)
