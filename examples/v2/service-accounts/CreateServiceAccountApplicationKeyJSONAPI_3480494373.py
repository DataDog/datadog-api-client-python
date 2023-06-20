"""
Create an application key with scopes for this service account returns "Created" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequestJSON

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

body = ApplicationKeyCreateRequestJSON(
    name="Example-Service-Account",
    scopes=[
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, body=body
    )

    print(response)
