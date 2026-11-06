"""
Create a Custom OIDC persona mapping returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.oidc_cloud_auth_claim_match_mode import OIDCCloudAuthClaimMatchMode
from datadog_api_client.v2.model.oidc_cloud_auth_claim_matcher_create import OIDCCloudAuthClaimMatcherCreate
from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_create_attributes import (
    OIDCCloudAuthPersonaMappingCreateAttributes,
)
from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_create_data import (
    OIDCCloudAuthPersonaMappingCreateData,
)
from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_create_request import (
    OIDCCloudAuthPersonaMappingCreateRequest,
)
from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_type import OIDCCloudAuthPersonaMappingType

# there is a valid "oidc_cloud_auth_provider" in the system
OIDC_CLOUD_AUTH_PROVIDER_DATA_ID = environ["OIDC_CLOUD_AUTH_PROVIDER_DATA_ID"]

# there is a valid "service_account_user_with_role" in the system
SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ID = environ["SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ID"]

body = OIDCCloudAuthPersonaMappingCreateRequest(
    data=OIDCCloudAuthPersonaMappingCreateData(
        type=OIDCCloudAuthPersonaMappingType.CUSTOM_OIDC_IDENTITY_MAPPING,
        attributes=OIDCCloudAuthPersonaMappingCreateAttributes(
            provider_id=OIDC_CLOUD_AUTH_PROVIDER_DATA_ID,
            account_uuid=SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ID,
            claim_matchers=[
                OIDCCloudAuthClaimMatcherCreate(
                    claim="sub",
                    mode=OIDCCloudAuthClaimMatchMode.EXACT,
                    values=[
                        "system:serviceaccount:controllers:example-controller",
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_oidc_cloud_auth_persona_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_oidc_cloud_auth_persona_mapping(body=body)

    print(response)
