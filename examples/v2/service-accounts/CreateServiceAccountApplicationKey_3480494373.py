"""
Create an application key with scopes for this service account returns "Created" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        attributes=ApplicationKeyCreateAttributes(
            name="Example-Create_an_application_key_with_scopes_for_this_service_account_returns_Created_response",
            scopes=["dashboards_read", "dashboards_write", "dashboards_public_share"],
        ),
        type=ApplicationKeysType("application_keys"),
    )
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, body=body
    )

    print(response)
