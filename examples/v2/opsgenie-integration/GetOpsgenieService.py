"""
Get a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ID = environ["OPSGENIE_SERVICE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.get_opsgenie_service(
        integration_service_id=OPSGENIE_SERVICE_DATA_ID,
    )

    print(response)
