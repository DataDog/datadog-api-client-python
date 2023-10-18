"""
Get one application key for this service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.get_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID,
        app_key_id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID,
    )

    print(response)
