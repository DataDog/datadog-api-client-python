"""
Create a new service object returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_create_request import OpsgenieServiceCreateRequestJSON
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

body = OpsgenieServiceCreateRequestJSON(
    name="Example-Opsgenie-Integration",
    opsgenie_api_key="00000000-0000-0000-0000-000000000000",
    region=OpsgenieServiceRegionType.US,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.create_opsgenie_service(body=body)

    print(response)
