"""
Revoke an access token for a service account returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_access_token" for "service_account_user"
SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID = environ["SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    api_instance.revoke_service_account_access_token(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID,
        pat_id=SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID,
    )
