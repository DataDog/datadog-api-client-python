"""
Create a new service object returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_create_attributes import OpsgenieServiceCreateAttributes
from datadog_api_client.v2.model.opsgenie_service_create_data import OpsgenieServiceCreateData
from datadog_api_client.v2.model.opsgenie_service_create_request import OpsgenieServiceCreateRequest
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType

body = OpsgenieServiceCreateRequest(
    data=OpsgenieServiceCreateData(
        attributes=OpsgenieServiceCreateAttributes(
            name="Example-Create_a_new_service_object_returns_CREATED_response",
            opsgenie_api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.US,
        ),
        type=OpsgenieServiceType.OPSGENIE_SERVICE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.create_opsgenie_service(body=body)

    print(response)
