"""
List application keys for this service account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.list_service_account_application_keys(
        service_account_id="00000000-0000-1234-0000-000000000000",
    )

    print(response)
