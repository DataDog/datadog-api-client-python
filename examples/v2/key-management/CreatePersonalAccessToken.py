"""
Create a personal access token returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.personal_access_token_create_attributes import PersonalAccessTokenCreateAttributes
from datadog_api_client.v2.model.personal_access_token_create_data import PersonalAccessTokenCreateData
from datadog_api_client.v2.model.personal_access_token_create_request import PersonalAccessTokenCreateRequest
from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType

body = PersonalAccessTokenCreateRequest(
    data=PersonalAccessTokenCreateData(
        type=PersonalAccessTokensType.PERSONAL_ACCESS_TOKENS,
        attributes=PersonalAccessTokenCreateAttributes(
            name="Example-Key-Management",
            scopes=[
                "dashboards_read",
            ],
            expires_at=(datetime.now() + relativedelta(days=365)),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_personal_access_token(body=body)

    print(response)
