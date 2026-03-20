"""
Get a deployment gates evaluation result returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gates_evaluation" in the system
DEPLOYMENT_GATES_EVALUATION_DATA_ID = environ["DEPLOYMENT_GATES_EVALUATION_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_deployment_gates_evaluation_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_gates_evaluation_result(
        id=DEPLOYMENT_GATES_EVALUATION_DATA_ID,
    )

    print(response)
