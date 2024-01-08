"""
Update Cloudflare account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_type import CloudflareAccountType
from datadog_api_client.v2.model.cloudflare_account_update_request import CloudflareAccountUpdateRequest
from datadog_api_client.v2.model.cloudflare_account_update_request_attributes import (
    CloudflareAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.cloudflare_account_update_request_data import CloudflareAccountUpdateRequestData

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = environ["CLOUDFLARE_ACCOUNT_DATA_ID"]

body = CloudflareAccountUpdateRequest(
    data=CloudflareAccountUpdateRequestData(
        attributes=CloudflareAccountUpdateRequestAttributes(
            api_key="fakekey",
            email="dev@datadoghq.com",
            zones=[
                "zone-id-3",
            ],
        ),
        type=CloudflareAccountType.CLOUDFLARE_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.update_cloudflare_account(account_id=CLOUDFLARE_ACCOUNT_DATA_ID, body=body)

    print(response)
