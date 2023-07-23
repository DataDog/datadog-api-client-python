"""
Update Cloudflare account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi
from datadog_api_client.v2.model.cloudflare_account_update_request import CloudflareAccountUpdateRequestJSON

# there is a valid "cloudflare_account" in the system
CLOUDFLARE_ACCOUNT_DATA_ID = environ["CLOUDFLARE_ACCOUNT_DATA_ID"]

body = CloudflareAccountUpdateRequestJSON(
    api_key="fakekey",
    email="new@email",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    response = api_instance.update_cloudflare_account(account_id=CLOUDFLARE_ACCOUNT_DATA_ID, body=body)

    print(response)
