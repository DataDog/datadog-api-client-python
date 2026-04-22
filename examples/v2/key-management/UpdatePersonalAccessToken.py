"""
Update a personal access token returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.personal_access_token_update_attributes import PersonalAccessTokenUpdateAttributes
from datadog_api_client.v2.model.personal_access_token_update_data import PersonalAccessTokenUpdateData
from datadog_api_client.v2.model.personal_access_token_update_request import PersonalAccessTokenUpdateRequest
from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType

# there is a valid "personal_access_token" in the system
PERSONAL_ACCESS_TOKEN_DATA_ID = environ["PERSONAL_ACCESS_TOKEN_DATA_ID"]

body = PersonalAccessTokenUpdateRequest(
    data=PersonalAccessTokenUpdateData(
        type=PersonalAccessTokensType.PERSONAL_ACCESS_TOKENS,
        id=PERSONAL_ACCESS_TOKEN_DATA_ID,
        attributes=PersonalAccessTokenUpdateAttributes(
            name="Example-Key-Management-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_personal_access_token(pat_id=PERSONAL_ACCESS_TOKEN_DATA_ID, body=body)

    print(response)
