"""
Delete Fastly account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    api_instance.delete_fastly_account(
        account_id="account_id",
    )
