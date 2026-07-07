"""
Update an identity provider returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.identity_providers_api import IdentityProvidersApi
from datadog_api_client.v2.model.identity_provider_type import IdentityProviderType
from datadog_api_client.v2.model.identity_provider_update_attributes import IdentityProviderUpdateAttributes
from datadog_api_client.v2.model.identity_provider_update_data import IdentityProviderUpdateData
from datadog_api_client.v2.model.identity_provider_update_request import IdentityProviderUpdateRequest

body = IdentityProviderUpdateRequest(
    data=IdentityProviderUpdateData(
        attributes=IdentityProviderUpdateAttributes(
            enabled=True,
        ),
        id="00000000-0000-0000-0000-000000000001",
        type=IdentityProviderType.IDENTITY_PROVIDERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IdentityProvidersApi(api_client)
    response = api_instance.update_identity_provider(idp_id="00000000-0000-0000-0000-000000000001", body=body)

    print(response)
