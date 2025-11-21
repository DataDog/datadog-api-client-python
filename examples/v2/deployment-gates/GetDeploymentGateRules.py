"""
Get rules for a deployment gate returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.deployment_gates_api import DeploymentGatesApi

# there is a valid "deployment_gate" in the system
DEPLOYMENT_GATE_DATA_ID = environ["DEPLOYMENT_GATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_deployment_gate_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = DeploymentGatesApi(api_client)
    response = api_instance.get_deployment_gate_rules(
        gate_id=DEPLOYMENT_GATE_DATA_ID,
    )

    print(response)
