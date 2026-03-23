"""
Get a deployment gate evaluation result returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_deployment_gates_evaluation_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_gates_evaluation_result(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
