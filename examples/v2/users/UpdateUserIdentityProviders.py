"""
Update identity provider overrides for a user returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.update_user_identity_providers_request import UpdateUserIdentityProvidersRequest
from datadog_api_client.v2.model.user_relationship_identity_provider_data import UserRelationshipIdentityProviderData
from datadog_api_client.v2.model.user_relationship_identity_provider_data_type import (
    UserRelationshipIdentityProviderDataType,
)

body = UpdateUserIdentityProvidersRequest(
    data=[
        UserRelationshipIdentityProviderData(
            id="00000000-0000-0000-0000-000000000001",
            type=UserRelationshipIdentityProviderDataType.IDENTITY_PROVIDERS,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    api_instance.update_user_identity_providers(user_id="00000000-0000-9999-0000-000000000000", body=body)
