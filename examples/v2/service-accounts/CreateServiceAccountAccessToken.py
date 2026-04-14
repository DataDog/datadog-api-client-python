"""
Create an access token for a service account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType
from datadog_api_client.v2.model.service_account_access_token_create_attributes import (
    ServiceAccountAccessTokenCreateAttributes,
)
from datadog_api_client.v2.model.service_account_access_token_create_data import ServiceAccountAccessTokenCreateData
from datadog_api_client.v2.model.service_account_access_token_create_request import (
    ServiceAccountAccessTokenCreateRequest,
)

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

body = ServiceAccountAccessTokenCreateRequest(
    data=ServiceAccountAccessTokenCreateData(
        type=PersonalAccessTokensType.PERSONAL_ACCESS_TOKENS,
        attributes=ServiceAccountAccessTokenCreateAttributes(
            name="Example-Service-Account",
            scopes=[
                "dashboards_read",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_access_token(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, body=body
    )

    print(response)
