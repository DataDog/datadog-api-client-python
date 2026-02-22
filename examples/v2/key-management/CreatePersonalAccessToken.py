"""
Create personal access token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.personal_access_token_create_attributes import PersonalAccessTokenCreateAttributes
from datadog_api_client.v2.model.personal_access_token_create_data import PersonalAccessTokenCreateData
from datadog_api_client.v2.model.personal_access_token_create_request import PersonalAccessTokenCreateRequest
from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType
from datetime import datetime
from dateutil.tz import tzutc

body = PersonalAccessTokenCreateRequest(
    data=PersonalAccessTokenCreateData(
        attributes=PersonalAccessTokenCreateAttributes(
            expires_at=datetime(2025, 3, 15, 10, 30, tzinfo=tzutc()),
            name="Example Personal Access Token",
            scopes=[
                "dashboards_read",
                "monitors_read",
            ],
        ),
        type=PersonalAccessTokenType.PERSONAL_ACCESS_TOKENS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_personal_access_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_personal_access_token(body=body)

    print(response)
