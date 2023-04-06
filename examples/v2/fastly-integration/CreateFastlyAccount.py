"""
Add Fastly account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_account_create_request import FastlyAccountCreateRequest
from datadog_api_client.v2.model.fastly_account_create_request_attributes import FastlyAccountCreateRequestAttributes
from datadog_api_client.v2.model.fastly_account_create_request_data import FastlyAccountCreateRequestData
from datadog_api_client.v2.model.fastly_account_type import FastlyAccountType

body = FastlyAccountCreateRequest(
    data=FastlyAccountCreateRequestData(
        attributes=FastlyAccountCreateRequestAttributes(
            api_key="ExampleFastlyIntegration",
            name="Example-Fastly-Integration",
            services=[],
        ),
        type=FastlyAccountType.FASTLY_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.create_fastly_account(body=body)

    print(response)
