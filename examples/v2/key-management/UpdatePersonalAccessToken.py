"""
Update personal access token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType
from datadog_api_client.v2.model.personal_access_token_update_attributes import PersonalAccessTokenUpdateAttributes
from datadog_api_client.v2.model.personal_access_token_update_data import PersonalAccessTokenUpdateData
from datadog_api_client.v2.model.personal_access_token_update_request import PersonalAccessTokenUpdateRequest
from uuid import UUID

body = PersonalAccessTokenUpdateRequest(
    data=PersonalAccessTokenUpdateData(
        attributes=PersonalAccessTokenUpdateAttributes(
            name="Updated Personal Access Token Name",
            scopes=[
                "dashboards_read",
                "dashboards_write",
            ],
        ),
        id=UUID("00000000-0000-0000-0000-000000000000"),
        type=PersonalAccessTokenType.PERSONAL_ACCESS_TOKENS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_personal_access_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_personal_access_token(
        pat_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
