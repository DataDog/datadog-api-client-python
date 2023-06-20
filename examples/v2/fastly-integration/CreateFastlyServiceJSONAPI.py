"""
Add Fastly service returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_service_request import FastlyServiceRequestJSON

body = FastlyServiceRequestJSON(
    id="abc123",
    tags=[
        "myTag",
        "myTag2:myValue",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.create_fastly_service(account_id="account_id", body=body)

    print(response)
