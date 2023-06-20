"""
Add Cloudflare account returns "CREATED" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_create_request import CloudflareAccountCreateRequestJSON

body = CloudflareAccountCreateRequestJSON(
    api_key="fakekey",
    email="new@email",
    name="examplecloudflareintegration",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.create_cloudflare_account(body=body)

    print(response)
