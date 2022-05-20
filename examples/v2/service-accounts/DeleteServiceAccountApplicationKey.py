"""
Delete an application key for this service account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    api_instance.delete_service_account_application_key(
        service_account_id="00000000-0000-1234-0000-000000000000",
        app_key_id="app_key_id",
    )
