"""
Update Fastly service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_service_attributes import FastlyServiceAttributes
from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData
from datadog_api_client.v2.model.fastly_service_request import FastlyServiceRequest
from datadog_api_client.v2.model.fastly_service_type import FastlyServiceType

body = FastlyServiceRequest(
    data=FastlyServiceData(
        attributes=FastlyServiceAttributes(
            tags=[
                "myTag",
                "myTag2:myValue",
            ],
        ),
        id="abc123",
        type=FastlyServiceType.FASTLY_SERVICES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.update_fastly_service(account_id="account_id", service_id="service_id", body=body)

    print(response)
