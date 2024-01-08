"""
Add Cloudflare account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_create_request import CloudflareAccountCreateRequest
from datadog_api_client.v2.model.cloudflare_account_create_request_attributes import (
    CloudflareAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.cloudflare_account_create_request_data import CloudflareAccountCreateRequestData
from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType

body = CloudflareAccountCreateRequest(
    data=CloudflareAccountCreateRequestData(
        attributes=CloudflareAccountCreateRequestAttributes(
            api_key="fakekey",
            email="dev@datadoghq.com",
            name="examplecloudflareintegration",
        ),
        type=CloudflareAccountType.CLOUDFLARE_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.create_cloudflare_account(body=body)

    print(response)
