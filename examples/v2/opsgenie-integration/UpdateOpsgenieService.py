"""
Update a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType
from datadog_api_client.v2.model.opsgenie_service_update_attributes import OpsgenieServiceUpdateAttributes
from datadog_api_client.v2.model.opsgenie_service_update_data import OpsgenieServiceUpdateData
from datadog_api_client.v2.model.opsgenie_service_update_request import OpsgenieServiceUpdateRequest

# there is a valid "opsgenie_service" in the system
OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME = environ["OPSGENIE_SERVICE_DATA_ATTRIBUTES_NAME"]
OPSGENIE_SERVICE_DATA_ID = environ["OPSGENIE_SERVICE_DATA_ID"]

body = OpsgenieServiceUpdateRequest(
    data=OpsgenieServiceUpdateData(
        attributes=OpsgenieServiceUpdateAttributes(
            name="fake-opsgenie-service-name--updated",
            opsgenie_api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.EU,
        ),
        id=OPSGENIE_SERVICE_DATA_ID,
        type=OpsgenieServiceType.OPSGENIE_SERVICE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.update_opsgenie_service(integration_service_id=OPSGENIE_SERVICE_DATA_ID, body=body)

    print(response)
