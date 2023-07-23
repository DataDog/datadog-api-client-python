"""
Add Fastly account returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_account_create_request import FastlyAccountCreateRequestJSON

body = FastlyAccountCreateRequestJSON(
    api_key="ExampleFastlyIntegration",
    name="Example-Fastly-Integration",
    services=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.create_fastly_account(body=body)

    print(response)
