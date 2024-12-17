"""
Deploy App returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_deployment_api import AppDeploymentApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["deploy_app"] = True
with ApiClient(configuration) as api_client:
    api_instance = AppDeploymentApi(api_client)
    response = api_instance.deploy_app(
        app_id=APP_DATA_ID,
    )

    print(response)
