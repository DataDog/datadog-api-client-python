"""
Delete Cloudflare account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloudflare_integration_api import CloudflareIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudflareIntegrationApi(api_client)
    api_instance.delete_cloudflare_account(
        account_id="account_id",
    )
