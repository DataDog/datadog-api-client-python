"""
Update an access token for a service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.personal_access_token_update_attributes import PersonalAccessTokenUpdateAttributes
from datadog_api_client.v2.model.personal_access_token_update_data import PersonalAccessTokenUpdateData
from datadog_api_client.v2.model.personal_access_token_update_request import PersonalAccessTokenUpdateRequest
from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_access_token" for "service_account_user"
SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ATTRIBUTES_NAME = environ["SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ATTRIBUTES_NAME"]
SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID = environ["SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID"]

body = PersonalAccessTokenUpdateRequest(
    data=PersonalAccessTokenUpdateData(
        id=SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID,
        type=PersonalAccessTokensType.PERSONAL_ACCESS_TOKENS,
        attributes=PersonalAccessTokenUpdateAttributes(
            name="My Personal Access Token-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.update_service_account_access_token(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, pat_id=SERVICE_ACCOUNT_ACCESS_TOKEN_DATA_ID, body=body
    )

    print(response)
