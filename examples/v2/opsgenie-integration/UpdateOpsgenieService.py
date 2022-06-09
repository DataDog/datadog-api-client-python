"""
Update a single service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType
from datadog_api_client.v2.model.opsgenie_service_update_attributes import OpsgenieServiceUpdateAttributes
from datadog_api_client.v2.model.opsgenie_service_update_data import OpsgenieServiceUpdateData
from datadog_api_client.v2.model.opsgenie_service_update_request import OpsgenieServiceUpdateRequest

body = OpsgenieServiceUpdateRequest(
    data=OpsgenieServiceUpdateData(
        attributes=OpsgenieServiceUpdateAttributes(
            custom_url="https://example.com",
            name="fake-opsgenie-service-name",
            opsgenie_api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType("us"),
        ),
        id="596da4af-0563-4097-90ff-07230c3f9db3",
        type=OpsgenieServiceType("opsgenie-service"),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.update_opsgenie_service(integration_service_id="integration_service_id", body=body)

    print(response)
